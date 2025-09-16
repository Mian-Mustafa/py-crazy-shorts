import tkinter as tk
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits
    password = "".join(random.choices(characters, k=8))
    label.config(text=password)
    
    
#Main Window
root = tk.Tk()
root.title("password generatoe 🔑")
#label to show password
label = tk.Label(root,font=("Arial",20))
label.pack(pady=10)

#buttom to generate password
btn = tk.Button(root,text="generate",command=generate_password)
btn.pack(pady=5)

#Run app
root.mainloop()