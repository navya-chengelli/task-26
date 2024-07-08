from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDBSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_text_accordion = (By.XPATH, "//*[@id='nameTextAccordion']/div[1]/label")
        self.name_input = (By.XPATH, '//input[@name="name-text-input"]')
        self.gender_dropdown = (By.NAME, "gender")
        self.birth_month_dropdown = (By.ID, "birth_month")
        self.birth_year_from = (By.NAME, "birth_date-min")
        self.birth_year_to = (By.NAME, "birth_date-max")
        self.death_year_from = (By.NAME, "death_date-min")
        self.death_year_to = (By.NAME, "death_date-max")
        self.acting_credits_from = (By.NAME, "roles")
        self.sort_by_dropdown = (By.NAME, "sort")
        self.search_button = (By.XPATH, "//button[@type='submit' and text()='Search']")

    def open(self):
        self.driver.get("https://www.imdb.com/search/name/")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(500, 500);")

    def fill_search_form(self, name, gender, birth_month, birth_year_min, birth_year_max, death_year_min,
                         death_year_max, acting_credits_min, sort_by):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_text_accordion)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_input)).send_keys(name)
        Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.gender_dropdown))).select_by_visible_text(gender)
        Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.birth_month_dropdown))).select_by_visible_text(birth_month)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birth_year_from)).send_keys(
            birth_year_min)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birth_year_to)).send_keys(birth_year_max)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_year_from)).send_keys(
            death_year_min)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_year_to)).send_keys(
            death_year_max)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.acting_credits_from)).send_keys(
            acting_credits_min)
        Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.sort_by_dropdown))).select_by_visible_text(sort_by)

    def click_search(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_button)).click()



