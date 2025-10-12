from scraper.extractor.sigaa_extractor import SigaaExtractor
from scraper.html.parser_html import HtmlParse
from scraper.config import CURSOS_SIGAA, DATA_FOLDER, DEFAULT_FILENAME
import os

def run_scraping():
    curso = input("Insira o curso (cdia, cc, ec): ").strip().lower()
    year = input("Insira o ano: ").strip()
    period = input("Insira o período (1/2): ").strip()

    url = CURSOS_SIGAA.get(curso)
    if not url:
        print("Curso não encontrado.")
        return

    extractor = SigaaExtractor(year, period, url)
    extractor.extract()

    # Parse automático após salvar HTML
    file_path = os.path.join(DATA_FOLDER, DEFAULT_FILENAME)
    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            html = file.read()

        parser = HtmlParse(html)
        dados = parser.parse()

        print("\nDisciplinas extraídas:")

        for d in dados:
            print(f"- {d['codigo']}: {d['disciplina']} ({len(d['turmas'])} turmas)")

    else:
        print("Arquivo HTML não encontrado para parse.")

if __name__ == "__main__":
    run_scraping()