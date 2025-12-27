from urllib.parse import urljoin, urlparse, urlunparse


def is_valid_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
    except ValueError:
        return False

    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def normalize_url(url: str, base_url: str | None = None) -> str:
    if not url:
        return ""

    final_url = url.strip()
    if base_url:
        final_url = urljoin(base_url, final_url)

    parsed = urlparse(final_url)
    if not parsed.scheme:
        return final_url

    normalized = parsed._replace(
        scheme=parsed.scheme.lower(),
        netloc=parsed.netloc.lower(),
        fragment="",
    )

    return urlunparse(normalized)
