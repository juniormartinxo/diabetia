import os
import re

from dotenv import load_dotenv

from crawler.items import PageItem
from crawler.spiders.base import BaseSpider
from crawler.utils.parsing import normalize_whitespace

load_dotenv()

_SITE_KEY_RE = re.compile(r"[^A-Za-z0-9]+")


def _normalize_site_key(value: str) -> str:
    return _SITE_KEY_RE.sub("_", value.strip()).strip("_").upper()


def _env_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def _env_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


class SiteSpider(BaseSpider):
    name = "site"

    def __init__(self, site: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        raw_site_key = (site or os.getenv("CRAWLER_SITE") or "").strip()
        if not raw_site_key:
            raise ValueError("Missing site key. Use -a site=<key> or CRAWLER_SITE.")

        site_key = _normalize_site_key(raw_site_key)
        if not site_key:
            raise ValueError("Invalid site key for environment variables.")

        self.allowed_domains = _env_list(
            os.getenv(f"SITE_{site_key}_ALLOWED_DOMAINS", "")
        )
        self.start_urls = _env_list(os.getenv(f"SITE_{site_key}_START_URLS", ""))
        self.use_playwright = _env_bool(os.getenv(f"SITE_{site_key}_USE_PLAYWRIGHT"))
        self.wait_for_selector = (
            os.getenv(f"SITE_{site_key}_WAIT_FOR_SELECTOR") or None
        )

        if not self.allowed_domains:
            raise ValueError(f"Missing env SITE_{site_key}_ALLOWED_DOMAINS")
        if not self.start_urls:
            raise ValueError(f"Missing env SITE_{site_key}_START_URLS")

    def _iter_start_requests(self):
        for url in self.start_urls:
            yield self.make_request(
                url,
                callback=self.parse,
                use_playwright=self.use_playwright,
                wait_for_selector=self.wait_for_selector,
            )

    def start_requests(self):
        yield from self._iter_start_requests()

    async def start(self):
        for request in self._iter_start_requests():
            yield request

    def parse(self, response):
        title = normalize_whitespace(response.css("title::text").get())
        yield PageItem(url=response.url, title=title, raw_html=response.text)
