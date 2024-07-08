import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    paths = r"C:\Users\HP\OneDrive\Desktop\chromedriver.exe"
    os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
#
#
#
    # tests/test_imdb_search.py
#
from imdb_search_page import IMDBSearchPage
#
def test_imdb_search(driver):
    imdb_search_page = IMDBSearchPage(driver)
    imdb_search_page.open()
    imdb_search_page.scroll_down()
    imdb_search_page.fill_search_form(
        name="lakshmi",
        gender="Male",
        birth_month="January",
        birth_year_min="1970",
        birth_year_max="1980",
        death_year_min="2000",
        death_year_max="2020",
        acting_credits_min="5",
        sort_by="Popularity Ascending"
    )
    imdb_search_page.click_search()
    # Add any assertions here to verify the results if needed
    assert "lakshmi" in driver.page_source

