from tkinter import*
from tkinter import ttk



raiz = Tk()
raiz.geometry("910x436")
raiz.config(bg="white")

imagen = PhotoImage(file="grafica1.png")
imagen2 = PhotoImage(file="temperaturas1.png")
imagen3 = PhotoImage(file="niveltanque1.png")
imagen4 = PhotoImage(file="velocidadbomba1.png")
menuimagen = PhotoImage(file="menu.png")

mainFrame = Frame(raiz, bg="black", width=910, height=7)
mainFrame.grid(column=0, row=1)

frame1 = Frame(raiz, bg="white", width=910, height=7)
frame1.grid(column=0, row=0)

frame2 = Frame(mainFrame, bg="cyan4", width=920, height=37)
frame2.grid(column=0, row=0)

frame3 = Frame(mainFrame, bg="black", width=910, height=381)
frame3.grid(column=0, row=1)

frame3_1 = Frame(frame3, bg="black", width=484, height=381)
frame3_1.grid(column=0, row=0)

frame3_2 = Frame(frame3, bg="black", width=426, height=381)
frame3_2.grid(column=1, row=0)

frame3_1_1 = Frame(frame3_1, bg="black", width=485, height=227)
frame3_1_1.grid(column=0, row=0)

frame3_1_2 = Frame(frame3_1, bg="black", width=485, height=154)
frame3_1_2.grid(column=0, row=1)

#ultimos frame arriba

frame3_1_1_1 = Frame(frame3_1_1, bg="black", width=89, height=227 )
frame3_1_1_1.grid(column=0, row=0, pady=3)

frame3_1_1_2 = Frame(frame3_1_1, bg="gray20", width=135, height=227, borderwidth=3, relief="raised")
frame3_1_1_2.grid(column=1, row=0, pady=3)

frame3_1_1_3 = Frame(frame3_1_1, bg="gray20", width=261, height=227, borderwidth=3, relief="raised")
frame3_1_1_3.grid(column=2, row=0)

#ultimos frame abajo
frame3_1_2_1 = Frame(frame3_1_2, bg="black", width=89, height=154)
frame3_1_2_1.grid(column=0, row=0)

frame3_1_2_2 = Frame(frame3_1_2, bg="gray20", width=198, height=154, borderwidth=3, relief="raised")
frame3_1_2_2.grid(column=1, row=0)

frame3_1_2_3 = Frame(frame3_1_2, bg="gray20", width=198, height=154, borderwidth=3, relief="raised")
frame3_1_2_3.grid(column=2, row=0)

#ultimo frame solo

frame3_2_1 = Frame(frame3_2, bg="gray20", width=325, height=381)
frame3_2_1.grid(column=0, row=0)

frame3_2_2 = Frame(frame3_2, bg="black", width=101, height=381)
frame3_2_2.grid(column=1, row=0)

#ahora si los ultimos del lado derecho del negro

framederecho1 = Frame(frame3_2_1, bg="gray20", width=325, height=292, borderwidth=3, relief="raised" )
framederecho1.grid(column=0, row=0)

framederecho2 = Frame(frame3_2_1, bg="black", width=325, height=89)
framederecho2.grid(column=0, row=1)

#frames para indicadores digitales

frameind1 = Frame(frame3_1_1_2, bg="gray20", width=135, height=30)
frameind1.grid(column=0, row=0)

frameind2 = Frame(frame3_1_1_2, bg="gray20", width=135, height=101)
frameind2.grid(column=0, row=1)

frameind3 = Frame(frame3_1_1_2, bg="gray20", width=135, height=30)
frameind3.grid(column=0, row=2)

frameind4 = Frame(frame3_1_1_2, bg="gray20", width=135, height=63)
frameind4.grid(column=0, row=3)

#frames para indicadores particion

framepart1 = Frame(frameind2, bg="gray20", width=67, height=101)
framepart1.grid(column=0, row=0)

framepart2 = Frame(frameind2, bg="gray20", width=68, height=101)
framepart2.grid(column=1, row=0)

framepart3 = Frame(frameind4, bg="gray20", width=67, height=63)
framepart3.grid(column=0, row=0)

framepart4 = Frame(frameind4, bg="gray20", width=68, height=63)
framepart4.grid(column=1, row=0)

#etiquetas

indicador = Label(frameind1, text="Indicadores Digitales    ", bg="gray20", fg="cyan4")
indicador.grid(column=0, row=0)

linea1 = Label(framepart1, text="Linea 1:   ", bg="gray20", fg="white")
linea1.grid(column=0, row=0)

linea2 = Label(framepart1, text="Linea 2:   ", bg="gray20", fg="white")
linea2.grid(column=0, row=1, pady=18)

linea3 = Label(framepart1, text="Linea 1:   ", bg="gray20", fg="white")
linea3.grid(column=0, row=2)

on1 = Label(framepart2, text="On          ", bg="gray20", fg="white")
on1.grid(column=0, row=0)

on2 = Label(framepart2, text="On          ", bg="gray20", fg="white")
on2.grid(column=0, row=1, pady=18)

on3 = Label(framepart2, text="On          ", bg="gray20", fg="white")
on3.grid(column=0, row=2)

boton1 = Radiobutton(framepart2, bg="gray20", fg="green", borderwidth=0)
boton1.grid(column=1, row=0)

boton2 = Radiobutton(framepart2, bg="gray20", fg="green", borderwidth=0)
boton2.grid(column=1, row=1, pady=18)

boton3 = Radiobutton(framepart2, bg="gray20", fg="green", borderwidth=0)
boton3.grid(column=1, row=2)

gabinete = Label(frameind3, text="Gabinete: ", bg="gray20", fg="white")
gabinete.grid(column=0, row=0, pady=10)

abierto = Label(frameind3, text="Abierto ", bg="gray20", fg="white")
abierto.grid(column=1, row=0)

boton4 = Radiobutton(frameind3, bg="gray20",fg="red", borderwidth=0)
boton4.grid(column=2, row=0)

alarma = Label(framepart3, text="Alarma:", bg="gray20", fg="white")
alarma.grid(column=0, row=0)

alarma2 = Label(framepart3, text="Alarma2:", bg="gray20", fg="white")
alarma2.grid(column=0, row=2)

vacio = Label(framepart3, height=1, text="", bg="gray20", fg="white")
vacio.grid(column=0, row=1)

on4= Label(framepart4, text="On           ", bg="gray20", fg="white")
on4.grid(column=0, row=0)

vacio = Label(framepart4, height=1, text="", bg="gray20", fg="white")
vacio.grid(column=0, row=1)

off = Label(framepart4, text="Off           ", bg="gray20", fg="white")
off.grid(column=0, row=2)

boton5 = Radiobutton(framepart4, bg="gray20",fg="red", borderwidth=0)
boton5.grid(column=1, row=0)

boton6 = Radiobutton(framepart4, bg="gray20",fg="green", borderwidth=0)
boton6.grid(column=1, row=2)

etqImagen =Label(framederecho1, bg="gray20", borderwidth=0)
etqImagen.grid(column=0, row=0, pady=6)
etqImagen['image']= imagen

etqImagen2 =Label(frame3_1_1_3, bg="gray20", borderwidth=0)
etqImagen2.grid(column=0, row=0)
etqImagen2['image']= imagen2

etqImagen3 =Label(frame3_1_2_3, bg="gray20", borderwidth=0)
etqImagen3.grid(column=0, row=0)
etqImagen3['image']= imagen3

etqImagen4 =Label(frame3_1_2_2, bg="gray20", borderwidth=0)
etqImagen4.grid(column=0, row=0)
etqImagen4['image']= imagen4

menuImagen5 =Button(frame2, bg="cyan4", borderwidth=0)
menuImagen5.grid(column=0, row=0)
menuImagen5['image']= menuimagen

spai = Label(frame2, height=2, text="SPAI 4.0                                                                                                                                                                                                                                                                                            ", bg="cyan4", fg="white")
spai.grid(column=1, row=0)

barra = Scrollbar(frame3_2_2, width=17).place(x=75, y=0)



raiz.mainloop()