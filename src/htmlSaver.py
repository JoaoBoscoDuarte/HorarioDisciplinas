import os

class HtmlSaver:
    def __init__(self, folder="src/data", filename="pagina.html"):
        self.folder = folder
        self.filename = filename

    def save(self, content):
        os.makedirs(self.folder, exist_ok=True)
        file_path = os.path.join(self.folder, self.filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)