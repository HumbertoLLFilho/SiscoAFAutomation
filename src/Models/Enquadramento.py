from pandas import DataFrame

class Enquadramento:
    def __init__(self) -> None:
        self.IsConfigured = False
        self.CodEnq = 0
    
    def parseFromDf(self, df: DataFrame, ind: int):
        self.NumOcorrencia = df['NumOcorrencia'][ind]
        self.CodEnq = int(df['CodEnq'][ind])
        
        self.IsConfigured = True

        return self