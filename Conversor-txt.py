import os
from tkinter import Tk, Label, Button, filedialog, messagebox

# Função para selecionar a pasta de origem
def escolher_pasta_origem():
    global pasta_origem
    pasta_origem = filedialog.askdirectory(title="Escolher pasta de origem")
    if pasta_origem:
        lbl_origem.config(text=f"Pasta de origem: {pasta_origem}")

# Função para selecionar a pasta de destino
def escolher_pasta_destino():
    global pasta_destino
    pasta_destino = filedialog.askdirectory(title="Escolher pasta de destino")
    if pasta_destino:
        lbl_destino.config(text=f"Pasta de destino: {pasta_destino}")

# Função para processar os ficheiros
def processar_ficheiros():
    if not pasta_origem or not pasta_destino:
        messagebox.showerror("Erro", "Por favor, escolha as pastas de origem e destino.")
        return

    ficheiros_texto = [f for f in os.listdir(pasta_origem) if f.endswith(".txt")]
    
    if not ficheiros_texto:
        messagebox.showinfo("Informação", "Não foram encontrados ficheiros de texto na pasta de origem.")
        return

    for i, ficheiro in enumerate(ficheiros_texto):
        caminho_ficheiro = os.path.join(pasta_origem, ficheiro)
        with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        nome_html = f"ficheiro_{i + 1}.html"
        caminho_html = os.path.join(pasta_destino, nome_html)
        with open(caminho_html, 'w', encoding='utf-8') as f:
            f.write(f"<html><body><pre>{conteudo}</pre></body></html>")
    
    messagebox.showinfo("Sucesso", f"{len(ficheiros_texto)} ficheiros foram convertidos para HTML com sucesso!")

# Função para sair do programa
def sair():
    janela.quit()

# Configuração da janela principal
janela = Tk()
janela.title("Conversor de Texto para HTML")
janela.geometry("600x300")
janela.resizable(False, False)

# Variáveis globais
pasta_origem = ""
pasta_destino = ""

# Elementos da interface
Label(janela, text="Escolha as pastas de origem e destino:", font=("Arial", 12)).pack(pady=10)

lbl_origem = Label(janela, text="Pasta de origem: Não escolhida", font=("Arial", 10))
lbl_origem.pack(pady=5)

btn_origem = Button(janela, text="Escolher Pasta de Origem", command=escolher_pasta_origem)
btn_origem.pack(pady=5)

lbl_destino = Label(janela, text="Pasta de destino: Não escolhida", font=("Arial", 10))
lbl_destino.pack(pady=5)

btn_destino = Button(janela, text="Escolher Pasta de Destino", command=escolher_pasta_destino)
btn_destino.pack(pady=5)

btn_processar = Button(janela, text="Processar Ficheiros", command=processar_ficheiros)
btn_processar.pack(pady=20)

btn_sair = Button(janela, text="Sair", command=sair)
btn_sair.pack(pady=10)

# Iniciar o loop principal da janela
janela.mainloop()
