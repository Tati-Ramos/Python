#O módulo webbrowser fornece uma interface de alto nível para permitir a exibição de documentos baseados na web aos usuários.
import webbrowser

#O pacote tkinter (“interface Tk”) é a interface padrão do Python para o kit de ferramentas Tcl/Tk GUI.
from tkinter import *


root = Tk()

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop()
