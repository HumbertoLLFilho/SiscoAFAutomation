from pandas import DataFrame

from Models.Enquadramento import Enquadramento
from Models.Envolvido import Envolvido

class Ocorrencia:
    def __init__(self) -> None:
        self.IsConfigured = False
        self.Enquadramentos = [] 
        self.Envolvidos = [] 

        self.dTypes =  {
            'Data da Análise': 'string',
            'Data de Cadastro': 'string',
            'Pessoa Obrigada': 'string',
            'Servidor público': 'string',
            'Detalhamento da ocorrência': 'string'
        }
    
    def parseFromDf(self, df: DataFrame, ind: int):
        self.NumOcorrencia = df['NumOcorrencia'][ind]

        self.CPFCNPJCom = df['CPFCNPJCom'][ind]

        self.DtInicio = df['DtInicio'][ind]
        self.DtFim = df['DtFim'][ind]

        self.AgNum = df['AgNum'][ind]
        self.AgNome = df['AgNome'][ind]
        self.AgMun = df['AgMun'][ind]
        self.AgUF = df['AgUF'][ind]
        self.VlCred = df['VlCred'][ind]
        self.VlDeb = df['VlDeb'][ind]
        self.VlProv = df['VlProv'][ind]
        self.VlProp = df['VlProp'][ind]
        self.Det = df['Det'][ind]
        
        self.IsConfigured = True

        return self
    
    def AddEnquadramentos(self, enquadramentos: []):
        for enquadramento in enquadramentos:
            if(self.NumOcorrencia == enquadramento.NumOcorrencia):
                self.Enquadramentos.append(enquadramento)

        return self
    
    def AddEnvolvidos(self, envolvidos: []):
        for envolvido in envolvidos:
            if(self.NumOcorrencia == envolvido.NumOcorrencia):
                self.Envolvidos.append(envolvido)

        return self

    def GetDTypes(self):
        return self.dTypes
