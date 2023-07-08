import tkinter as tk


def salvar_selecoes():
    nova_janela = tk.Toplevel()
    nova_janela.title("Algoritmo do mercador")
    largura_tela = nova_janela.winfo_screenwidth()
    altura_tela = nova_janela.winfo_screenheight()
    largura = 400
    altura = 400
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    nova_janela.geometry(f"+{pos_x}+{pos_y}")
    nova_janela.geometry(f"{largura}x{altura}")

    texto = tk.Text(nova_janela, width=60, height=60)
    texto.pack()

    tabela_2 = []

    for i, checkbox in enumerate(checkboxes):
        if checkbox.get() == 1:
            item = tabela[i][0]
            valor = tabela[i][1]
            peso = tabela[i][2]
            tabela_2.append([item, valor, peso])

    n = len(tabela_2)
    W = 20  # limite de peso
    M = [[0 for x in range(W + 1)] for x in range(n + 1)]  # matriz de soluções

    for i in range(1, n + 1):
        item = tabela_2[i - 1][0]
        vi = tabela_2[i - 1][1]
        wi = tabela_2[i - 1][2]

        for w in range(1, W + 1):
            if wi > w:
                M[i][w] = M[i - 1][w]
            else:
                M[i][w] = max(M[i - 1][w], vi + M[i - 1][w - wi])

    texto.insert(tk.END, f"Valor total: {M[n][W]}\n")
    texto.insert(tk.END, "Itens selecionados:\n")
    w = W
    for i in range(n, 0, -1):
        if M[i][w] != M[i - 1][w]:
            texto.insert(tk.END, tabela_2[i - 1][0] + "\n")
            w = w - tabela_2[i - 1][2]

    nova_janela.mainloop()


# Tabela com as informações de cada arma
tabela = [
    ["SG-09R", 400, 2],
    ["Punisher", 500, 3],
    ["Red9", 700, 4],
    ["SR M1903", 600, 5],
    ["TMP", 800, 5],
    ["Espingarda W870", 900, 6],
    ["Blacktail", 1200, 6],
    ["Broken Butterfly", 2100, 6],
    ["Motim", 1400, 7],
    ["Stingray", 1500, 9],
    ["CQBR", 2000, 12],
    ["Striker", 1900, 13]
]

# Cria e configura a janela principal
janela = tk.Tk()
janela.title("Algoritmo do mercador")
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
largura = 950
altura = 550
pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2
janela.geometry(f"+{pos_x}+{pos_y}")
janela.geometry(f"{largura}x{altura}")
janela.resizable(False, False)

# Cria um frame para colocar o canvas 
frame = tk.Frame(janela)
frame.grid(row=0, column=0)
canvas = tk.Canvas(frame, width=largura, height=altura)
canvas.pack(side="left", fill="both", expand=True)
imagem = tk.PhotoImage(file="mercador-resident-evil-4.png")
canvas.create_image(0, 0, anchor="nw", image=imagem)
checkboxes = []

label_arma = tk.Label(janela, text="Arma")
label_valor = tk.Label(janela, text="Valor")
label_peso = tk.Label(janela, text="Peso")
canvas.create_window(200, 25, window=label_arma)
canvas.create_window(300, 25, window=label_valor)
canvas.create_window(400, 25, window=label_peso)

for i, item in enumerate(tabela):
    checkbox_var = tk.IntVar()
    checkbox = tk.Checkbutton(janela, variable=checkbox_var)
    canvas.create_window(25, (i + 2) * 25, window=checkbox)
    checkboxes.append(checkbox_var)

    for j, info in enumerate(item):
        label = tk.Label(janela, text=str(info))
        canvas.create_window((j + 2) * 100, (i + 2) * 25, window=label)

# Botão para salvar as seleções
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_selecoes)
canvas.create_window(largura // 2, (len(tabela) + 2) * 25, window=botao_salvar)
janela.mainloop()
