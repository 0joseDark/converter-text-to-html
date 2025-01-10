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