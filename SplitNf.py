# MODELO 33 2102 14564469000672 55 001 000091965 1 00233526 2
#        UF A/M  CNPJ           MD SER Nº NOTA   T COD NUM  V

# UNIDADE FEDERAL 
# ANO/MÊS
# CNPJ
# MODELO DO DOCUMENTO (55 - NF-e / 57 - CT-e / 58 - MDF-e)
# SÉRIE DO DOCUMENTO
# Nº DA NOTA
# TIPO DE EMISSÃO
# CÓDIGO NUMÉRICO
# DÍGITO VERIFICADOR

from tkinter import *

#def split_nf(cod_nf=00000000000000000000000000000000000000000000)
    #pass
    
    
class app:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="1st widget") 
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Quit"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()
        pass

root = Tk()
app(root)
root.mainloop()


