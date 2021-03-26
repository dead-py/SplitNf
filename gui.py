#!/bin/python3

from tkinter import Label, Button, Entry, Frame, Grid, mainloop, Tk, Listbox, END
from split import *
from export import *


class Application:

    def __init__(self, master=None):
        master.minsize(width=245, height=250)
        master.maxsize(width=245, height=250)
        master.title("   NF Splitter")

        self.frame = Frame(master)
        self.frame.grid()

        self.lbl1 = Label(self.frame, text='NF')  # Frame para organização e amostragem dos gadgets
        self.lbl1.grid(padx=[15,1], pady=1, column=1, row=1)

        self.btn_split = Button(self.frame, text='Split')  # Botão 'Split'
        self.btn_split["command"] = self.print_data
        self.btn_split.grid(padx=[1, 1], pady=1, column=3, row=1)

        self.btn_clear = Button(self.frame,  text='Clear')  # Botão 'Clear'
        
        self.btn_clear["command"] = self.clear_data
        self.btn_clear.grid(padx=[1,89], pady=5, column=2, row=5)

        self.nf_entry = Entry(self.frame, width=25)  # Entrada de texto
        self.nf_entry.grid(padx=1, pady=1, column=2, row=1)

        self.mensagem = Label(self.frame, text="Dados da Nota")  # Saída para a entrada de texto após clicar no botão
        self.mensagem.grid(column=2, row=3)

        self.listbox = Listbox(self.frame, width=25, height=9)
        self.listbox.grid(padx=1, pady=1, column=2, row=4)

        self.btn_export = Button(self.frame, text="Export TXT")  # Exporta a lista de notas para CSV
        self.btn_export["command"] = self.export_txt
        self.btn_export.grid(padx=[65,1],column=2, row=5)
        pass


    def  print_data(self):
        entry = self.nf_entry.get()
        

        if len(entry) > 44 or len(entry) == 44:
            data = split_nf_list(entry)

        else:
            data = split_nf_list('00000000000000000000000000000000000000000000')

        if self.listbox:
                self.listbox.delete(0, self.listbox.size())

        for d in data:

            if data == 1:
                self.listbox.delete(0,self.listbox.size())
                self.listbox.insert(1, "Nº Inválido")

            else:

                self.listbox.insert(END, d)


    def clear_data(self):
        self.listbox.delete(0, self.listbox.size())
        pass


    def export_txt(self):
        entry = self.nf_entry.get()
        data = split_nf_list(entry)
        export_txt(data)


        

root = Tk()
root.geometry("250x250")
Application(root)
root.mainloop()