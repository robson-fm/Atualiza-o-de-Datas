import os
import customtkinter as ctk
from models.data_model import carregar_planilhas, atualizar_planilha_referencia
from tkinter import filedialog, messagebox
from datetime import datetime
from requests import post
from os import getlogin


class TestAutomacao:
    def __init__(self):
        self.data_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def enviardados(self, erro):
        dados = {
            "Automação": "Atualizar data Ateste",
            "Data Fim": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Data Inicio": self.data_inicio,
            "Erro": erro,
            "Modulo": "Atualizar Ateste",
            "valores": getlogin(),
            "Versao": "V0"
        }
        response = post("https://automacoesppi-default-rtdb.firebaseio.com/Execucoes.json", json=dados)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")


class AppController:
    def __init__(self, view):
        self.view = view
        print("Controlador recebido:", self.view)
        if self.view:
            raise ValueError("A visualização não pode ser None")

    def selecionar_arquivo(self, entry):
        filepath = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")])
        if filepath:
            entry.delete(0, ctk.END)
            entry.insert(0, filepath)

    def executar_atualizacao(self):
        test_automacao = TestAutomacao()  # Inicialize o rastreamento de automação
        arquivo_principal = self.view.entry_relatorio_caixa.get()
        arquivo_referencia = self.view.entry_ateste.get()

        if not os.path.isfile(arquivo_principal) or not os.path.isfile(arquivo_referencia):
            ctk.messagebox.showerror("Erro", "Por favor, selecione ambos os arquivos corretamente.")
            test_automacao.enviardados("Arquivos inválidos")
            return

        try:
            df_principal, df_referencia = carregar_planilhas(
                arquivo_principal, arquivo_referencia)
            atualizar_planilha_referencia(df_principal, df_referencia, arquivo_referencia)
            messagebox.showinfo("Sucesso", "Atualização concluída com sucesso!")
            test_automacao.enviardados("")  # Envia sem erro
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
            test_automacao.enviardados(str(e))  # Registra o erro
        print("Executando a atualização...")
