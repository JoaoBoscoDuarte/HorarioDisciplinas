from SIGAAExtractor import SIGAAExtractor

def main():
    cursos = {
        "cdia": "https://sigaa.ufpb.br/sigaa/public/curso/turmas.jsf?lc=pt_BR&id=14289031",
        "cc": "https://sigaa.ufpb.br/sigaa/public/curso/turmas.jsf?lc=pt_BR&id=1626669",
        "ec": "https://sigaa.ufpb.br/sigaa/public/curso/turmas.jsf?lc=pt_BR&id=1626865",
    }

    curso = input("Insira o curso (cdia, cc, ec): ")
    year = input("Insira o ano: ")
    period = input("Insira o periodo (1/2): ")

    url = cursos.get(curso.lower())
    if not url:
        print("Curso não encontrado")
        return
    
    extractor =  SIGAAExtractor(year, period, url)
    extractor.extract()
    print("Extração fincalizad com sucesso")

if __name__ == "__main__":
    main()