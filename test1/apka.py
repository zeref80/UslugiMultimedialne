import tkinter as tk
import subprocess
import sys
from PIL import Image, ImageTk



def loguj():
    print("Akcja logowania")
    try:
        process = subprocess.run([sys.executable, 'main.py'], stdin=subprocess.PIPE, check=True)
     #   subprocess.run([sys.executable, 'main.py'], stdin=subprocess.PIPE, check=True)
        process.communicate()  # Czekanie na zakończenie procesu drugiego skryptu
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        process.terminate()  # Zabicie procesu pierwszego skryptu, niezależnie od wyniku drugiego skryptu



#Popen
    root.destroy()

def opcje():
    print("Akcja opcji")

def wyjdz():
    root.destroy()



# Tworzenie głównego okna
root = tk.Tk()
root.title("STAH App")
root.geometry("500x500")

# Dodawanie przycisków
button_loguj = tk.Button(root, text="Loguj", activebackground="#C1CDCD", command=loguj, width=40, height=5)
button_loguj.place(x=100, y=200)
#button_loguj.pack(pady=20)

button_opcje = tk.Button(root, text="Opcje", command=opcje, width=40, height=5)
button_opcje.place(x=100, y=300)

obraz = Image.open("StahApps4.jpg")
obraz_tk = ImageTk.PhotoImage(obraz)
label_obraz = tk.Label(root, image=obraz_tk)
label_obraz.place(x=37, y=20)

#button_opcje.pack(pady=20)

button_wyjdz = tk.Button(root, text="Wyjdź", command=wyjdz, width=40, height=5)
button_wyjdz.place(x=100, y=400)
#button_wyjdz.pack(pady=20)

# Uruchamianie głównej pętli programu
root.mainloop()
