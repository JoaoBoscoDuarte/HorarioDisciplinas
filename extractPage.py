from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from loading_util import with_loading

class ExtractPage:

    def __init__(self):
        self.YEAR = "2025"
        self.PERIOD = "1"
        self.URL = "https://sigaa.ufpb.br/sigaa/public/curso/turmas.jsf?lc=pt_BR&id=1626669"

        # Headless mode (no window)
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)


    def main(self):
        """ _____________________________________________________________  
            Refer to the project documentation if you have any questions. 
            In case of an error, please report it.
            Created by João Bosco | Last updated: 05/21/2025 """

        with_loading(self.driver.get, self.URL, message="Opening the page") # Open the page
        
        with_loading(self.fillYear, message="Filling year field")            # Fill year field
        with_loading(self.fillPeriod, message="Filling period field")        # Fill period field
        with_loading(self.runButton, message="Clicking search button")       # Click search button
        with_loading(self.wait_for_results, message="Waiting for results")   # Save the page HTML

        with_loading(self.saveInHtml, message="Saving HTML")                 # Close the browser
        self.driver.quit()       

    # Fill the year field
    def fillYear(self):
        year_input = self.driver.find_element(By.ID, "form:inputAno")
        year_input.clear()
        year_input.send_keys(self.YEAR)

    # Fill the period field
    def fillPeriod(self):
        period_select = Select(self.driver.find_element(By.ID, "form:inputPeriodo"))
        period_select.select_by_value(self.PERIOD)

    # Click the "Buscar" button
    def runButton(self):
        buscar_button = self.driver.find_element(By.XPATH, '//input[@value="Buscar"]')
        buscar_button.click()

    # Save the full HTML of the page
    def saveInHtml(self):
        html = self.driver.page_source
        with open('pagina.html', 'w', encoding='utf-8') as f:
            f.write(html)

    def wait_for_results(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "turmasAbertas")))

# Execute
if __name__ == "__main__":
    ep = ExtractPage()
    ep.main()