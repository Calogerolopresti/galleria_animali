# main.py — scritto dal professore, non si modifica
from animali_apy      import scarica_url_cani, scarica_url_gatti
from animali_download import scarica_tutte
from animali_cartella import crea_cartella, elenca_immagini
from animali_galleria import ordina_alfabeticamente, stampa_galleria


CARTELLA  = "immagini_animali"
QUANTE    = 5        # quante immagini scaricare per ogni animale

if __name__ == "__main__":
    print("=== GALLERIA ANIMALI ===")
    print()

    # STEP 1 — Studente 3: crea la cartella sul disco
    crea_cartella(CARTELLA)

    # STEP 2 — Studente 1: scarica gli URL dalle API
    print("Recupero URL cani...")
    url_cani  = scarica_url_cani(QUANTE)
    print("Recupero URL gatti...")
    url_gatti = scarica_url_gatti(QUANTE)

    # STEP 3 — Studente 2: scarica le immagini sul disco
    print()
    print("Download immagini cani...")
    scarica_tutte(url_cani, CARTELLA, "cane")
    print("Download immagini gatti...")
    scarica_tutte(url_gatti, CARTELLA, "gatto")

    # STEP 4 — Studente 3: legge i file presenti nella cartella
    print()
    file_presenti = elenca_immagini(CARTELLA)

    # STEP 5 — Studente 4: ordina e stampa la galleria
    file_ordinati = ordina_alfabeticamente(file_presenti)
    stampa_galleria(file_ordinati, CARTELLA)