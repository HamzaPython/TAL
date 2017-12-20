# from tkinter import *
# main=Tk()
# main.title("Notre Application")
# main.geometry("500x400+350+500")
# titre=Label(main,text="les algorithmes :")
algorithme = {1: 'Bleu', 2: 'WER', 3: 'F-measure'}
titre.grid(row=0, column=0)
valeur = IntVar()
for i in algorithme:
    radio1 = Radiobutton(
        main, variable=valeur, text=algorithme[i], value=i, width=10)
    radio1.grid(row=1, column=i)
# var1='Bleu'
# var2='WER'
# var3='F-measure'


def recup():
    return valeur.get()


# def choix():
#     if recup()==1:
#        return var1
#     elif recup()==2:
#         return var2
#     elif recup()==3:
#        return  var3
#
# def fonct():
#     print(choix())
# def lab():
#     lb=Label(main,text=fonct())
#     lb.grid(row=4,column=1)

botton = Button(main, text="Calcule du resultat ", command=lab)
botton.grid()
main.mainloop()
