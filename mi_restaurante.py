import random 
from tkinter import *
import datetime
from tkinter import filedialog, messagebox

# Crear la funcionalidad de cada boton de la calculadora que cuando los presionen se muestren en el visor
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)# Borra lo que se enci¿uentre en el visor y no nosmuestre los números uqe ya se amrcaron dos veces
    visor_calculadora.insert(END, operador)

# Borrar en calculadora
def borrar():
    global operador # aca y con la línea de abajo para cuando borremos y volvemos a escribir no traiga el numero anterio si no que borre todo
    operador = ''
    visor_calculadora.delete(0, END)# 0, END borra desde la posición 0 hasta el efinal END    

# Obtener Resultado
def obtener_resultado():
    global operador
    resultado = str(eval(operador)) # eval es evaluar el operedor lo que hace es evaluar lo que esta en operador si es suma resta, y asi sea string va hacer la operación
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

#Función ckeck de las comidas, bebidas y postres el cuadro con el chulo jeje  revisar si esta activo o no 
def revisar_check():
    x = 0
    for c in cuadro_comida:
        if variables_comida[x].get() == 1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() == '0':# esta línea se ace porque cuando chekeamos un cuadro y ponemos un valos de precio y pasamos a otro cuadro para chekaerlo borra el anterior por la línes que tenmos acontinuación.
                cuadro_comida[x].delete(0, END)# se va el cero cuando checkeamos el cuadro
            cuadro_comida[x].focus()# focus cuando ckeamos el cuadro el cursor aparezca en el espcaio para llenar 
        else: # cuado no este chekeado vuleva aprecer el cero
            cuadro_comida[x].config(state=DISABLED) 
            texto_comida[x].set('0')   
        x +=1   

    x = 0
    for c in cuadro_bebida:
        if variables_bebida[x].get() == 1:
            cuadro_bebida[x].config(state=NORMAL)
            if cuadro_bebida[x].get() == '0':# esta línea se ace porque cuando chekeamos un cuadro y ponemos un valos de precio y pasamos a otro cuadro para chekaerlo borra el anterior por la línes que tenmos acontinuación.
                cuadro_bebida[x].delete(0, END)# se va el cero cuando checkeamos el cuadro
            cuadro_bebida[x].focus()# focus cuando ckeamos el cuadro el cursor aparezca en el espcaio para llenar 
        else: # cuado no este chekeado vuleva aprecer el cero
            cuadro_bebida[x].config(state=DISABLED) 
            texto_bebida[x].set('0')   
        x +=1  

    x = 0
    for c in cuadro_postre:
        if variables_postre[x].get() == 1:
            cuadro_postre[x].config(state=NORMAL)
            if cuadro_postre[x].get() == '0':# esta línea se ace porque cuando chekeamos un cuadro y ponemos un valos de precio y pasamos a otro cuadro para chekaerlo borra el anterior por la línes que tenmos acontinuación.
                cuadro_postre[x].delete(0, END)# se va el cero cuando checkeamos el cuadro
            cuadro_postre[x].focus()# focus cuando chekeamos el cuadro el cursor aparezca en el espcaio para llenar 
        else: # cuado no este chekeado vuleva aprecer el cero
            cuadro_postre[x].config(state=DISABLED) 
            texto_postre[x].set('0')   
        x +=1  

# función total para el boton total
def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1
    print(sub_total_postre)  

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 2)}')
    var_costo_subtotal.set(f'$ {round(sub_total, 2)}')
    var_costo_impuesto.set(f'$ {round(impuestos, 2)}')
    var_costo_total.set(f'$ {round(total, 2)}')

# Función recibo o ticket
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}' 
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n') 
    texto_recibo.insert(END, f'*' * 63 + '\n')  
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

    # buscar la cantidad de cada producto para los item
    x = 0
    for comida in texto_comida:
        if comida.get() !='0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                f'${int(comida.get()) * precios_comida[x]}\n')
        x += 1                                
    
    x = 0
    for bebida in texto_bebida:
        if bebida.get() !='0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                f'${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1                                
    
    x = 0
    for postre in texto_postre:
        if postre.get() !='0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                f'${int(postre.get()) * precios_postres[x]}\n')
        x += 1   

    texto_recibo.insert(END, f'-' * 75 + '\n')    
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')  
    texto_recibo.insert(END, f' Sub-Total: \t\t\t{var_costo_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_costo_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_costo_total.get()}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n') 
    texto_recibo.insert(END, 'Lo Esperamos Pronto')

# Función Guardar
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')#filedialog.asksaveasfile que se guarde como un archivo
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')

# Función resetear
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    # hacer que el cuadro quede desactivado
    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)     
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)     
    for cuadro in cuadro_postre:
        cuadro.config(state=DISABLED)     

    # hacer que se desactive el chek del cuadro
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    # hacer que se borren los cuadros de subtotal, impuestos, total todos los de abajo
    var_costo_comida.set('')    
    var_costo_bebida.set('')    
    var_costo_postre.set('')    
    var_costo_subtotal.set('')    
    var_costo_impuesto.set('')    
    var_costo_total.set('')    
    
# Iniciar tkinter

aplicacion = Tk()

# Tamaño de la ventana 1020*630 tamaño de la ventana Y 0 0 son los ejes donde va aparecer la ventana
aplicacion.geometry('1130x630+0+0')

# evitar maximizar la pantalla 0 , 0 para evitar que se maximice en los ejes x y y el boton de masimizar queda desalilitado
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

# Color de fondo de la ventana
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT ) # bd es el borde y relieve es como para darle algo de trimencionalidad hay 5 opciones para este ejemplo ponemos FLAT
panel_superior.pack(side=TOP)# Llamamos a panel superior para que se visualice y lo ponemos arriba con slide =TOP
                             # Pero todavia no se puede visualizar porque no tiene contenido.

# Etiqueta titulo panael superior
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=20)

etiqueta_titulo.grid(row=0, column=0) #grid quiere decir  cuadricula por eso reow = 0 y column = 0                        

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos va dentro del panel izquierdo
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=40)
panel_costos.pack(side=BOTTOM)

#Panel comida va también dentro del panel izquierdo
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                            bd=1, relief=FLAT, fg='azure4')# bold es color negrita y fg color de letra
panel_comidas.pack(side=LEFT)  

#Panel bebidas va también dentro del panel Izquierdo
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                            bd=1, relief=FLAT, fg='azure4')# bold es color negrita y fg color de letra
panel_bebidas.pack(side=LEFT) 

#Panel postres va también dentro del panel Izquierdo
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                            bd=1, relief=FLAT, fg='azure4')# bold es color negrita y fg color de letra
panel_postres.pack(side=LEFT)

# Vamos a crear el panel de la derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT) 
panel_derecha.pack(side=RIGHT)     

# Panel calculadora va dentro panel derecha
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')#bg es color de fondo es backgroud
panel_calculadora.pack()# Aca no ponemos nada dentro de los parantices poruqe si no se pone nada ve pone arriba lo asume asi

# Panel recibo va dentro panel derecha
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones va dentro panel derecha
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista de productos para poder ya visualizar lo que esta dentro del panel izquierdo
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Pastas', 'Pizza', 'Carnes', 'Hambuerguesa', 'Sopas']

lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Cola', 'Vino', 'Cerveza', 'Refajo', 'Tinto']

lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Pastel1', 'Pastel2', 'Pastel3']

#generar items comida
variables_comida = []
cuadro_comida = []
texto_comida = []

#Cargar los nombres de estas listas dentro de los paneles de comida, bebidas y postres
contador = 0
for comida in lista_comidas:

    #Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()# aca con IntVar lo que hacemos es que cada elemento que se agrega se transforme un un valor Intero
    comida = Checkbutton(panel_comidas,
                        text=comida.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue =1,
                        offvalue=0,
                        variable=variables_comida[contador],
                        command=revisar_check)

    comida.grid(row=contador, column=0, sticky=W)# sticky=W se justifique a la izquierda simpre
    
    # Crear los cuadros de entrada
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()# para que en el cuadro apararezca 0
    texto_comida[contador].set('0')

    cuadro_comida[contador] = Entry(panel_comidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,# qUIERE DECIR DESACTIVADO EL CUADRO HASTA QUE SE ACTIVE EL CHECKBOOT
                                    textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador,
                                 column=1)                                    


    contador +=1

#generar items bebidas
variables_bebida = []
cuadro_bebida = []
texto_bebida = []

#Cargar los nombres de estas listas dentro de los paneles de comida, bebidas y postres
contador = 0
for bebida in lista_bebidas:

    
    #Crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()# aca con IntVar lo que hacemos es que cada elemento que se agrega se transforme un un valor Entero
    bebida = Checkbutton(panel_bebidas,
                        text=bebida.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue =1,
                        offvalue=0,
                        variable=variables_bebida[contador],
                        command=revisar_check)

    bebida.grid(row=contador, column=0, sticky=W)# sticky=W se justifique a la izquierda simpre

    # Crear los cuadros de entrada
    cuadro_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()# para que en el cuadro apararezca 0
    texto_bebida[contador].set('0')
    cuadro_bebida[contador] = Entry(panel_bebidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,# qUIERE DECIR DESACTIVADO EL CUADRO HASTA QUE SE ACTIVE EL CHECKBOOT
                                    textvariable=texto_bebida[contador])  

    cuadro_bebida[contador].grid(row=contador,
                                 column=1)   

    contador +=1    

#generar items postres
variables_postre = []
cuadro_postre = []
texto_postre = []

#Cargar los nombres de estas listas dentro de los paneles de comida, bebidas y postres
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()# aca con IntVar lo que hacemos es que cada elemento que se agrega se transforme un un valor Entero
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue =1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)

    postre.grid(row=contador, column=0, sticky=W)# sticky=W se justifique a la izquierda simpre

       # Crear los cuadros de entrada
    cuadro_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()# para que en el cuadro apararezca 0
    texto_postre[contador].set('0')
    cuadro_postre[contador] = Entry(panel_postres,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,# qUIERE DECIR DESACTIVADO EL CUADRO HASTA QUE SE ACTIVE EL CHECKBOOT
                                    textvariable=texto_postre[contador])

    cuadro_postre[contador].grid(row=contador,
                                 column=1)                                    

    contador +=1  

#Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal= StringVar()
var_costo_impuesto = StringVar()
var_costo_total = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text = 'Costo Comida',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',# solo lectura
                           textvariable= var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text = 'Costo Bebida',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_bebida.grid(row=1, column=0, padx=41)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',# solo lectura
                           textvariable= var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos,
                              text = 'Costo Postre',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_postre.grid(row=2, column=0, padx=41)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',# solo lectura
                           textvariable= var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx=41)


etiqueta_subtotal = Label(panel_costos,
                              text = 'Costo Subtotal',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_subtotal.grid(row=0, column=2, padx=41)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',# solo lectura
                           textvariable= var_costo_subtotal)

texto_subtotal.grid(row=0, column=3)

etiqueta_impuesto = Label(panel_costos,
                              text = 'Costo Impuestos',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',# solo lectura
                           textvariable= var_costo_impuesto)

texto_impuesto.grid(row=1, column=3)

etiqueta_total = Label(panel_costos,
                              text = 'Costo Total',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',# solo lectura
                           textvariable= var_costo_total)

texto_total.grid(row=2, column=3)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text= boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg= 'white',
                   bg= 'azure4',
                   bd=1,
                   width=7)

    botones_creados.append(boton) 

    boton.grid(row=0,
               column=columnas) 
    columnas +=1   

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)# para el recibo y verlos en panatalla
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)


# Area de recibo
texto_recibo = Text(panel_recibo,
                     font=('Dosis', 12, 'bold'),
                     bd=1,
                     width=42,
                     height=10)
texto_recibo.grid(row=0,
                  column=0)  

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)# columnspan para ampliar la columna

# loop para crear los botones calculadora
botones_calculadora =['7', '8', '9', '+', '4', '5', '6', '-',
                      '1', '2', '3', 'x', 'R', 'B', '0', '/']

botones_guardados = []

fila = 1 # ezpieza en 1 por que la pocicsion 0 ya esta ocupada por el visor de la calculadora
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)  
    botones_guardados.append(boton)                    
    boton.grid(row=fila,
               column=columna)    

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command =lambda : click_boton('7'))        
botones_guardados[1].config(command =lambda : click_boton('8'))        
botones_guardados[2].config(command =lambda : click_boton('9'))        
botones_guardados[3].config(command =lambda : click_boton('+'))        
botones_guardados[4].config(command =lambda : click_boton('4'))        
botones_guardados[5].config(command =lambda : click_boton('5'))        
botones_guardados[6].config(command =lambda : click_boton('6'))        
botones_guardados[7].config(command =lambda : click_boton('-'))        
botones_guardados[8].config(command =lambda : click_boton('1'))        
botones_guardados[9].config(command =lambda : click_boton('2'))        
botones_guardados[10].config(command =lambda : click_boton('3'))        
botones_guardados[11].config(command =lambda : click_boton('*'))        
botones_guardados[12].config(command =obtener_resultado)       
botones_guardados[13].config(command =borrar)       
botones_guardados[14].config(command =lambda : click_boton('0'))        
botones_guardados[15].config(command =lambda : click_boton('/'))        
        
                                    

# evitar que la pantalla se cierre
aplicacion.mainloop()