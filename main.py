import customtkinter
import random
import pyperclip
import json

settings = {}

def set_settings ():
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

def load_settings ():
    global settings
    with open('settings.json', 'r') as f:
        settings = json.load(f)

# Génère une suite de nombres aléatoire
def RNombre (difficulte):
    i = 0
    nombre = []
    while i <= difficulte:
        nombre.append(random.randint(1,9))
        i += 1
    tableau_str = [str(element) for element in nombre]
    return tableau_str

# Remplace les nombres aléatoires par des charactères aléatoires
def Rmdp (difficulte):
    characteres = ['a', '3', '/', ':', 'b', '-', '1', 'c', 'd', '4', 'e', 'f', '2', 'g', '!', 'h', 'i', 'j', '#', '9', 'k', 'l', 'm', 'n', '6', 'o', '+', 'p', 'q', 'r', '5', 's', '?', '@', 't', 'u', 'v', 'w', '7', 'x', 'y', '8', 'z']
    mdp_int = RNombre(difficulte)
    mdp_str = []
    for c in mdp_int:
        c = random.randint(0, 42)
        mdp_str.append(characteres[c])
    mdp = ''.join(mdp_str)
    return mdp

# Copie le mot de passe généré
def copier (mdp):
    pyperclip.copy(mdp)
    if settings['language'] == "fr":
        label_copy.configure(text="Copié ✅")
    elif settings['language'] == "en":
        label_copy.configure(text="Copied ✅")

# Génère le mot de passe en cliquant sur le bouton
def on_click ():
    global mdp
    if difficulte.get():
        if int(difficulte.get()) > 800000:
            if checked() == 'on':
                mdp = ''.join(RNombre(800000))
            else:
                mdp = Rmdp(800000)
                label_mdp2.configure(text=mdp)
            label_mdp2.configure(text='*' * 800000)
        else:
            if checked() == 'on':
                mdp = ''.join(RNombre(int(difficulte.get()) - 1))
            else:
                mdp = Rmdp(int(difficulte.get()) - 1)
            label_mdp2.configure(text='*' * int(difficulte.get()))
        set_language()
        button.configure(width=40)
        label_copy.configure(text='')
        button_copy.place(x=175, y=300)
        show_mdp()

# Défini si oui ou non l'utilisateur veut voir le mot de passe
def show_mdp ():
    try:
        if label_show.get() == "on":
            label_mdp2.configure(text=mdp)
        else:
            label_mdp2.configure(text='*' * len(mdp))
    except:
        return

def checked ():
    return check_box.get()

def openParameters ():
    parameters_window.deiconify()

def closeParameters ():
    parameters_window.withdraw()

def button_set_theme ():
    global theme
    if theme_input.get() == "Clair" or theme_input.get() == "light":
        theme = "light"
    elif theme_input.get() == "Sombre" or theme_input.get() == "Dark":
        theme = "dark"
    elif theme_input.get() == "Système (par défaut)" or theme_input.get() == "System (default)":
        theme = "system"
    set_theme()

def set_theme ():
    if 'theme' in globals():
        settings['theme'] = theme
    customtkinter.set_appearance_mode(settings['theme'])
    window.deiconify()
    set_settings()

def button_set_language ():
    global language
    if language_input.get() == "English":
        language = "en"
    elif language_input.get() == "Français":
        language =  "fr"
    set_language()

def set_language ():
    if 'language' in globals():
        settings['language'] = language

    if settings['language'] == "fr":
        label.configure(text="Entrez la difficulté: ")
        label2.configure(text="(max 800 000)")
        check_box.configure(text="Chiffres seulement")
        button.configure(text="Générer")
        label_mdp1.configure(text='Mot de passe: ')
        label_show.configure(text='Voir mot de passe')
        label_language.configure(text="Choisir la langue :")
        confirmLanguage_bouton.configure(text="Confirmer")
        label_theme.configure(text="Choisir le thème :")
        theme_input.configure(values=["Clair", "Sombre", "Système (par défaut)"])
        confirmTheme_bouton.configure(text="Confirmer")
        button_copy.configure(text="Copier")
        window.title("Générateur")
        parameters_window.title("Paramètres")

    elif settings['language'] == "en":
        label.configure(text="Enter the difficulty: ")
        label2.configure(text="(800 000 max)")
        check_box.configure(text="Number only")
        button.configure(text="Generate")
        label_mdp1.configure(text='Password: ')
        label_show.configure(text='Show password')
        label_language.configure(text="Choose language :")
        confirmLanguage_bouton.configure(text="Confirm")
        label_theme.configure(text="Choose theme :")
        theme_input.configure(values=["Light", "Dark", "System (default)"])
        confirmTheme_bouton.configure(text="Confirm")
        button_copy.configure(text="Copy")
        window.title("Generator")
        parameters_window.title("Settings")
    set_settings()

# Paramètres de la fenêtre
window = customtkinter.CTk()
window.title("Générateur")
window.geometry("400x350")
window.resizable(False, False)

parameters_window = customtkinter.CTk()
parameters_window.title("Paramètres")
parameters_window.geometry("400x350")
parameters_window.resizable(False, False)

button_copy = customtkinter.CTkButton(window, text="", width=0, command=lambda: copier(mdp))

open_parameters = customtkinter.CTkButton(window, text="⚙", font=("", 15), width=10, command=openParameters)
open_parameters.place(x=5, y=5)

close_parameters = customtkinter.CTkButton(parameters_window, text="❌", font=("", 15), width=10, command=closeParameters)
close_parameters.place(x=5, y=5)

label = customtkinter.CTkLabel(window, text="Entrez la difficulté: ", font=("", 20))
label.place(x=10, y=50)

label2 = customtkinter.CTkLabel(window, text="(max 800 000)", font=("", 12))
label2.place(x=190, y=50)

# Permet d'entrer la difficulté du mot de passe
difficulte = customtkinter.CTkEntry(window, width=60, height=30)
difficulte.place(x=290, y=50)

# Permet de choisir chiffres seulement ou non
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

# Permet oui ou non l'affichage du mot de passe
label_show = customtkinter.CTkCheckBox(window, text='Voir mot de passe', font=("", 10), command=show_mdp, onvalue="on", offvalue="off")
label_show.place(x=30, y=300)

label_language = customtkinter.CTkLabel(parameters_window, text="Choisir la langue :", font=("", 15))
label_language.place(x=20, y=50)

language_input = customtkinter.CTkOptionMenu(parameters_window, values=["Français", "English"])
language_input.place(x=170, y=50)

confirmLanguage_bouton = customtkinter.CTkButton(parameters_window, text="Confirmer", font=("", 15), width=130, height=32, command=button_set_language)
confirmLanguage_bouton.place(x=130, y=100)

label_theme = customtkinter.CTkLabel(parameters_window, text="Choisir le thème :", font=("", 15))
label_theme.place(x=20, y=200)

theme_input = customtkinter.CTkOptionMenu(parameters_window, values=["Clair", "Sombre", "Système (par défaut)"])
theme_input.place(x=170, y=200)

confirmTheme_bouton = customtkinter.CTkButton(parameters_window, text="Confirmer", font=("", 15), width=130, height=32, command=button_set_theme)
confirmTheme_bouton.place(x=130, y=250)

load_settings()
set_language()
set_theme()

# Affiche la fenêtre
window.mainloop()