# animali_download.py — STUDENTE 2 — branch: feature/download
import os
import requests


def scarica_immagine(url, percorso):
    """
    Scarica un'immagine da un URL e la salva nel percorso indicato.
    Ritorna True se il salvataggio è riuscito, False altrimenti.
    IMPORTANTE: usa "wb" (write binary) non "w"!
    """
    try:
        risposta = None
        risposta=requests.get(url, timeout=15)

        if risposta.status_code == 200:
            # TODO 2: apri il file con open(percorso, "wb") come f
            #         e scrivi risposta.content dentro f
            with open(percorso, "wb") as f:
                f.write(risposta.content)

            # TODO 3: calcola la dimensione in KB
                dimensione_kb = 0
                dimensione_kb = len(risposta.content) / 1024
                print(f"  Salvato: {percorso} ({dimensione_kb:.1f} KB)")
            return True

        else:
            print(f"  Errore HTTP {risposta.status_code}: {url}")
            return False

    except requests.exceptions.ConnectionError:
        print(f"  Errore connessione: {url}")
        return False


def scarica_tutte(url_list, cartella, prefisso):
    """
    Scarica tutte le immagini in url_list nella cartella indicata.
    I file vengono nominati: prefisso_1.ext, prefisso_2.ext, ...
    Ritorna il numero di immagini salvate con successo.
    """
    salvate = 0

    # TODO 4: ciclo for con enumerate(url_list)
    # enumerate inizia da 1: enumerate(url_list, start=1)
    for numero, url in enumerate(url_list, start=1):

        # TODO 5: estrai l'estensione dall'URL
        estensione = ""
        estensione = url.split(".")[-1]

        # TODO 6: costruisci il nome del file
        nome_file = ""
        nome_file = prefisso + "_" + str(numero) + "." + estensione

        # TODO 7: costruisci il percorso completo con os.path.join
        percorso = ""
        percorso = os.path.join(cartella, nome_file)
        # TODO 8: chiama scarica_immagine(url, percorso)
        # se ritorna True: incrementa salvate
        successo = False
        if scarica_immagine(url, percorso):
            successo = True
        if successo:
            salvate = salvate + 1

    print(f"  {salvate}/{len(url_list)} immagini salvate")
    return salvate


if __name__ == "__main__":
    os.makedirs("test_download", exist_ok=True)
    url_test = ["https://http.cat/200", "https://http.cat/404"]
    scarica_tutte(url_test, "test_download", "gatto_http")