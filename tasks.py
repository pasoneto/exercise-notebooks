from datetime import datetime
import argparse

class Task:
    def __init__(self, What, When, Obs):
        self.what = What
        self.when = datetime.strptime(When, "%d/%m/%Y")
        self.countdown = self.when - datetime.today()
        self.obs = Obs

secult_es = Task("Edital Secult", "30/09/2020", "https://prosas.com.br/editais/6063-instrucao-normativa-0012020-projeto-cultural-rubem-braga-2020?locale=en")
xudesc = Task("Edital UDESC", "05/10/2020", ["https://www.udesc.br/arquivos/ceart/id_cpmenu/8825/Orienta__es_Provas_Virtuas_PS_004_2020_CEART_UDESC_Candidatos_16015984408575_8825.pdf", "www.udesc.br/processoseletivo/042020"])
ufabc = Task("Edital UFABC", "23/10/2020", ["https://sig.ufabc.edu.br/sigaa/public/processo_seletivo/view.jsf", "file:///home/pasoneto/Documents/tasks/ncg_doutorado.pdf"])
max_plank = Task('Max Planck - Elke B. Lange & Lauren K. Fink', "01/10/2020", 'https://www.aesthetics.mpg.de/en/career/jobs/researcher-phd-candidate.html')
avaliador = Task("Edital avaliador SC", "30/10/2020", "https://prosas.com.br/editais/7854-edital-de-avaliadores-premio-nodgi-pellizzetti-de-incentivo-a-cultura-de-rio-do-sulsc-2020?locale=en")
connecticut = Task("University of Connecticut", "30/10/2020", "https://mail.google.com/mail/u/0/#label/job+oportunities/FMfcgxwJXxtGkGXKZSzRdVDldKTqRBzp")
ufg = Task("Musica - UFG", "06/10/2020", ["file:///tmp/mozilla_pasoneto0/158_20200923_1600876015-1.pdf", "file:///tmp/mozilla_pasoneto0/158_20200923_1600875919-1.pdf", "https://sistemas.ufg.br/CONCURSOS_WEB/informacoes/concurso/cd_concurso/2582"])
unespar = Task("Universidade Estadual do Parana - Musica", "22/10/2020", ["www.unespar.edu.br/concursos", "http://progesp.unespar.edu.br/menu-principal/concursos-publicos/concurso-publico/edital-n-001-2020-cpps/edital-001-2020-pss.pdf"])
maple = Task("Doutorado, Michael Schulz", "30/10/2020", "https://mail.google.com/mail/u/0/#inbox/FMfcgxwJZJdDFgzPGnxvMLsbbXMCdJvV")
sjq = Task("Concurso Sao Joaquim", "29/10/2020", "https://www.acesseconcursossc.com.br/concursos/publicacoes/MUNIC%C3%8DPIO+DE+S%C3%83O+JOAQUIM/178")
visa = Task("Visa Finland", "29/11/2020", ["https://migri.fi/en/researcher", "https://www.raja.fi/current_issues/guidelines_for_border_traffic"])
funding = Task("Funding Finland", "24/11/2020", ["https://www.oph.fi/en/development/edufi-fellowship", "https://docs.google.com/document/d/1rc3gmzPha_yxEboaM-zP6yeLLPr0RnzgXxtHfLemvv8/edit","https://docs.google.com/document/d/13LsTSA4nRn3e9R63CM5QUhELDJH39S0bMztLKPo8WMQ/edit", "Kirjaamo@oph.fi, Subject of the e-mail: EDUFI Fellowship"])
secultvix = Task("Secult Vix - Formacao", "16/11/2020", "https://prosas.com.br/dashboards/followed-oportunities")
secultes = Task("Secult ES - App", "09/12/2020", ["https://mapa.cultura.es.gov.br/oportunidade/47/", "https://secult.es.gov.br/Media/secult/2020/EDITAL%20CULTURA%20DIGITAL%20-%20LEI%20ALDIR%20BLANC%20-%20SECULT%20-%20ES%20(1).pdf"])
phd = Task("PhD next meeting", "24/11/2020", ["MIR tutorial https://www.audiolabs-erlangen.de/resources/MIR/2017_TutorialAudioMIR_ISMIR/"])
icmpc = Task("ICMPC - Abstract", "14/01/2021", "https://sites.google.com/sheffield.ac.uk/escom2021/call-for-papers")
oportunity = Task("Phd opportunity", "27/01/2021", "https://mail.google.com/mail/u/0/#inbox/FMfcgxwKjfDHlbMfvbqdRqPfJKmmRLbd")

sep = "--------------------------------------------------------------------------------------------------------"

maple = [maple.what, maple.countdown, maple.obs, sep]
ufabc = [ufabc.what, ufabc.countdown, ufabc.obs, sep]
avaliador = [avaliador.what, avaliador.countdown, avaliador.obs, sep]
connecticut = [connecticut.what, connecticut.countdown, connecticut.obs, sep]
unespar = [unespar.what, unespar.countdown, unespar.obs, sep]
sjq = [sjq.what, sjq.countdown, sjq.obs, sep] 
visa = [visa.what, visa.countdown, visa.obs, sep]
secultvix = [secultvix.what, secultvix.countdown, secultvix.obs, sep]
secultes = [secultes.what, secultes.countdown, secultes.obs, sep]
funding = [funding.what, funding.countdown, funding.obs, sep]
phd = [phd.what, phd.countdown, phd.obs, sep]
icmpc = [icmpc.what, icmpc.countdown, icmpc.obs, sep]
oportunity = [oportunity.what, oportunity.countdown, oportunity.obs, sep]

tarefas = [visa,  icmpc, oportunity] #secultes, phd, secultvix, funding, connecticut, avaliador, secult, max_plank, ufg, udesc, maple, avaliador

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
