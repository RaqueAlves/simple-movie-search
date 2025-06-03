import tkinter as tk

class LoginFrame(tk.Frame):

    FONTE_LABEL = ("Segoe UI", 12)
    FONTE_ENTRY = ("Segoe UI", 14)
    FONTE_BOTAO = ("Segoe UI", 12, "bold")
    FONTE_WARN = ("Segoe UI", 10, "italic")

    COR_ERRO = "#ffcccc"  # cor de fundo vermelha clara para erro
    COR_NORMAL = "white"  # cor normal do Entry
    COR_TEXTO_ERRO = "#d32f2f"  # vermelho escuro para texto de erro
    COR_TEXTO_SUCESSO = "#388e3c"  # verde escuro para texto de sucesso

    def __init__(self, master, controller):
        super().__init__(master, padx=30, pady=30)
        self.controller = controller

        # Label e Entry usuário
        tk.Label(self, text="Usuário:", font=self.FONTE_LABEL).grid(row=0, column=0, sticky="w", pady=(0,5))
        self.entry_user = tk.Entry(self, font=self.FONTE_ENTRY, bg=self.COR_NORMAL)
        self.entry_user.grid(row=1, column=0, sticky="ew", pady=(0,15))
        self.entry_user.focus()

        # Label e Entry senha
        tk.Label(self, text="Senha:", font=self.FONTE_LABEL).grid(row=2, column=0, sticky="w", pady=(0,5))
        self.entry_password = tk.Entry(self, show="*", font=self.FONTE_ENTRY, bg=self.COR_NORMAL)
        self.entry_password.grid(row=3, column=0, sticky="ew", pady=(0,10))
        self.entry_password.bind("<Return>", lambda e: self.login())

        # Label para exibir avisos (mensagens de erro ou sucesso)
        self.warm_label = tk.Label(self, text="", font=self.FONTE_WARN,
                                   fg=self.COR_TEXTO_ERRO, wraplength=400, justify="left")
        self.warm_label.grid(row=4, column=0, sticky="w", pady=(0,15))

        # Botões estilizados
        self.login_button = tk.Button(self, text="Login", font=self.FONTE_BOTAO,
                                      bg="#28a745", fg="white", activebackground="#1e7e34",
                                      relief="raised", bd=2, command=self.login)
        self.login_button.grid(row=5, column=0, sticky="ew", ipady=8, pady=(0,10))

        self.register_button = tk.Button(self, text="Registrar", font=self.FONTE_BOTAO,
                                         bg="#007bff", fg="white", activebackground="#0056b3",
                                         relief="raised", bd=2, command=self.register)
        self.register_button.grid(row=6, column=0, sticky="ew", ipady=8)

        # Configurar expansão horizontal
        self.grid_columnconfigure(0, weight=1)

    def mostrar_erro(self, mensagem):
        self.warm_label.config(text=mensagem, fg=self.COR_TEXTO_ERRO)

    def mostrar_sucesso(self, mensagem):
        self.warm_label.config(text=mensagem, fg=self.COR_TEXTO_SUCESSO)

    def limpar_mensagem(self):
        self.warm_label.config(text="")

    def validar_campos(self):
        """Valida usuário e senha; destaca campos vazios e retorna se está tudo ok."""
        usuario = self.entry_user.get().strip()
        senha = self.entry_password.get().strip()

        valido = True

        # Resetar cores para padrão antes de validar
        self.entry_user.config(bg=self.COR_NORMAL)
        self.entry_password.config(bg=self.COR_NORMAL)
        self.limpar_mensagem()

        if not usuario:
            self.entry_user.config(bg=self.COR_ERRO)
            valido = False
        if not senha:
            self.entry_password.config(bg=self.COR_ERRO)
            valido = False

        return valido, usuario, senha

    def login(self):
        valido, usuario, senha = self.validar_campos()
        if not valido:
            self.mostrar_erro("Usuário e senha são obrigatórios.")
            return
        verificado = self.controller.verificar_login(usuario, senha)
        if verificado == True or verificado == "Login efetuado com sucesso.":
            self.mostrar_sucesso("Login efetuado com sucesso.")
        else:
            self.mostrar_erro(str(verificado))

    def register(self):
        valido, usuario, senha = self.validar_campos()
        if not valido:
            self.mostrar_erro("Usuário e senha são obrigatórios para registro.")
            return
        verificado = self.controller.cadastrar_user(usuario, senha)
        if verificado == True or verificado == "Cadastro realizado com sucesso.":
            self.mostrar_sucesso("Cadastro realizado com sucesso.")
        else:
            self.mostrar_erro(str(verificado))