from tkinter import *


class Application:
    def __init__(self, master=None):
        self.frame = Frame(master)
        self.frame.grid()

        self.lbl1 = Label(self.frame, text='NF')  # Frame para organização e amostragem dos gadgets
        self.lbl1.grid(padx=5, pady=10, column=1, row=1)

        self.btn_split = Button(self.frame, text='Split')  # Botão 'Split'
        self.btn_split["command"] = self.print_entry
        self.btn_split.grid(padx=5, pady=10, column=3, row=1)

        self.nf_entry = Entry(self.frame)  # Entrada de texto
        self.nf_entry.grid(padx=5, pady=10, column=2, row=1)

        self.mensagem = Label(self.frame, text="")  # Saída para a entrada de texto após clicar no botão
        self.mensagem.grid(padx=5, pady=10, column=1, row=2)

        pass

    def print_entry(self):
        entry = self.nf_entry.get()
        self.mensagem["text"] = entry

root = Tk()
Application(root)
root.mainloop()