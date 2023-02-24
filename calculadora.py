from tkinter import *
from tkinter import ttk

#Cores

black = "#1e1f1e" 
white = "#feffff"
blue = "#38576b"
gray = "#ECEFF1"
orange = "#FFAB40"

#Configuração da Janela e Frames
janela = Tk()
janela.title("CalculadoraPY")
janela.geometry("235x310")
janela.config(bg=black)

frame1 = Frame(janela, width=300, height=50, bg=blue) #Display
frame1.grid(row=0, column=0)

frame2 = Frame(janela, width=300, height=300) #Botões
frame2.grid(row=1, column=0)


allValues = ''
valortxt = StringVar()

def valoresOnClick(botao):

    global allValues

    allValues = allValues + str(botao)

    valortxt.set(allValues)

def calcular():
    try:
        global allValues
        allValues = allValues.replace('x','*')
        allValues = allValues.replace('÷', '/')

        resultado = eval(allValues)
    
        valortxt.set(str(resultado))
    except SyntaxError:
        valortxt.set('Operação Inválida')
    except ZeroDivisionError:
        valortxt.set('Impos. dividir por 0')
  
def limparDisplay():

    global allValues

    allValues = ''
    valortxt.set('')

#Criação da Label


appLabel = Label(frame1, textvariable=valortxt, width=16, height=2, padx=6, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=blue, fg=white)
appLabel.place(x=0, y=0)

#Criação de botões

#Linha 01
b1 = Button(frame2, command = limparDisplay ,text = 'C', width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0,y=0)

b2 = Button(frame2, command= lambda: valoresOnClick('%'), text = '%', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=0)

b3 = Button(frame2, command= lambda: valoresOnClick('÷'),text = '÷', width=5, height=2, bg=orange,fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177,y=0)

#Linha 02
b4 = Button(frame2, command= lambda: valoresOnClick('7'),text = '7', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0,y=52)

b5 = Button(frame2, command= lambda: valoresOnClick('8'),text = '8', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59,y=52)

b6 = Button(frame2, command= lambda: valoresOnClick('9'),text = '9', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118,y=52)

b7 = Button(frame2, command= lambda: valoresOnClick('x'),text = 'x', width=5, height=2, bg=orange,fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177,y=52)

#Linha 03
b8 = Button(frame2, command= lambda: valoresOnClick('4'),text = '4', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0,y=104)

b9 = Button(frame2, command= lambda: valoresOnClick('5'),text = '5', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59,y=104)

b10 = Button(frame2, command= lambda: valoresOnClick('6'),text = '6', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118,y=104)

b11 = Button(frame2, command= lambda: valoresOnClick('-'),text = '-', width=5, height=2, bg=orange,fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177,y=104)

#Linha 04
b12 = Button(frame2, command= lambda: valoresOnClick('1'),text = '1', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0,y=156)

b13 = Button(frame2, command= lambda: valoresOnClick('2'),text = '2', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59,y=156)

b14 = Button(frame2, command= lambda: valoresOnClick('3'),text = '3', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118,y=156)

b15 = Button(frame2, command= lambda: valoresOnClick('+'),text = '+', width=5, height=2, bg=orange,fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177,y=156)

#Linha 05
b16 = Button(frame2, command= lambda: valoresOnClick('0'),text = '0', width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0,y=208)

b17 = Button(frame2, command= lambda: valoresOnClick('.'),text = '.', width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118,y=208)

b18 = Button(frame2, command = calcular ,text = '=', width=5, height=2, bg=orange,fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177,y=208)

janela.mainloop()