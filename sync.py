import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        context = p.chromium.launch()
        #context = await browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        page.goto("https://python-vs-poop.anvil.app/")

        start = time.time()
        now = time.time()
        score = 0
        snake_select = page.locator("//option[text() = '🐍']/..")
        snake_option = page.locator("//option[text() = '🐍']")
        while now - start < 30:
            value = snake_option.get_attribute("value")
            snake_select.select_option(value=value)
            score += 1
            now = time.time()
            print(f"\r{now-start:.2f}s - {score}", end="")

        print("typing initials")
        initials = page.locator("//input[@placeholder = 'Enter Three Initials']")
        initials.fill("kjh")

        print("submitting score")
        submit = page.locator("//*[text() = 'Submit Score']/..")
        #await submit.click()

        print("waiting a bit for submission")
        page.wait_for_timeout(1000)

        print("\ndone")

        context.close()
        #await browser.close()

main()