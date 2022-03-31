import requests
from bs4 import BeautifulSoup
import json

class Loterias:
    Url = ""
    tipoJogo = ""
    numero = 0
    nomeMunicipioUFSorteio = ""
    dataApuracao = ""
    valorArrecadado = 0.0
    valorEstimadoProximoConcurso = 0.0
    valorAcumuladoProximoConcurso = 0.0
    valorAcumuladoConcursoEspecial = 0.0
    valorAcumuladoConcurso_0_5 = 0.0
    acumulado = False
    indicadorConcursoEspecial = 0
    dezenasSorteadasOrdemSorteio = []
    listaMunicipioUFGanhadores = []
    listaRateioPremio = []

    def __init__(self, tipo):
        if (tipo == "mega-sena"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/"
        elif(tipo == "loto-facil"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/"
        elif(tipo == "quina"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/quina/"
        elif(tipo == "loto-mania"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania/"
        elif(tipo == "time-mania"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/timemania/"
        elif(tipo == "dupla-sena"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/duplasena/"
        elif(tipo == "dia-de-sorte"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/diadesorte/"
        elif(tipo == "super-sete"):
            self.Url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/supersete/"
 
    def buscar(self,sorteio):
        url = "{}{}".format(self.Url,sorteio)
        res = requests.get(url)
        html_page = res.text
        soup = BeautifulSoup(html_page, 'html.parser')
        objeto = json.loads(soup.text)
        self.tipoJogo = objeto['tipoJogo']
        self.numero = objeto['numero']
        self.nomeMunicipioUFSorteio =  objeto['nomeMunicipioUFSorteio']
        self.dataApuracao =  objeto['dataApuracao']
        self.valorArrecadado =  objeto['valorArrecadado']
        self.valorEstimadoProximoConcurso =  objeto['valorEstimadoProximoConcurso']
        self.valorAcumuladoProximoConcurso =  objeto['valorAcumuladoProximoConcurso']
        self.valorAcumuladoConcursoEspecial = objeto['valorAcumuladoConcursoEspecial']
        self.valorAcumuladoConcurso_0_5 = objeto['valorAcumuladoConcurso_0_5']
        self.acumulado = objeto['acumulado']
        self.indicadorConcursoEspecial = objeto['indicadorConcursoEspecial']
        self.dezenasSorteadasOrdemSorteio = objeto['dezenasSorteadasOrdemSorteio']
        self.listaMunicipioUFGanhadores = objeto['listaMunicipioUFGanhadores']
        self.listaRateioPremio = objeto['listaRateioPremio']
    
    def tipo_jogo(self):
        return self.tipoJogo
    
    def concurso(self):
        return self.numero

    def Municipio_Sorteio(self):
        return self.nomeMunicipioUFSorteio

    def DataApuracao(self):
        return self.dataApuracao

    def ValorArrecadado(self):
        return self.valorArrecadado
    
    def ValorEstimadoProximoConcurso(self):
        return self.valorEstimadoProximoConcurso
    
    def ValorAcumuladoProximoConcurso(self):
        return self.valorAcumuladoProximoConcurso
    
    def ValorAcumuladoConcursoEspecial(self):
        return self.valorAcumuladoConcursoEspecial

    def ValorAcumuladoConcurso_0_5(self):
        return self.valorAcumuladoConcurso_0_5

    def Acumulado(self):
        return self.acumulado
    
    def IndicadorConcursoEspecial(self):
        self.indicadorConcursoEspecial

    def DezenasSorteadasOrdemSorteio(self):
        nova = []
        lista = self.dezenasSorteadasOrdemSorteio
        for li in lista:
            nova.append(int(li))
        return nova
    
    def ListaMunicipioUFGanhadores(self):
        la = list()
        la.append(['posicao','ganhadores','municipio','uf','nomeFatansiaUL','serie'])
        lista = self.listaMunicipioUFGanhadores
        for li in lista:
            la.append([li['posicao'], li['ganhadores'], li['municipio'], li['uf'], li['nomeFatansiaUL'], li['serie']])    
        return la
    
    def ListaRateioPremio(self):
        lista = self.listaRateioPremio
        ra = list()
        ra.append(['faixa','numeroDeGanhadores','valorPremio','descricaoFaixa'])
        for li in lista:
            ra.append([li['faixa'], li['numeroDeGanhadores'], li['valorPremio'], li['descricaoFaixa']])
        return ra