import os
from scraper.config import DATA_FOLDER, DEFAULT_FILENAME

class HtmlSaver:

    def __init__(self, folder: str = DATA_FOLDER, filename: str = DEFAULT_FILENAME):
        self.folder = folder
        self.filename = filename

    def save(self, content: str) -> None:
        os.makedirs(self.folder, exist_ok=True)
        file_path = os.path.join(self.folder, self.filename)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"HTML salvo em: {file_path}")
