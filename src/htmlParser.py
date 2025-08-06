from bs4 import BeautifulSoup # type: ignore

class HtmlParse:
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def parse(self):
        listOfClass = []

        # Takes only the div "turmasAbertas"
        listClass = self.soup.find('div', id='turmasAbertas')
        
        '''
        - Cada bloco com a tag _table_ no arquivo html apresenta como nome da classe "listagem"
        - Linha de cima -> Codigo e nome da disciplina
        - Linha de baixo -> Demias dados
        '''

        # For each table with class "listagem"
        # Only tag table of html
        for table in listClass.select("table.listagem"):
                 
            '''Dentro da tag _td_ com nome de classe "sublistagem", acessamos a tag _a_ e tem os dados:
            - Name of class
            - Code of class'''

        data = table.find("td", class_="subListagem").find('a')
        if not data:
            pass

        textOfData = data.text.strip()
        code, name = textOfData.split(" - ", 1)
        
        classData = {
            "codigo": code.strip(),
            "disciplina": name.strip(),
            "turma": []
        }

        # Pega demais dados (tag _td)
        for tr in table.select("tbody tr"):
            tds = tr.find_all("td")
            if len(tds) < 5:
                continue

                period = tds[0].text.strip()
                classNum = tds[1].text.strip()

            teacherTag = tds[2].find("a")
            teacher = teacherTag.text.strip() if teacherTag else ""

            lattes = teacherTag['href'].strip() if teacherTag and 'href' in teacherTag.attrs else ""
            slots = int(tds[3].text.strip())
            hours = tds[4].text.strip()

            classData["turma"].append({
                "periodo": period,
                "turma": classNum,
                "docente": teacher,
                "lattes": lattes,
                "vagas": slots,
                "horario": hours
            })

        listOfClass.append(classData)
        print(listOfClass)


if __name__ == "__main__":
    # Open the gtml and pass to parameter of class
    with open("data/pagina.html", "r") as file:
        html = file.read()

    hp = HtmlParse(html)
    hp.parse()

