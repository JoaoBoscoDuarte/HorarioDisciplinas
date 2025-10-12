from bs4 import BeautifulSoup

class HtmlParse:

    def __init__(self, html: str):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def parse(self):
        list_of_classes = []

        container = self.soup.find('div', id='turmasAbertas')
        if not container:
            print("[!] Div 'turmasAbertas' não encontrada.")
            return []

        for table in container.select("table.listagem"):

            data = table.find("td", class_="subListagem").find('a')
            if not data:
                continue

            text_data = data.text.strip()
            code, name = text_data.split(" - ", 1)

            class_data = {
                "codigo": code.strip(),
                "disciplina": name.strip(),
                "turmas": []
            }

            for tr in table.select("tbody tr"):
                
                tds = tr.find_all("td")
                if len(tds) < 5:
                    continue

                period = tds[0].text.strip()
                class_num = tds[1].text.strip()

                teacher_tag = tds[2].find("a")
                teacher = teacher_tag.text.strip() if teacher_tag else ""
                lattes = teacher_tag['href'].strip() if teacher_tag and 'href' in teacher_tag.attrs else ""

                slots = tds[3].text.strip()
                hours = tds[4].text.strip()

                class_data["turmas"].append({
                    "periodo": period,
                    "turma": class_num,
                    "docente": teacher,
                    "lattes": lattes,
                    "vagas": slots,
                    "horario": hours
                })

            list_of_classes.append(class_data)

        return list_of_classes
