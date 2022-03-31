from logging import lastResort
from caixa import Loterias
from tkinter  import *

def buscando(nconcurso):
    sena = Loterias("mega-sena")
    sena.buscar(nconcurso)
    conc = sena.concurso()
    msort = sena.Municipio_Sorteio()
    data = sena.DataApuracao()

    dez = sena.DezenasSorteadasOrdemSorteio()
    lresult.delete(0, END)
    lresult.insert(END, 'Concurso: {}'.format(conc))
    lresult.insert(END,'Data sorteio: {}'.format(data))
    lresult.insert(END, 'local:{}'.format(msort))
    lresult.insert(END, 'Dezenas sorteadas')
    lresult.insert(END, '{}'.format(dez))

form1 = Tk()
form1.title("Mega-sena")

form1.resizable(False, False)
form1.iconbitmap("icones/Martz90-Hex-Game-gta-iv.ico")
lconcurso = Label(form1, text="Numero do concurso")
tconcurso = Entry(form1, width=5)
b1 = Button(form1, text="Procurar", command=lambda:buscando(tconcurso.get()))
lresult = Listbox(form1, width=40)

lconcurso.grid(row=0, column=0, padx=2)
tconcurso.grid(row=1, column=0, padx=2)
b1.grid(row=2)
lresult.grid(row=3)

form1.mainloop()