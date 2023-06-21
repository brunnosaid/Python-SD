import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import os
import shutil
import ctypes
from unidecode import unidecode


def find(nome_arquivo, diretorio_atual):
    try:
        # Verifica se o diretório atual corresponde ao nome do arquivo
        if unidecode(os.path.basename(diretorio_atual).lower()) == unidecode(nome_arquivo.lower()):
            messagebox.showinfo("Diretório Encontrado!", f"Local Encontrado: {diretorio_atual}")
            return True

        # Processamento de Busca
        for item in os.listdir(diretorio_atual):
            full_path = os.path.join(diretorio_atual, item)

            # Ignora pastas que começam com um ponto
            if os.path.isdir(full_path) and not item.startswith("."):
                processamento.insert(tk.END, f"Verificando: {full_path}\n")
                processamento.see(tk.END)
                processamento.update()

                if find(nome_arquivo, full_path):
                    return True

        # Caso não encontre nada
        return False

    except PermissionError:
        # Lidar com o erro de permissão negada
        processamento.insert(tk.END, "Erro de permissão negada ao acessar a pasta.\n")
        processamento.see(tk.END)
        processamento.update()
        return False


def name_file():
    nome_arquivo = entrada.get()
    if nome_arquivo:
        diretorio_atual = os.path.expanduser("~")
        encontrado = find(nome_arquivo, diretorio_atual)
        if encontrado:
            resposta = messagebox.askyesno("Excluir Arquivo/Diretório", "Deseja excluir o arquivo/diretório encontrado?")
            if resposta:
                try:
                    # Verifica se o programa está sendo executado como administrador
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        shutil.rmtree(diretorio_atual)
                        messagebox.showinfo("Exclusão Concluída", "Arquivo/Diretório excluído com sucesso.")
                    else:
                        # Se não estiver sendo executado como administrador, solicita privilégios elevados
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                except PermissionError:
                    messagebox.showwarning("Erro de Permissão", "Erro de permissão negada ao excluir o arquivo/diretório.")
        else:
            messagebox.showinfo("Arquivo não encontrado", "O arquivo não foi encontrado.")


# Inicio do programa
root = ThemedTk(theme="breeze")

style = ttk.Style()
style.theme_use()

largura = 900
altura = 600

# Config do programa
root.geometry(f"{largura}x{altura}")
root.title("Search and Destroy")

# -----------------------------------------------------------------------------------
# Config para Caixa do Texto
entrada = tk.Entry(root, width=300, font=("Arial", 20))
entrada.pack(padx=10, pady=15)

# Config para Botão de Pesquisa
botao_find = tk.Button(root, text="Buscar", command=name_file)
botao_find.pack()

# -----------------------------------------------------------------------------------
# Config para Tela de Logs
frame_log = tk.Frame(root)
frame_log.pack(fill=tk.BOTH, expand=True)

processamento = tk.Text(frame_log)
processamento.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_log)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

processamento.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=processamento.yview)

# Config para o usuario não alterar o tamanho do programa
root.resizable(False, False)
root.mainloop()
