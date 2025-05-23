from htmlSaver import HtmlSaver
from pageExtractor import PageExtractor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class SIGAAExtractor(PageExtractor):
    def __init__(self, year, period, url):
        super().__init__(year, period, url)

        # No window
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    # Execute
    def extract(self):
        print("Opening the page...")         # Open the page
        self.openPage()

        print("Filling year field...")       # Fill year field
        self.fillYear()

        print("Filling period field...")     # Fill period field
        self.fillPeriod()

        print("Clicking search button...")   # Click search button
        self.runButton()

        print("Saving HTML...")              # Save the page HTML
        self.saveInHtml()

        self.driver.quit()                   # Close the browser
        print("Done.")

    def openPage(self):
        self.driver.get(self.url)                                        

    # Fill the year field
    def fillYear(self):
        year_input = self.driver.find_element(By.ID, "form:inputAno")
        year_input.clear()
        year_input.send_keys(self.year)

    # Fill the period field
    def fillPeriod(self):
        period_select = Select(self.driver.find_element(By.ID, "form:inputPeriodo"))
        period_select.select_by_value(self.period)

    # Click the "Buscar" button
    def runButton(self):
        buscar_button = self.driver.find_element(By.XPATH, '//input[@value="Buscar"]')
        buscar_button.click()

    # Save the full HTML of the page
    def saveInHtml(self):
        saver = HtmlSaver()
        saver.save(self.driver.page_source)