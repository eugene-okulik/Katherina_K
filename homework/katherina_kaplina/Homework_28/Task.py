from playwright.sync_api import Page, expect, Route
import json
import re


def test_apple(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.wait_for_load_state('networkidle')
    page.locator('[class="rf-hcard-content-title"]').get_by_text('iPhone 16 Pro &').click()
    title = page.locator('//*[@data-autom="DigitalMat-overlay-header-0-0"]')
    expect(title).to_have_text('яблокофон 16 про')
