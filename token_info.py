import requests
#permet d'appeler la bibliotheque requests

API_KEY = "xxx"  # Remplacer par votre propre clé API Etherscan
#N'oubliez pas de mettre votre vraie clé API ici (ne jamais publier la vraie en ligne)


def get_token_info(contract_address):
    url = "https://api.etherscan.io/api"

    params = {
            "module": "token", #on utilise la partie token de l'API
            "action": "tokeninfo", #on demande des infos de base sur un token
            "contractaddress": contract_address, #on envoie l'adresse du token tapé
            "apikey": API_KEY, #on envoie la clé API pour s'identifier
    }
    
    response = requests.get(url, params=params) #envoi une requete HTTP GET vers l'URL de l'API Etherscan

    data = response.json()

    if data["status"] == "1": #si 1 = ok si 0 = probleme adresse ou API ou token n'existe pas
        token = data["result"][0] #stockage donnée token
        print(f"Nom du token: {token['tokenName']}")
        print(f"symbol: {token['symbol']}")
        print(f"Décimales: {token['decimals']}")
        print(f"Total Supply : {int(token['totalSupply']) / 10**int(token['decimals'])} {token['symbol']}")
    else:
        print("Erreur:", data["message"])

def analyser_contrat(contract_address):
    url = "https://api.etherscan.io/api"

    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "1":
        contrat = data["result"][0]
        print(f"Contrat vérifié: {'oui' if contrat['SourceCode'] else 'non'}")
        if "ContractCreator" in contrat:
            print(f"Créateur (propriétaire) : {contrat['ContractCreator']}")
        else:
            print("Créateur non disponible")
        print(f"Date de création: {contrat['Creationdate'] if 'Creationdate' in contrat else 'Non Disponible'}")
    else:
        print(f"Erreur lors de l'analyse du contrat :", data["message"])

if __name__ == "__main__":
    contract_address = input("entrez l'adresse du contrat ERC-20: ")
    get_token_info(contract_address)
    analyser_contrat(contract_address)


    