import customtkinter
import random
import pyperclip

def RNombre (difficulte):  # Génère une suite de nombres aléatoire
    i = 0
    nombre = []
    while i <= difficulte:
        nombre.append(random.randint(1,9))
        i += 1
    tableau_str = [str(element) for element in nombre]
    return tableau_str

def Rmdp (difficulte):  # Remplace les nombres aléatoires par des charactères aléatoires
    characteres = ['a', '3', '/', ':', 'b', '-', '1', 'c', 'd', '4', 'e', 'f', '2', 'g', '!', 'h', 'i', 'j', '#', '9', 'k', 'l', 'm', 'n', '6', 'o', '+', 'p', 'q', 'r', '5', 's', '?', '@', 't', 'u', 'v', 'w', '7', 'x', 'y', '8', 'z']
    mdp_int = RNombre(difficulte)
    mdp_str = []
    for c in mdp_int:
        c = random.randint(0, 42)
        mdp_str.append(characteres[c])
    mdp = ''.join(mdp_str)
    return mdp

def copier (mdp):  # Copie le mot de passe généré
    pyperclip.copy(mdp)
    label_copy.configure(text="Copié ✅")

def on_click ():  # Génère le mot de passe en cliquant sur le bouton
    if difficulte.get():
        if int(difficulte.get()) > 800000:
            if checked() == 'on':
                mdp = ''.join(RNombre(800000))
            else:
                mdp = Rmdp(800000)
            label_mdp2.configure(text=mdp)
        else:
            if checked() == 'on':
                mdp = ''.join(RNombre(int(difficulte.get()) - 1))
            else:
                mdp = Rmdp(int(difficulte.get()) - 1)
            label_mdp2.configure(text=str(mdp))
        button_copy = customtkinter.CTkButton(window, text="Copier", width=40, command=lambda: copier(mdp))
        button_copy.place(x=175, y=300)

def checked ():
    return check_box.get()

# Paramètres de la fenêtre
window = customtkinter.CTk()
window.title("Mot de passe aléatoire")
window.geometry("400x350")
window.resizable(False, False)

label = customtkinter.CTkLabel(window, text="Entrez la difficulté: ", font=("", 20))
label.place(x=10, y=50)

label2 = customtkinter.CTkLabel(window, text="(max 800 000)", font=("", 12))
label2.place(x=190, y=50)

# Permet d'entrer la difficulté du mot de passe
difficulte = customtkinter.CTkEntry(window, width=60, height=30)
difficulte.place(x=290, y=50)

check_box = customtkinter.CTkCheckBox(window, text="Chiffres seulement", command=checked, onvalue="on", offvalue="off")
check_box.place(x=50, y= 100)

# Bouton générer
button = customtkinter.CTkButton(window, text="Générer", font=("", 20), command=on_click)
button.place(x=130, y=150)

label_mdp1 = customtkinter.CTkLabel(window, text='Mot de passe: ', font=("", 20))
label_mdp1.place(x=10, y=250)

label_mdp2 = customtkinter.CTkLabel(window, text='', font=("", 15))
label_mdp2.place(x=145, y=250)

label_copy = customtkinter.CTkLabel(window, text='', font=("", 12))
label_copy.place(x=250, y=300)

# Affiche la fenêtre
window.mainloop()