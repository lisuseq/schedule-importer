import tkinter as tk
import os
from tkinter import filedialog

def wybierz_plik():
    sciezka_pliku = filedialog.askopenfilename()
    if sciezka_pliku:
        label_path.config(text=os.path.basename(sciezka_pliku))

# Paleta kolorów
background_color = "#C097F6"
primary_color = "#4F248C"
secondary_color = "#AB85DE"

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Importer planu")
okno.geometry("300x125")
okno.config(bg=background_color)


# --- Pierwszy wiersz ---
label = tk.Label(okno, text="Imię:")
label.grid(row=0, column=0, sticky="w", padx=20, pady=15)
label.config(bg=background_color, fg=primary_color)

pole_tekstowe = tk.Entry(okno, width=25)
pole_tekstowe.grid(row=0, column=1, sticky="w", padx=0, pady=15)
pole_tekstowe.config(bg=secondary_color, fg=primary_color)

# --- Drugi wiersz ---
przycisk = tk.Button(okno, text="Wybierz plik", command=wybierz_plik)
przycisk.grid(row=1, column=0, sticky="w", padx=20, pady=5)
przycisk.config(bg=secondary_color, fg=primary_color)

label_path = tk.Label(okno, text="Nazwa:")
label_path.grid(row=1, column=1, sticky="w", padx=0, pady=5)
label_path.config(bg=background_color, fg=primary_color)

# Uruchomienie aplikacji
okno.mainloop()