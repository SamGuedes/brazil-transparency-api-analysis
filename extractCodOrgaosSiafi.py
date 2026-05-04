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


            if not data:
                break


            print(f"{response.status_code} | Registros na página: {len(data)} | Registros Acumulados: {len(fetchedCod)}")            
            
            fetchedCod.extend(data)

            page += 1 

        else:
            response.raise_for_status()

    return fetchedCod

        

       






