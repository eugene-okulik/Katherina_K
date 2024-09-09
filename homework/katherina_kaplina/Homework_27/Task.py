from playwright.sync_api import Page, expect, BrowserContext


def test_1_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')


def test_2_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        button.click()
    new_page = new_page_event.value
    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    new_page.close()
    expect(button).to_be_enabled()


def test_3_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_button = page.locator('#colorChange')
    expect(color_button).to_have_css('color', 'rgb(220, 53, 69)')
    color_button.click()
