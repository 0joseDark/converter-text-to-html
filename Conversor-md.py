import os
from tkinter import Tk, filedialog, Label, Button, Menu, messagebox
import markdown

# Função para selecionar a pasta de origem
def escolher_pasta_origem():
    global pasta_origem
    pasta_origem = filedialog.askdirectory(title="Escolher Pasta de Origem")
    label_origem.config(text=f"Pasta de Origem: {pasta_origem}")

# Função para selecionar a pasta de destino
def escolher_pasta_destino():
    global pasta_destino
    pasta_destino = filedialog.askdirectory(title="Escolher Pasta de Destino")
    label_destino.config(text=f"Pasta de Destino: {pasta_destino}")

# Função para converter ficheiros Markdown em HTML
def converter_markdown_para_html():
    if not pasta_origem or not pasta_destino:
        messagebox.showerror("Erro", "Por favor, selecione ambas as pastas.")
        return

    try:
        for ficheiro in os.listdir(pasta_origem):
            if ficheiro.endswith(".md"):
                caminho_ficheiro_md = os.path.join(pasta_origem, ficheiro)
                with open(caminho_ficheiro_md, "r", encoding="utf-8") as f:
                    texto_md = f.read()

                # Converter Markdown para HTML
                texto_html = markdown.markdown(texto_md)

                # Nomear o ficheiro HTML
                nome_html = os.path.splitext(ficheiro)[0] + ".html"
                caminho_ficheiro_html = os.path.join(pasta_destino, nome_html)

                # Gravar o ficheiro HTML
                with open(caminho_ficheiro_html, "w", encoding="utf-8") as f:
                    f.write(texto_html)

        messagebox.showinfo("Sucesso", "Ficheiros convertidos com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para sair da aplicação
def sair():
    janela.destroy()

# Configurar a janela principal
janela = Tk()
janela.title("Conversor de Markdown para HTML")
janela.geometry("600x300")

# Variáveis globais
pasta_origem = ""
pasta_destino = ""

# Menu
menu = Menu(janela)
menu_ajuda = Menu(menu, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Conversor de Markdown para HTML\nDesenvolvido em Python"))
menu.add_cascade(label="Ajuda", menu=menu_ajuda)
janela.config(menu=menu)

# Widgets
label_origem = Label(janela, text="Pasta de Origem: Não selecionada", anchor="w")
label_origem.pack(fill="x", padx=10, pady=5)

botao_origem = Button(janela, text="Escolher Pasta de Origem", command=escolher_pasta_origem)
botao_origem.pack(padx=10, pady=5)

label_destino = Label(janela, text="Pasta de Destino: Não selecionada", anchor="w")
label_destino.pack(fill="x", padx=10, pady=5)

botao_destino = Button(janela, text="Escolher Pasta de Destino", command=escolher_pasta_destino)
botao_destino.pack(padx=10, pady=5)

botao_converter = Button(janela, text="Converter Markdown para HTML", command=converter_markdown_para_html)
botao_converter.pack(padx=10, pady=5)

botao_sair = Button(janela, text="Sair", command=sair)
botao_sair.pack(padx=10, pady=5)

# Iniciar o loop principal da interface
janela.mainloop()
