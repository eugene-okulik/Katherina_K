from playwright.sync_api import Page


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name="Form Authentication").click()
    page.get_by_role('textbox', name="Username").fill('Kate')
    page.get_by_role('textbox', name="Password").fill('Tester')
    page.get_by_role('button', name=" Login").click()


def test_by_role(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Kate')
    page.get_by_placeholder('Last Name').fill('Tester')
    page.get_by_placeholder('name@example.com').fill('kate@test.test')
    page.locator('[for="gender-radio-2"]').click()
    page.get_by_placeholder('Mobile Number').fill('1234567890')
    subject = page.locator('#subjectsInput')
    subject.fill('English')
    subject.press('Enter')
    page.locator('[for="hobbies-checkbox-2"]').click()
    page.get_by_placeholder('Current Address').fill('Current Address Minsk')
    page.locator('#state').click()
    page.locator('//*[text()="NCR"]').click()
    page.locator('#city').click()
    page.locator('//*[text()="Delhi"]').click()
    page.get_by_role('button', name="Submit").click()
