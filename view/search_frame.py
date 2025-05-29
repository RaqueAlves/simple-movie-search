import tkinter as tk

class SearchFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()
        tk.Button(self, text="Buscar", command=self.buscar).pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def buscar(self):
        termo = self.search_entry.get()
        resultado = self.controller.buscar_filme(termo)
        self.result_label.config(text=resultado)
