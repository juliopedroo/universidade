import math
import tkinter as tk
from tkinter import messagebox

# Função para o Princípio da Regra da Soma
def principio_regra_soma():
    # Obtém a entrada do usuário
    n1 = entry1.get()
    n2 = entry2.get()

    #Controle de Erros: verifica se as entradas não estão em brancos e se são números inteiros
    if not n1.isdigit() or not n2.isdigit():
        messagebox.showerror("Erro", "Verifique se digitou apenas números inteiros e se preencheu os dois campos necessários!")
        return

    n1 = int(n1)
    n2 = int(n2)
    total = n1 + n2
    possibilidades = list(range(1, n1 + 1)) + list(range(1, n2 + 1))
    messagebox.showinfo("Resultado", f"Total de possibilidades: {total}\nPossibilidades: {possibilidades}")

# Função para o Princípio da Regra do Produto
def principio_regra_produto():
    # Obtém a entrada do usuário
    n1 = entry1.get()
    n2 = entry2.get()

    #Controle de Erros: verifica se as entradas não estão em brancos e se são números inteiros
    if not n1.isdigit() or not n2.isdigit():
        messagebox.showerror("Erro", "Verifique se digitou apenas números inteiros e se preencheu os dois campos necessários!")
        return

    n1 = int(n1)
    n2 = int(n2)
    total = n1 * n2
    possibilidades = [(i, j) for i in range(1, n1 + 1) for j in range(1, n2 + 1)]
    messagebox.showinfo("Resultado", f"Total de possibilidades: {total}\nPossibilidades: {possibilidades}")

# Função para Permutação
def permutacao():
    # Obtém a entrada do usuário
    n = entry1.get()

    #Controle de Erros: verifica se a entrada não está em branco e se é um número inteiro
    if not n.isdigit():
        messagebox.showerror("Erro", "Verifique se digitou um número inteiro!")
        return

    n = int(n)
    total = math.factorial(n)
    elementos = list(range(1, n + 1))
    possibilidades = []

    for i in range(math.perm(n, n)):
        permutacao = []
        for j in range(n):
            permutacao.append(elementos[(i // math.factorial(n - j - 1)) % (n - j)])
        possibilidades.append(permutacao)

    messagebox.showinfo("Resultado", f"Total de permutações: {total}\nPossibilidades: {possibilidades}")


# Função para Permutação utilizando as letras de uma palavra
def permutacao_palavra():
    # Obtém a entrada do usuário
    palavra = entry1.get()

    # Controle de Erro: verifica se a entrada contém apenas letras
    if not palavra.isalpha():
        messagebox.showerror("Erro", "A entrada deve ser uma palavra e não pode conter números!") # Exibe uma mensagem de erro se a entrada não for uma palavra
        return

    # Calcula o total de permutações
    total = math.factorial(len(palavra))
    caracteres = list(palavra)
    possibilidades = []
    for i in range(math.perm(len(palavra), len(palavra))):
        permutacao = []
        for j in range(len(palavra)):
            permutacao.append(caracteres[(i // math.factorial(len(palavra) - j - 1)) % (len(palavra) - j)])
        possibilidades.append("".join(permutacao))
    
    # Exibe o resultado das permutações
    messagebox.showinfo("Resultado", f"Total de permutações utilizando as letras da palavra: {total}\nPossibilidades: {possibilidades}")

# Função para Amostragem com Reposição
def amostragem_com_reposicao():
    # Obtém a entrada do usuário
    n = entry1.get()
    k = entry2.get()

    #Controle de Erros: verifica se as entradas não estão em brancos e se são números inteiros
    if not n.isdigit() or not k.isdigit():
        messagebox.showerror("Erro", "Verifique se digitou apenas números inteiros e se preencheu os dois campos necessários!")
        return

    n = int(n)
    k = int(k)
    total = n ** k
    elementos = list(range(1, n + 1))
    possibilidades = []
    for i in range(total):
        amostra = [elementos[i // (n**j) % n] for j in range(k-1, -1, -1)]
        possibilidades.append(amostra)
    messagebox.showinfo("Resultado", f"Total de amostras com reposição: {total}\nPossibilidades: {possibilidades}")

# Função para Amostragem sem Reposição
def amostragem_sem_reposicao():
    # Obtém a entrada do usuário
    n = entry1.get()
    k = entry2.get()

    #Controle de Erros: verifica se as entradas não estão em brancos e se são números inteiros
    if not n.isdigit() or not k.isdigit():
        messagebox.showerror("Erro", "Verifique se digitou apenas números inteiros e se preencheu os dois campos necessários!")
        return

    n = int(n)
    k = int(k)
    total = math.comb(n, k)
    elementos = list(range(1, n + 1))
    indices = list(range(k))
    possibilidades = []
    for i in range(total):
        amostra = [elementos[j] for j in indices]
        possibilidades.append(amostra)
        indices[-1] += 1
        for j in range(k - 1, -1, -1):
            if indices[j] == n - k + j + 1 and j != 0:
                indices[j - 1] += 1
                for l in range(j, k):
                    indices[l] = indices[l - 1] + 1
    messagebox.showinfo("Resultado", f"Total de amostras sem reposição: {total}\nPossibilidades: {possibilidades}")

# Função para Combinações
def combinacoes():
    # Obtém a entrada do usuário
    n = entry1.get()
    k = entry2.get()

    #Controle de Erros: verifica se as entradas não estão em brancos e se são números inteiros
    if not n.isdigit() or not k.isdigit():
        messagebox.showerror("Erro", "Verifique se digitou apenas números inteiros e se preencheu os dois campos necessários!")
        return

    n = int(n)
    k = int(k)
    total = math.comb(n, k)
    elementos = list(range(1, n + 1))
    indices = list(range(k))
    possibilidades = []
    for i in range(total):
        combinacao = [elementos[j] for j in indices]
        possibilidades.append(combinacao)
        indices[-1] += 1
        for j in range(k - 1, -1, -1):
            if indices[j] == n - k + j + 1 and j != 0:
                indices[j - 1] += 1
                for l in range(j, k):
                    indices[l] = indices[l - 1] + 1
    messagebox.showinfo("Resultado", f"Total de combinações: {total}\nPossibilidades: {possibilidades}")

# Função com as informações de créditos do programa
def exibir_creditos():
    creditos = """
    Projeto de Matemática Discreta - Cálculos de Análise Combinatória

    • Professor: 
        Viviano

    • Aluno:
        Julio Monteiro
    """

    messagebox.showinfo("Créditos", creditos)

# Define qual orientação deve ser exibida a depender da operação escolhida do dropdown
def update_operacao(*args):
    operacao = dropdown.get()
    orientation = orientacoes_operacoes.get(operacao, "")
    message_label.config(text=f"Orientação: {orientation}")

# Atenção: a função update_operacao, está sendo utilizada como um callback para o evento de seleção do dropdown. 
# Ao adicionar o parâmetro *args, estamos permitindo que a função seja chamada com argumentos adicionais que
# podem ser passados pelo evento.

#Função que captura a escolha de operação do dropdown e executa a função referente à escolha
def executar_operacao():
    operacao = dropdown.get()
    if operacao == "Princípio da Regra da Soma":
        principio_regra_soma()
    elif operacao == "Princípio da Regra do Produto":
        principio_regra_produto()
    elif operacao == "Permutação":
        permutacao()
    elif operacao == "Permutação utilizando as letras de uma palavra":
        permutacao_palavra()
    elif operacao == "Amostragem com reposição":
        amostragem_com_reposicao()
    elif operacao == "Amostragem sem reposição":
        amostragem_sem_reposicao()
    elif operacao == "Combinações":
        combinacoes()

# Orientações referentes a cada operação possível de seleção
orientacoes_operacoes = {
    "Princípio da Regra da Soma": "Digite dois valores inteiros para realizar\n a soma.",
    "Princípio da Regra do Produto": "Digite dois valores inteiros para realizar\n o produto.",
    "Permutação": "Digite um valor inteiro para calcular\n a permutação (nesse caso o campo do valor 2 pode ficar em branco).",
    "Permutação utilizando as letras de uma palavra": "Digite uma palavra para calcular\n a permutação (nesse caso o campo do valor 2 pode ficar em branco).",
    "Amostragem com reposição": "Digite dois valores inteiros para realizar a\n amostragem com reposição.",
    "Amostragem sem reposição": "Digite dois valores inteiros para realizar a\n amostragem sem reposição.",
    "Combinações": "Digite dois valores inteiros para realizar\n as combinações."
}


#Inicializando a janela da calculadora
root = tk.Tk()
root.title("Calculadora de Possibilidades")
root.geometry("500x250")

# Dropdown para seleção da operação desejada
dropdown = tk.StringVar(root)
dropdown.set("Selecione uma operação")
options = [
    "Princípio da Regra da Soma",
    "Princípio da Regra do Produto",
    "Permutação",
    "Permutação utilizando as letras de uma palavra",
    "Amostragem com reposição",
    "Amostragem sem reposição",
    "Combinações"
]
dropdown_menu = tk.OptionMenu(root, dropdown, *options, command=update_operacao)
dropdown_menu.pack()

# Exibição da Orientação referene à operação selecionada
message_label = tk.Label(root, text="Orientação: ")
message_label.pack()

#Espaçamento vertical entre elementos
space_label = tk.Label(root, height=1)
space_label.pack()

# Label para input do valor 1
label1 = tk.Label(root, text="Digite o valor 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

# Label para input do valor 2 (se necessário)
label2 = tk.Label(root, text="Digite o valor 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

#Botão para executar a operação selecionada
button = tk.Button(root, text="Calcular", command=executar_operacao)
button.pack()

#Espaçamento vertical entre elementos
space_label = tk.Label(root, height=2)
space_label.pack()

# Botão de créditos
btn_creditos = tk.Button(root, text="Créditos", command=exibir_creditos, font=("Arial", 7), bg="lightblue", fg="black", width=5, height=1)
btn_creditos.pack()

# Loop do programa
root.mainloop()