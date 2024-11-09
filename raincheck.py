import os
import sys

def read_242_file(filename):
    # Adiciona a extensão '.242' se não estiver presente
    if not filename.endswith(".242"):
        filename += ".242"
    
    # Verifica se o arquivo existe no diretório atual
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content  # Retorna o conteúdo do arquivo
    else:
        return None  # Retorna None se o arquivo não for encontrado

def main():
    # Verifica se um nome de arquivo foi fornecido como argumento de linha de comando
    if len(sys.argv) < 2:
        print("Uso: program.py arquivo_fonte[.242]")
        return
    
    # Obtém o nome do arquivo do argumento da linha de comando
    filename = sys.argv[1]
    # Chama a função de leitura do arquivo
    content = read_242_file(filename)
    
    # Exibe o conteúdo do arquivo ou uma mensagem de erro
    if content is not None:
        print(content)
    else:
        print(f"Arquivo '{filename}' não encontrado")

# Chama a função main se este script for executado
if __name__ == "__main__":
    main()

