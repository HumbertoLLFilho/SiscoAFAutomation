from pandas import DataFrame

class Envolvido:
    def __init__(self) -> None:
        self.IsConfigured = False
    
    def parseFromDf(self, df: DataFrame, ind: int):
        self.NumOcorrencia = df['NumOcorrencia'][ind]

        self.CPFCNPJEnv = df['CPFCNPJEnv'][ind]
        self.NmEnv = df['NmEnv'][ind]
        self.TpEnv = df['TpEnv'][ind]
        self.AgNumEnv = df['AgNumEnv'][ind]
        self.AgNomeEnv = df['AgNomeEnv'][ind]
        self.NumConta = df['NumConta'][ind]
        self.DtAbConta = df['DtAbConta'][ind]
        self.DtAtuaCad = df['DtAtuaCad'][ind]
        self.PObrigada = df['PObrigada'][ind]
        self.PEP = df['PEP'][ind]
        self.ServPub = df['ServPub'][ind]
        
        self.IsConfigured = True

        return self