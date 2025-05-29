import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x300")

        tk.Label(self.root, text="User: ").pack(pady=5)
        self.entry_user = tk.Entry(self.root)
        self.entry_user.pack()

        tk.Label(self.root, text="Password: ").pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Register", command=self.register).pack(pady=10)

    def start(self):
        self.root.mainloop()

    def login(self):
        usuario = self.entry_user.get()
        senha = self.entry_password.get()
        self.controller.verificar_login(usuario, senha)
    
    def register(self):
        usuario = self.entry_user.get()
        senha = self.entry_password.get()
        self.controller.cadastrar_user(usuario, senha)

    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)