from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from scraper.extractor.page_extractor import PageExtractor
from scraper.html.saver import HtmlSaver


class SigaaExtractor(PageExtractor):
    def __init__(self, year: int, period: int, url: str):
        super().__init__(year, period, url)

        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def extract(self) -> None:
        print("[*] Abrindo página...")
        self.open_page()

        print("[*] Preenchendo ano...")
        self.fill_year()

        print("[*] Preenchendo período...")
        self.fill_period()

        print("[*] Buscando resultados...")
        self.run_button()

        print("[*] Salvando HTML...")
        self.save_html()

        print("[✔] Extração concluída.")
        self.driver.quit()

    def open_page(self):
        self.driver.get(self.url)

    def fill_year(self):
        year_input = self.driver.find_element(By.ID, "form:inputAno")
        year_input.clear()
        year_input.send_keys(str(self.year))

    def fill_period(self):
        period_select = Select(self.driver.find_element(By.ID, "form:inputPeriodo"))
        period_select.select_by_value(str(self.period))

    def run_button(self):
        search_button = self.driver.find_element(By.XPATH, '//input[@value="Buscar"]')
        search_button.click()
        self.wait.until(EC.presence_of_element_located((By.ID, "turmasAbertas")))

    def save_html(self):
        saver = HtmlSaver()
        saver.save(self.driver.page_source)