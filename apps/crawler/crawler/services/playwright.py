from typing import Iterable, Optional

from scrapy_playwright.page import PageMethod


def build_playwright_meta(
    *,
    wait_for_selector: Optional[str] = None,
    page_methods: Optional[Iterable[PageMethod]] = None,
    include_page: bool = False,
) -> dict:
    meta = {
        "playwright": True,
    }

    if include_page:
        meta["playwright_include_page"] = True

    methods = []
    if wait_for_selector:
        methods.append(PageMethod("wait_for_selector", wait_for_selector))
    if page_methods:
        methods.extend(page_methods)

    if methods:
        meta["playwright_page_methods"] = methods

    return meta
