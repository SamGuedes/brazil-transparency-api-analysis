import requests
from urllib.parse import urljoin

def fetchCodOrgaosSiafi(baseUrl: str, endpoint: str, apiKey: str):
    urlCodOrgaos =  urljoin(baseUrl, endpoint)
    fetchedCod = []
    page = 1

    headers = {
        "chave-api-dados": apiKey,
        "accept": "application/json"
    }

    while True:

        params = {
            "pagina": page
        }

        response = requests.get(url=urlCodOrgaos, headers=headers, params=params)



        if response.status_code ==  200:
            data = response.json()
            print(f"{response.status_code} | {response.text} | Registros na página: {len(data)} | Registros Acumulados: {len(fetchedCod)}")
            

            if not response.content and not fetchedCod:
                print("Sem dados")

                break

            if not response.content: 
                print("Sem mais dados")

            
            fetchedCod.extend(data)

            page += 1 

        else:
            response.raise_for_status()

        

       






