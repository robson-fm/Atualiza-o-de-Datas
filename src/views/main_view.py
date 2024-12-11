import customtkinter as ctk


class MainView:
    def __init__(self, controller):
        # O controlador é passado como parâmetro e atribuído a self.controller
        if controller is None:
            raise ValueError("O controlador não pode ser None")

        # Para verificar
        print("Controlador recebido:", controller)
        self.controller = controller

        # Configuração da interface
        self.app = ctk.CTk()
        self.app.title("Atualizar data Ateste")
        self.app.geometry("400x350")

        # Configuração de estilo global do CustomTkinter
        ctk.set_appearance_mode("dark")  # Modo escuro para garantir contraste
        ctk.set_default_color_theme("dark-blue")  # Tema padrão

        # Componentes da interface
        self.label_relatorio_caixa = ctk.CTkLabel(self.app, text="Selecionar"
                                                  + "arquivo Relatório Caixa:")
        self.label_relatorio_caixa.pack(pady=(20, 5))
        self.entry_relatorio_caixa = ctk.CTkEntry(self.app, width=200)
        self.entry_relatorio_caixa.pack(pady=5)
        self.botao_relatorio_caixa = ctk.CTkButton(
            self.app,
            text="Selecionar",
            command=lambda: self.controller.selecionar_arquivo(
                self.entry_relatorio_caixa))
        self.botao_relatorio_caixa.pack(pady=5)

        self.label_ateste = ctk.CTkLabel(self.app, text="Selecionar arquivo"
                                         + "Ateste:")
        self.label_ateste.pack(pady=(20, 5))
        self.entry_ateste = ctk.CTkEntry(self.app, width=200)
        self.entry_ateste.pack(pady=5)
        self.botao_ateste = ctk.CTkButton(
            self.app,
            text="Selecionar",
            command=lambda: self.controller.selecionar_arquivo(
                self.entry_ateste))
        self.botao_ateste.pack(pady=5)

        self.botao_atualizar = ctk.CTkButton(
            self.app,
            text="Atualizar",
            command=self.controller.executar_atualizacao)
        self.botao_atualizar.pack(pady=20)

        # Configura as cores após todos os componentes serem criados
        self.configurar_estilo_personalizado()

    def configurar_estilo_personalizado(self):
        self.app.configure(fg_color="#3E3E42")  # Cor de fundo principal
        # Cor do texto
        self.label_relatorio_caixa.configure(text_color="white")
        self.label_ateste.configure(text_color="white")  # Cor do texto

    def run(self):
        self.app.mainloop()
