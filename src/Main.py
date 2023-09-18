import pandas as pd

from dicttoxml import dicttoxml
from Models.Ocorrencia import Ocorrencia
from Models.Enquadramento import Enquadramento
from Models.Envolvido import Envolvido
from Services.XmlService import CreateXml

## Passo a passo:
##  - Abrir o arquivo
##  - Separar cada planilha em seu objeto:
##      Planilha de Ocorrencias vira uma lista do obj "Ocorrencia", etc...
##  - Adicionar os nós e filhos de acordo com os campos de ID dentro de cada um

xls = pd.ExcelFile('..\\Lib\\Files\\SISCOAF.xlsm') # Trocar para o caminho que o excel esta

ocorrenciasDf = pd.read_excel(xls, 'OCORRENCIA')
enquadramentosDf = pd.read_excel(xls, 'ENQUADRAMENTOS')
envolvidosDf = pd.read_excel(xls, 'ENVOLVIDOS')

ocorrenciasDf['DtInicio'] = pd.to_datetime(ocorrenciasDf.DtInicio)
ocorrenciasDf['DtFim'] = pd.to_datetime(ocorrenciasDf.DtFim)

ocorrenciasDf['DtInicio'] = ocorrenciasDf['DtInicio'].dt.strftime('%d/%m/%Y')
ocorrenciasDf['DtFim'] = ocorrenciasDf['DtFim'].dt.strftime('%d/%m/%Y')

envolvidosDf['DtAbConta'] = pd.to_datetime(envolvidosDf.DtAbConta)
envolvidosDf['DtAtuaCad'] = pd.to_datetime(envolvidosDf.DtAtuaCad)

envolvidosDf['DtAbConta'] = envolvidosDf['DtAbConta'].dt.strftime('%d/%m/%Y')
envolvidosDf['DtAtuaCad'] = envolvidosDf['DtAtuaCad'].dt.strftime('%d/%m/%Y')

ocorrencias = []
enquadramentos = []
envolvidos = []

for ind in envolvidosDf.index:
    envolvido = Envolvido().parseFromDf(envolvidosDf, ind)

    envolvidos.append(envolvido)

for ind in enquadramentosDf.index:
    enquadramento = Enquadramento().parseFromDf(enquadramentosDf, ind)

    enquadramentos.append(enquadramento)

for ind in ocorrenciasDf.index:
    ocorrencia = Ocorrencia()
    

    ocorrencia.parseFromDf(ocorrenciasDf, ind).AddEnquadramentos(enquadramentos).AddEnvolvidos(envolvidos)

    ocorrencias.append(ocorrencia)

CreateXml(ocorrencias)