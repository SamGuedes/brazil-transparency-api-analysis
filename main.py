import pandas as pd
from extractLicitacoes import fetchLicitacoes
from extractCodOrgaosSiafi import fetchCodOrgaosSiafi
from dotenv import load_dotenv
import os 


load_dotenv(".env")
apiKey = os.getenv("apiKey")


baseUrl = "https://api.portaldatransparencia.gov.br/api-de-dados/"

endpoints = {
    "licitacoes": "licitacoes",
    "codOrgaos": "orgaos-siafi"
}


df = pd.DataFrame(fetchCodOrgaosSiafi(baseUrl, endpoints["codOrgaos"], apiKey))

df