import os

BOT_NAME = "crawler"

SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"

ROBOTSTXT_OBEY = True
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

ITEM_PIPELINES = {
    "crawler.pipelines.CleanPipeline": 300,
}

# Playwright integration
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

PLAYWRIGHT_BROWSER_TYPE = os.getenv("PLAYWRIGHT_BROWSER", "chromium")
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
}
PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = int(
    os.getenv("PLAYWRIGHT_NAV_TIMEOUT_MS", "30000")
)
