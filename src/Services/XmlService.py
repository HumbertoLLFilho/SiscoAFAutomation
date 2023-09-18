import xml.etree.ElementTree as ET
import time

from Models.Ocorrencia import Ocorrencia

dataReporte = ('SISCOAF')+(str(time.strftime('%d%m%Y')))

def CreateXml(ocorrencias: list[Ocorrencia]):
    lote = ET.Element("LOTE")
    ocx = ET.SubElement(lote, "OCORRENCIAS", ID=dataReporte)

    for ocorrencia in ocorrencias:
        ocorrenciaElement = ET.SubElement(ocx, "OCORRENCIA")

        ocorrenciaElement = formatOcorrenciaElement(ocorrenciaElement, ocorrencia)

        enquadramentosElement = ET.SubElement(ocorrenciaElement, "ENQUADRAMENTOS")
        for enquadramento in ocorrencia.Enquadramentos:
            enquadramentoElement = ET.SubElement(enquadramentosElement, "ENQUADRAMENTO")

            enquadramentoElement = formatEnquadramentoElement(enquadramentoElement, enquadramento)
        
        envolvidosElement = ET.SubElement(ocorrenciaElement, "ENVOLVIDOS")
        for envolvido in ocorrencia.Envolvidos:
            envolvidoElement = ET.SubElement(envolvidosElement, "ENVOLVIDO")

            envolvidoElement = formatEnvolvidoElement(envolvidoElement, envolvido)
            

    SaveXml(ET.ElementTree(lote), dataReporte)

def SaveXml(tree, fileName):
    path = f'..\\Lib\\Files\\{fileName}.xml'

    tree.write(path, encoding='iso-8859-1', xml_declaration=True)

def formatOcorrenciaElement(element, ocorrencia):
    ET.SubElement(element, "CPFCNPJCom").text = str(ocorrencia.CPFCNPJCom)
    ET.SubElement(element, "NumOcorrencia").text = str(ocorrencia.NumOcorrencia)
    ET.SubElement(element, "DtInicio").text = str(ocorrencia.DtInicio)
    ET.SubElement(element, "DtFim").text = str(ocorrencia.DtFim)
    ET.SubElement(element, "AgNum").text = str(ocorrencia.AgNum)
    ET.SubElement(element, "AgNome").text = str(ocorrencia.AgNome)
    ET.SubElement(element, "AgMun").text = str(ocorrencia.AgMun)
    ET.SubElement(element, "AgUF").text = str(ocorrencia.AgUF)
    ET.SubElement(element, "VlCred").text = str(ocorrencia.VlCred)
    ET.SubElement(element, "VlDeb").text = str(ocorrencia.VlDeb)
    ET.SubElement(element, "VlProv").text = str(ocorrencia.VlProv)
    ET.SubElement(element, "VlProp").text = str(ocorrencia.VlProp)
    ET.SubElement(element, "Det").text = str(ocorrencia.Det)

    return element

def formatEnquadramentoElement(element, enquadramento):
    ET.SubElement(element, "CodEnq").text = str(enquadramento.CodEnq)
            
    return element

def formatEnvolvidoElement(element, envolvido):
    ET.SubElement(element, "CPFCNPJEnv").text = str(envolvido.CPFCNPJEnv)
    ET.SubElement(element, "NmEnv").text = str(envolvido.NmEnv)
    ET.SubElement(element, "TpEnv").text = str(envolvido.TpEnv)
    ET.SubElement(element, "AgNumEnv").text = str(envolvido.AgNumEnv)
    ET.SubElement(element, "AgNomeEnv").text = str(envolvido.AgNomeEnv)
    ET.SubElement(element, "NumConta").text = str(envolvido.NumConta)
    ET.SubElement(element, "DtAbConta").text = str(envolvido.DtAbConta)
    ET.SubElement(element, "DtAtuaCad").text = str(envolvido.DtAtuaCad)
    ET.SubElement(element, "PObrigada").text = str(envolvido.PObrigada)
    ET.SubElement(element, "PEP").text = str(envolvido.PEP)
    ET.SubElement(element, "ServPub").text = str(envolvido.ServPub)

    return element