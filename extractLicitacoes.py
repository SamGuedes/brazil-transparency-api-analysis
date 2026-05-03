from urllib.parse import urljoin
import requests

def fetchLicitacoes(baseUrl: str, endpoint: str, apiKey: str):

    urlLicitacoes = urljoin(baseUrl, endpoint) 
    page = 1
    
    fetchedData = []

    headers = {
        "chave-api-dados": f"{apiKey}",
        "accept": "application/json"
    }

    while True:
        
        params = {
            "pagina": page,
            "dataInicial": "01-01-2026",
            "dataFinal": "01-02-2026",
            "codigoOrgao": 1 
        }

        response = requests.get(url=urlLicitacoes, headers=headers, params=params)

        data = response.json()

        if response.status_code == 200:
            print(f"{response.status_code} | {response.text} | Resultados: {len(data)} | Total Acumulado: {len(fetchedData)}")    

            if not response.content:
                print("Sem Dados")
                break

            fetchedData.extend(data)

        else:
            print(response.status_code, response.content)
            break

        page += 1

    return fetchedData







    
    
