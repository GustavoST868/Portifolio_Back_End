import tkinter as tk

def Interface_Skills():
    def Botao_Voltar():
        janela.destroy()
        Interface()

    janela = tk.Tk()
    janela.title("")
    janela.geometry("600x600")

    imagem = tk.PhotoImage(file=r".\imagem.skills.png")
    imagem_label = tk.Label(janela, image=imagem)
    imagem_label.place(x=0, y=0, relheight=1, relwidth=1)

    botao_voltar = tk.Button(janela, text="Voltar", height=2, width=40, relief="flat", command=Botao_Voltar, borderwidth=0, highlightthickness=0)
    botao_voltar.place(x=155, y=480)

    janela.mainloop()

def Interface_Sobre():
    def Botao_Voltar():
        janela.destroy()
        Interface()

    janela = tk.Tk()
    janela.title("")
    janela.geometry("600x600")

    imagem = tk.PhotoImage(file=r".\imagem.sobre.png")
    imagem_label = tk.Label(janela, image=imagem)
    imagem_label.place(x=0, y=0, relheight=1, relwidth=1)

    botao_voltar = tk.Button(janela, text="Voltar", height=2, width=40, relief="flat", command=Botao_Voltar, borderwidth=0, highlightthickness=0)
    botao_voltar.place(x=155, y=524)

    janela.mainloop()

def Interface():
    def Botao_Sobre():
        janela.destroy()
        Interface_Sobre()
        
    def Botao_Skills():
        janela.destroy()
        Interface_Skills()
       
    janela = tk.Tk()
    janela.title("")
    janela.geometry("600x600")

    imagem = tk.PhotoImage(file=r".\imagem.png")
    imagem_label = tk.Label(janela, image=imagem)
    imagem_label.place(x=0, y=0, relheight=1, relwidth=1)

    botao_sobre = tk.Button(janela, text="Sobre", height=2, width=45, relief="flat", command=Botao_Sobre, borderwidth=0, highlightthickness=0)
    botao_sobre.place(x=140, y=264)

    botao_skills = tk.Button(janela, text="Skills", height=2, width=45, relief="flat", command=Botao_Skills, borderwidth=0, highlightthickness=0)
    botao_skills.place(x=140, y=264 + 120)

    janela.mainloop()

if __name__ == "__main__":
    Interface()
