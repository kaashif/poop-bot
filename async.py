import time
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        context = await p.chromium.launch()
        #context = await browser.new_context(record_video_dir="videos/")
        page = await context.new_page()
        await page.goto("https://python-vs-poop.anvil.app/")

        start = time.time()
        now = time.time()
        score = 0
        snake_select = page.locator("//option[text() = '🐍']/..")
        snake_option = page.locator("//option[text() = '🐍']")
        while now - start < 30:
            value = await snake_option.get_attribute("value")
            await snake_select.select_option(value=value)
            score += 1
            now = time.time()
            print(f"\r{now-start:.2f}s - {score}", end="")

        print("\ntyping initials")
        initials = page.locator("//input[@placeholder = 'Enter Three Initials']")
        await initials.fill("kjh")

        print("submitting score")
        submit = page.locator("//*[text() = 'Submit Score']/..")
        #await submit.click()

        print("waiting a bit for submission")
        await page.wait_for_timeout(1000)

        print("\ndone")

        await context.close()
        #await browser.close()

asyncio.run(main())