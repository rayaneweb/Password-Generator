from tkinter import *
from logic import generate_password, check_strength
import os
import sys



def generate():
    password = generate_password()
    fade_in_text(password_entry, password)
    strength, color = check_strength(password)
    strength_label.config(text=f"Sécurité : {strength}", fg=color)

def on_key_release(event):
    password = password_entry.get()
    if password:
        strength, color = check_strength(password)
        strength_label.config(text=f"Sécurité : {strength}", fg=color)
    else:
        strength_label.config(text="Sécurité : ---", fg="white")

def fade_in_text(entry_widget, text, index=0, delay=50):
    if index == 0:
        entry_widget.delete(0, END)
    if index < len(text):
        entry_widget.insert(index, text[index])
        entry_widget.after(delay, lambda: fade_in_text(entry_widget, text, index+1, delay))


# Fenêtre principale


window = Tk()
window.title("Password Generator")
window.geometry("720x480")
window.config(background="#7D0808")


# Gestion des assets (PyInstaller)


if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Chemins vers l'icône et l'image
icon_path = os.path.join(base_path, "assets", "p.ico")
image_path = os.path.join(base_path, "assets", "p.png")

window.iconbitmap(icon_path)
image = PhotoImage(file=image_path).zoom(15).subsample(30)


# Frame principale


frame = Frame(window, bg="#7D0808", bd=0)

# Canvas avec image
width = 300
height = 300
canvas = Canvas(frame, width=width, height=height, bg="#7D0808", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()

# Titre
title = Label(frame, text="Password Generator", font=("Arial", 24), bg="#7D0808", fg="white")
title.pack()

# Entry mot de passe
password_entry = Entry(frame, font=("Arial", 14), width=30, fg="#7D0808", bd=2, relief="solid")
password_entry.bind("<KeyRelease>", on_key_release)
password_entry.pack(fill=X)

# Label sécurité
strength_label = Label(frame, text="Sécurité : ---", font=("Arial", 14), bg="#7D0808", fg="white")
strength_label.pack(pady=5)

# Bouton Generate
gen_button = Button(frame, text="Generate", font=("Arial", 14), bg="#FFFFFF", fg="#7D0808", bd=2, relief="solid", command=generate)
gen_button.pack(pady=10)



frame.pack(expand=YES)
window.mainloop()
