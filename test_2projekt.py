import re
from playwright.sync_api import Page, expect



# funguje stránka "Hledat agiliťáky"
def test_agilitak(page: Page):
    page.goto("https://www.kacr.info/")

    # Najdi tlacitko a klikni na nej
    page.get_by_role("link", name="Hledat agiliťáky").click()

    # Hledam nadpis
    expect(page.locator('div:text("Hledat agiliťáky")')).to_be_visible()




# Použiji formulář "Hledat agiliťáky" na nalezení konkrétního existujiciho agiliťáka
def test_agilitak_dana(page: Page):
    page.goto("https://www.kacr.info/")

    # Najdi tlacitko a klikni na nej
    page.get_by_role("link", name="Hledat agiliťáky").click()

    # vypln jmeno
    page.locator("#search_query").fill("humpolcova")

    # odesli formular
    page.locator('a.green:text("Hledat")').click()

    # Hledam Danu
    expect(page.locator('a:text("Dana Humpolcová")')).to_be_visible()


# test horniho hledaciho policka s existujicim psem
def test_etera(page: Page):
    page.goto("https://www.kacr.info/")

    # vypln jmeno
    page.locator("#query").fill("etera")

    #odesli
    page.keyboard.press("Enter")

    # klikni na Etera Dai Muratori
    page.locator('a:text("A3Ch Etera Dai Muratori")').click()

    expect(page.locator('h1:text("A3Ch Etera Dai Muratori")')).to_be_visible()


