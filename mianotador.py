from tkinter import *

from tkinter import messagebox

from tkinter.filedialog import askopenfile, asksaveasfile


def acopiar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

def apegar():

    editor.insert(INSERT, editor.clipboard_get())

def acortar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

    editor.delete("sel.first", "sel.last")

def adeshacer():

    editor.edit_undo()

def arehacer():

    editor.edit_redo()

def anuevo():

    editor.delete(1.0,END)

def aabrir():

    documento = askopenfile(filetypes=[("Archivo de texto","*.txt")])

    if documento != None:

        editor.insert(1.0, documento.read())

def aguardar():

    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])

    print(documento.write(editor.get(1.0, END)))

def aguardarcomo():
    
    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])

    print(documento.write(editor.get(1.0, END)))
 

def aacerca():

    messagebox.showinfo ("Acerca de Mi Anotador ", "MiAnotador  es un lector de archivos de texto plano,"
    
   
                                                         

                                                         

                                                         " Tenemos  funcionalidades que no tienen otros anotadores"

                                                         " bloc de notas de Windows, la primera es la opción de rehacer,"

                                                         " la segunda característica es que se puede deshacer o rehacer tantas veces se desee")

                                                         


if __name__ == "__main__":



    ventana = Tk()
    



    menubar = Menu(ventana)

    archivo = Menu(menubar, tearoff=0)

    archivo.add_command(label="Nuevo     ", command=anuevo)

    archivo.add_command(label="Abrir     ", command=aabrir)

    archivo.add_command(label="Guardar     ", command=aguardar)


    archivo.add_command(label="Guardar como     ", command=aguardarcomo)
    archivo.add_command(label="Salir     ", command=ventana.quit)

    menubar.add_cascade(label="Archivo", menu=archivo)



    editar = Menu(menubar, tearoff=0)

    editar.add_command(label="Deshacer     ", command=adeshacer)

    editar.add_command(label="Rehacer     ", command=arehacer)

    editar.add_separator()

    editar.add_command(label="Copiar     ", command=acopiar)

    editar.add_command(label="Pegar     ", command=apegar)

    editar.add_command(label="Cortar     ", command=acortar)

    menubar.add_cascade(label="Edición", menu=editar)



    ayuda = Menu(menubar, tearoff=0)

    ayuda.add_command(label="Acerca de MiAnotador  ", command=aacerca)

    menubar.add_cascade(label="Ayuda", menu=ayuda)



    editor = Text(ventana, undo="true")

    editor.pack(side=TOP, fill=BOTH, expand=1)


ventana.title("MiAnotador: Escribimos aca")

ventana.geometry("800x500")
    
ventana.config(menu= menubar , bg="blue" )
##La idea era que el titulo tendria fondo azul, no lo logre por mas que intente varias veces##

    
ventana.mainloop()

    