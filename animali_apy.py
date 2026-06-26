# animali_api.py — STUDENTE 1 — branch: feature/api
import requests

URL_CANI  = "https://api.thedogapi.com/v1/images/search"
URL_GATTI = "https://api.thecatapi.com/v1/images/search"


def scarica_url_da_api(url_api, quante):
    """
    Funzione generica: chiama l'API con il parametro limit=quante
    e ritorna la lista degli URL delle immagini.
    Ritorna una lista vuota in caso di errore.
    """
    parametri = {"limit": 10}

    try:
        risposta = requests.get(url_api, params=parametri, timeout=10)

        if risposta.status_code == 200:
            immagini = risposta.json()

            url_list = []
            # TODO 2: ciclo for su immagini
            # per ogni immagine: url_list.append(immagine["url"])
            for immagine in immagini:
                quante -= 1
                url_list.append(immagine["url"])
                if quante == 0:
                  break

            return url_list

        else:
            print(f"Errore API: {risposta.status_code}")
            return []

    except requests.exceptions.ConnectionError:
        print("Errore: nessuna connessione a Internet")
        return []


def scarica_url_cani(quante):
    """
    Scarica URL di immagini di cani.
    Ritorna una lista di URL.
    """
    # TODO 3: chiama scarica_url_da_api con URL_CANI e quante

    return scarica_url_da_api(URL_CANI, quante)


def scarica_url_gatti(quante):
    """
    Scarica URL di immagini di gatti.
    Ritorna una lista di URL.
    """
    # TODO 4: chiama scarica_url_da_api con URL_GATTI e quante
    return scarica_url_da_api(URL_GATTI, quante)


if __name__ == "__main__":
    cani  = scarica_url_cani(3)
    gatti = scarica_url_gatti(3)
    print("URL cani:")
    for url in cani:
        print(" ", url)
    print("URL gatti:")
    for url in gatti:
        print(" ", url)