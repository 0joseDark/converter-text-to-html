# converter-text-to-html

### Explicação

1. **Importação de módulos**:
   - `os`: Permite manipular caminhos de ficheiros e diretórios.
   - `Tkinter`: Cria a interface gráfica para interação com o utilizador.

2. **Funções**:
   - `escolher_pasta_origem`: Mostra uma janela para selecionar a pasta de origem.
   - `escolher_pasta_destino`: Mostra uma janela para selecionar a pasta de destino.
   - `processar_ficheiros`: Lê os ficheiros `.txt` da pasta de origem, converte para HTML e guarda na pasta de destino.
   - `sair`: Encerra a aplicação.

3. **Janela principal**:
   - Configurada com título, tamanho fixo e elementos como etiquetas, botões e mensagens informativas.

4. **Processamento dos ficheiros**:
   - Os ficheiros `.txt` da pasta de origem são lidos e o seu conteúdo é encapsulado em HTML.
   - Cada ficheiro HTML gerado recebe um nome incremental, como `ficheiro_1.html`.

5. **Mensagens informativas**:
   - Mostram erros ou sucessos ao utilizador, melhorando a usabilidade.

6. **Execução**:
   - A função `mainloop` mantém a janela aberta até que o utilizador a feche ou clique no botão "Sair".
   ---
1. Selecionar uma pasta de origem contendo ficheiros Markdown.
2. Escolher uma pasta de destino para gravar os ficheiros convertidos em HTML.
3. Converter os ficheiros Markdown em HTML.
4. Sair da aplicação.



---

### Explicação dos Módulos Utilizados

1. **`os`**: Usado para manipular caminhos de ficheiros e pastas.
2. **`tkinter`**: Fornece a interface gráfica, incluindo botões, menus, e caixas de diálogo.
3. **`filedialog`**: Permite abrir janelas para seleção de ficheiros ou pastas.
4. **`messagebox`**: Mostra mensagens de erro ou sucesso.
5. **`markdown`**: Converte texto em formato Markdown para HTML. Este módulo deve ser instalado com `pip install markdown`.

---

### Como Usar o Programa

1. Certifique-se de ter o Python instalado no Windows 10.
2. Instale o módulo `markdown` com o comando:
   ```bash
   pip install markdown
   ```
3. Execute o script.
4. Na interface:
   - Clique em "Escolher Pasta de Origem" e selecione a pasta com os ficheiros Markdown.
   - Clique em "Escolher Pasta de Destino" e escolha a pasta onde os ficheiros HTML serão gravados.
   - Clique em "Converter Markdown para HTML" para iniciar a conversão.
   - Clique em "Sair" para fechar a aplicação.
