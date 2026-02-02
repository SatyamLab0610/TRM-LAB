from playwright.async_api import async_playwright

async def crawl_site(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto(url, timeout=20000)
            await page.wait_for_timeout(5000)
            text = await page.inner_text("body")
            await browser.close()
            return {"text": text}
        except:
            await browser.close()
            return None
