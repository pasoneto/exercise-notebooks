

from datetime import datetime
import argparse

class Task:
    def __init__(self, What, When, Obs):
        self.what = What
        self.when = datetime.strptime(When, "%d/%m/%Y")
        self.countdown = self.when - datetime.today()
        self.obs = Obs

#secult_es = Task("Edital Secult", "30/09/2020", "https://prosas.com.br/editais/6063-instrucao-normativa-0012020-projeto-cultural-rubem-braga-2020?locale=en")
#udesc = Task("Edital UDESC", "05/10/2020", ["https://www.udesc.br/arquivos/ceart/id_cpmenu/8825/Orienta__es_Provas_Virtuas_PS_004_2020_CEART_UDESC_Candidatos_16015984408575_8825.pdf", "www.udesc.br/processoseletivo/042020"])
ufabc = Task("Edital UFABC", "23/10/2020", "file:///tmp/mozilla_pasoneto0/Edital_046.2020_-_Doutorado.pdf")
#max_plank = Task('Max Planck - Elke B. Lange & Lauren K. Fink', "01/10/2020", 'https://www.aesthetics.mpg.de/en/career/jobs/researcher-phd-candidate.html')
avaliador = Task("Edital avaliador SC", "16/10/2020", "https://prosas.com.br/editais/7854-edital-de-avaliadores-premio-nodgi-pellizzetti-de-incentivo-a-cultura-de-rio-do-sulsc-2020?locale=en")
connecticut = Task("University of Connecticut", "30/10/2020", "https://mail.google.com/mail/u/0/#label/job+oportunities/FMfcgxwJXxtGkGXKZSzRdVDldKTqRBzp")
#ufg = Task("Musica - UFG", "06/10/2020", ["file:///tmp/mozilla_pasoneto0/158_20200923_1600876015-1.pdf", "file:///tmp/mozilla_pasoneto0/158_20200923_1600875919-1.pdf", "https://sistemas.ufg.br/CONCURSOS_WEB/informacoes/concurso/cd_concurso/2582"])
unespar = Task("Universidade Estadual do Parana - Musica", "06/10/2020", ["http://progesp.unespar.edu.br/menu-principal/concursos-publicos/concurso-publico/edital-n-001-2020-cpps/edital-001-2020-pss.pdf", "http://200.201.19.32/concurso_docente_v2/menu/index/?cid=5f7b433e6ef66"])
maple = Task("Doutorado, Michael Schulz", "30/10/2020", "https://mail.google.com/mail/u/0/#inbox/FMfcgxwJZJdDFgzPGnxvMLsbbXMCdJvV")

sep = "--------------------------------------------------------------------------------------------------------"
maple = [maple.what, maple.countdown, maple.obs, sep]
ufabc = [ufabc.what, ufabc.countdown, ufabc.obs, sep]
avaliador = [avaliador.what, avaliador.countdown, avaliador.obs, sep]
connecticut = [connecticut.what, connecticut.countdown, connecticut.obs, sep]
unespar = [unespar.what, unespar.countdown, unespar.obs, sep]

tarefas = [ufabc, avaliador, connecticut, unespar, maple] #secult, max_plank, ufg, udesc

for k in tarefas:
    for j in k:
        print(j)

#def main():
#    parser = argparse.ArgumentParser(description='Process some integers.')
#    parser.add_argument('--add')
#    args = vars(parser.parse_args())
#    if 'add' in args:
#        print(f"mandou add {args['add']}")


#if __name__ == '__main__':
#    main()
