import tkinter as tk

import tkinter as tk

class SearchFrame(tk.Frame):

    FONTE_LABEL = ("Segoe UI", 12)
    FONTE_ENTRADA = ("Segoe UI", 14)
    FONTE_BOTAO = ("Segoe UI", 12, "bold")

    def __init__(self, master, controller):
        super().__init__(master, padx=20, pady=20)  # espaçamento interno do frame
        self.controller = controller

        # Label explicativa
        self.prompt_label = tk.Label(self, text="Digite o nome do filme para buscar:", font=self.FONTE_LABEL)
        self.prompt_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        # Entrada para busca
        self.search_entry = tk.Entry(self, font=self.FONTE_ENTRADA)
        self.search_entry.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        self.search_entry.focus()
        self.search_entry.bind("<Return>", lambda event: self.buscar())  # Enter ativa a busca

        # Botão de busca estilizado
        self.search_button = tk.Button(self, text="Buscar", font=self.FONTE_BOTAO,
                                       bg="#0078D7", fg="white", activebackground="#005A9E",
                                       relief="raised", bd=2, command=self.buscar)
        self.search_button.grid(row=2, column=0, sticky="ew", ipady=8, pady=(0, 15))

        # Label para exibir resultados
        self.result_label = tk.Label(self, text="", font=self.FONTE_LABEL, fg="#333333", wraplength=400, justify="left")
        self.result_label.grid(row=3, column=0, sticky="w")

        # Configurar grid para a entrada e botão expandirem horizontalmente
        self.grid_columnconfigure(0, weight=1)

    def buscar(self):
        termo = self.search_entry.get().strip()
        if termo:
            resultado = self.controller.buscar_filme(termo)
            self.result_label.config(text=resultado)
        else:
            self.result_label.config(text="Por favor, digite um termo para busca.")
