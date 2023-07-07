from tkinter import Tk, Canvas, PhotoImage

# Cria e configura a  janela principal
janela = Tk()
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
canvas = Canvas(janela, width=largura, height=altura)
canvas.pack()
#imagem_fundo = PhotoImage(file="resident-evil-mercador-fundo-preto.png")
imagem_fundo = PhotoImage(file="mercador-resident-evil-4.png")
canvas.configure(background="black")
canvas.create_image(0, 0, anchor="nw", image=imagem_fundo)

# Inicia o loop principal da janela
janela.mainloop()
