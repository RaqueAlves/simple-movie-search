from view.login_frame import LoginFrame
from view.search_frame import SearchFrame
import tkinter as tk
from tkinter import messagebox

class AppView:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.controller = controller

        self.root.geometry("300x400")

        self.login_frame = LoginFrame(self.root, controller)
        self.search_frame = SearchFrame(self.root, controller)

        self.login_frame.pack(fill="both", expand=True)

    def trocar_para_pesquisa(self):
        self.login_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)

    def start(self):
        self.root.mainloop()    
    
    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
