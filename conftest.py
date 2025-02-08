import pytest
from selenium.webdriver.remote.webdriver import WebDriver


LANGUAGES: list[tuple[str, str, str]] = [

    ('ar', 'العربيّة', 'أضف الى سلة التسوق'),

    ('ca', 'català', 'Afegeix a la cistella'),

    ("cs", 'česky', 'Vložit do košíku'),

    ("da", 'dansk', 'Læg i kurv'),

    ('de', 'Deutsch', 'In Warenkorb legen'),

    ("en-gb", 'English', 'Add to basket'),

    ("el", 'Ελληνικά', 'Προσθήκη στο καλάθι'),

    ("es", 'español', 'Añadir al carrito'),

    ("fi", 'suomi', 'Lisää koriin'),

    ("fr", 'français', 'Ajouter au panier'),

    ("it", 'italiano', 'Aggiungi al carrello'),

    ("ko", '한국어', '장바구니 담기'),

    ("nl", 'Nederlands', 'Voeg aan winkelmand toe'),

    ("pl", 'polski', 'Dodaj do koszyka'),

    ("pt", 'Português', 'Adicionar ao carrinho'),

    ("pt-br", 'Português Brasileiro', 'Adicionar à cesta'),

    ("ro", 'Română', 'Adauga in cos'),

    ("ru", 'Русский', 'Добавить в корзину'),

    ("sk", 'Slovensky', 'Pridať do košíka'),

    ("uk", 'Українська', 'Додати в кошик'),

    ("zh-hans", '简体中文', 'Add to basket'),

]


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                    help="Choose a language")


@pytest.fixture(scope="function")
def browser(request) -> WebDriver:
    from selenium import webdriver

    browser = webdriver.Chrome()
    def browser_quit():
        browser.quit()

    request.addfinalizer(browser_quit)

    return browser


@pytest.fixture
def lang_and_expected_text(request) -> tuple[str, str]:
    """Returns the selected language and the expected text for it."""
    lang = request.config.getoption("language")
    if lang is None:
        raise pytest.UsageError("--language please specify language")
    
    def find_lang(lang) -> tuple[str, str]|None:
        for i in LANGUAGES:
            if lang in i[0]:
                return i[0], i[2]

        return None

    lang = find_lang(lang)
    if lang is None:
        raise pytest.UsageError(f"--language only the following values ​​are allowed: {",".join([i[0] for i in LANGUAGES])}")

    return lang
