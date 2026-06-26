import os

def ordina_alfabeticamente(lista_file):
    """
    Prende una lista di stringhe e la restituisce
    ordinata alfabeticamente
    :param lista_file:
    :return: lista_ordinata
    """
    lista_ordinata = sorted(lista_file)
    return lista_ordinata

def stampa_galleria (lista_file_ordinati,cartella):
    """
    scorre la lista dei file ordinati e stampa il riepilogo grafico testuale.
    Mostra il nome del file,percorso completo e la sua dimensione in KB
    :param lista_file_ordinati:
    :param cartella:
    :return: nessuno, stampa solo la galleria
    """
    print("\n"+"="*40)
    print("🐾 GALLERIA ANIMALI ORDINATA 🐾")
    print("=" * 40 + "\n")

    if not lista_file_ordinati:
        print("La galleria è vuota. Nessuna immagine trovata")
        return

    for file in lista_file_ordinati:
        percorso_completo = os.path.join(cartella,file)

        try:
            # Ottiene la dimensioni del file in byte e converte in kb
            dimensione_bytes = os.path.getsize(percorso_completo)
            dimensione_kb = dimensione_bytes / 1024

            # stampa la dimensione dei file formattati
            print(f"📄 File: {file}")
            print(f"   📍 Percorso: {percorso_completo}")
            print(f"   ⚖️  Dimensione: {dimensione_kb:.2f} KB")
            print("-" * 30)


        except OSError:
            print(f"⚠️ Impossibile leggere il file: {file}")

    print(f"Totale elementi in galleria: {len(lista_file_ordinati)}")
    print("="*40 + "\n")


if __name__ == "__main__":
    print("Esecuzione test locale per animali_galleria.py...\n")

    # 1. Creiamo dei file reali sul tuo PC solo per fare il test
    file_reali = ["gatto_2.png", "cane_1.jpg", "gatto_1.png", "cane_2.jpg"]

    print("--- CREAZIONE FILE DI TEST ---")
    for nome_file in file_reali:
        # Crea un file vuoto nella cartella corrente
        with open(nome_file, "w") as f:
            f.write("Finto contenuto immagine")
        print(f"Creato file reale: {nome_file}")

    print("\n--- TEST ORDINAMENTO ---")
    file_ordinati = ordina_alfabeticamente(file_reali)
    print("Lista ordinata: ", file_ordinati)

    print("\n--- TEST STAMPA GALLERIA ---")
    # Usiamo "." come cartella, che significa "la cartella corrente dove si trova il file"
    stampa_galleria(file_ordinati, ".")

    # 2. Pulizia: eliminiamo i finti file per non sporcare il progetto
    for nome_file in file_reali:
        if os.path.exists(nome_file):
            os.remove(nome_file)
