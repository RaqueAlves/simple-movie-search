import tkinter as tk

class LoginFrame(tk.Frame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        tk.Label(self, text="User: ").pack(pady=5)
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        tk.Label(self, text="Password: ").pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        tk.Button(self, text="Register", command=self.register).pack(pady=10)

    def login(self):
        usuario = self.entry_user.get()
        senha = self.entry_password.get()
        self.controller.verificar_login(usuario, senha)
    
    def register(self):
        usuario = self.entry_user.get()
        senha = self.entry_password.get()
        self.controller.cadastrar_user(usuario, senha)