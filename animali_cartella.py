# animali_cartella.py — STUDENTE 3 — branch: feature/cartella
import os


def crea_cartella(percorso):
    """
    Crea la cartella nel percorso indicato.
    Se esiste già, non dà errore (exist_ok=True).
    Stampa un messaggio per informare l'utente.
    """

    # TODO 1: controlla se la cartella esiste già
    esisteva_gia = os.path.isdir(percorso)

    # TODO 2: crea la cartella con os.makedirs
    os.makedirs(percorso, exist_ok = True)

    # TODO 3: stampa il messaggio appropriato
    if esisteva_gia:
        print(f"La cartella '{percorso}' esiste già")
    else:
        print(f"La cartella '{percorso}' è stata creata")


def elenca_immagini(cartella):
    """
    Ritorna la lista dei file immagine (.jpg, .jpeg, .png)
    presenti nella cartella indicata.
    """

    # TODO 4: leggi tutti i file con os.listdir(cartella)
    tutti_i_file = os.listdir(cartella)

    # TODO 5: filtra solo i file immagine
    immagini = []

    for nome_file in tutti_i_file:

        # TODO 6: controlla se termina con .jpg, .jpeg o .png
        estensioni = (".jpg", ".jpeg", ".png")
        immagini = [
            nome_file
            for nome_file in tutti_i_file
            if nome_file.lower().endswith(estensioni)
        ]

    print(f"Trovate {len(immagini)} immagini in {cartella}")
    return immagini


if __name__ == "__main__":
    crea_cartella("test_cartella")
    crea_cartella("test_cartella")    # seconda volta: non dà errore

    # Crea un file di test per provare elenca_immagini
    with open("test_cartella/foto.jpg", "wb") as f:
        f.write(b"")    # file vuoto di test
    with open("test_cartella/nota.txt", "w") as f:
        f.write("questo non è un'immagine")

    immagini = elenca_immagini("test_cartella")
    print("Immagini trovate:", immagini)
    # Deve stampare solo ['foto.jpg'], non nota.txt