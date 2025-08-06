from htmlSaver import HtmlSaver
from pageExtractor import PageExtractor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class SigaaExtractor(PageExtractor):
    def __init__(self, year: int, period: int, url: str):
        super().__init__(year, period, url)

        # No window
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    # Execute
    def extract(self) -> None:
        print("Opening the page...")         # Open the page
        self.open_page()

        print("Filling year field...")       # Fill year field
        self.fill_year()

        print("Filling period field...")     # Fill period field
        self.fill_period()

        print("Clicking search button...")   # Click search button
        self.run_button()

        print("Saving HTML...")              # Save the page HTML
        self.save_html()

        print("Done")
        self.driver.quit()                   # Close the browser

    def open_page(self) -> None:
        self.driver.get(self.url)                                        

    # Fill the year field
    def fill_year (self) -> None:
        year_input = self.driver.find_element(By.ID, "form:inputAno")
        year_input.clear()
        year_input.send_keys(self.year)

    # Fill the period field
    def fill_period(self) -> None:
        period_select = Select(self.driver.find_element(By.ID, "form:inputPeriodo"))
        period_select.select_by_value(self.period)

    # Click the "Buscar" button
    def run_button(self) -> None:
        search_button = self.driver.find_element(By.XPATH, '//input[@value="Buscar"]')
        search_button.click()

    # Save the full HTML of the page
    def save_html(self) -> None:
        saver = HtmlSaver()
        saver.save(self.driver.page_source)
