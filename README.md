### Python Search and Destroy Files

- Este é um programa de interface gráfica simples em Python usando a biblioteca Tkinter que permite que você procure por um arquivo ou diretório em seu sistema e oferece a opção de excluí-lo, caso seja encontrado.
- O programa começa com uma função recursiva usada para procurar o arquivo ou diretório no sistema. Ele percorre os diretórios e subdiretórios e verifica se o nome do arquivo corresponde ao nome fornecido.
- A função `name_file()` é chamada quando o botão "Buscar" é clicado. Ela obtém o nome do arquivo ou diretório da entrada do usuário, chama a função find() para procurar e exibir mensagens com o resultado.
- Se o arquivo ou diretório for encontrado, uma caixa de diálogo será exibida pedindo ao usuário que confirme a exclusão. Se o usuário confirmar, o código tentará excluir o arquivo ou diretório encontrado. `Se o programa estiver sendo executado como administrador, ele excluirá diretamente`. Caso contrário, ele solicitará privilégios elevados e tentará excluí-lo novamente.
- A interface gráfica é criada usando a biblioteca Tkinter. Há uma janela principal criada com o nome "Search and Destroy". Existem um campo de entrada para o nome do arquivo ou diretório a ser procurado e um botão "Buscar" que chama a função `name_file()`. Abaixo disso, há uma área de exibição de logs que mostra o progresso da busca.


# Requisitos

- Linguagem de programação: Python
- Dependências: `sys` `tkinter` `ttk` `messagebox` `ThemedTk` `os` `shutil` `ctypes` `unidecode`

# Instalação 

Clone este repositório em sua máquina local usando o comando abaixo:

   ```
   git clone <https://github.com/brunnosaid/Python-SD.git>
   ```

# Utilização

1. Insira o nome do arquivo desejado no campo de entrada de texto
2. Pressione o Botão `Buscar` e aguarde

**Contribuição**

1. Se você deseja contribuir para o projeto, siga as etapas abaixo:
   - Faça um fork deste repositório.
   - Crie um branch com sua nova funcionalidade ou correção: `git checkout -b minha-funcionalidade`
   - Faça as alterações necessárias e adicione os arquivos modificados: `git add .`
   - Faça o commit das suas alterações: `git commit -m 'Adicionando nova funcionalidade'`
   - Envie para o branch criado no seu repositório fork: `git push origin minha-funcionalidade`
   - Crie um novo pull request para o repositório original.

