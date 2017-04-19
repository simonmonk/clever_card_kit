from guizero import *
import RPi.GPIO as GPIO
import SimpleMFRC522


reader = SimpleMFRC522.SimpleMFRC522()

app = App(title="Money Box", layout="grid", width=350, height=170)
    
def read_tag():
    id, text = reader.read()
    if id:
        values = text.split("/")
        name_field.set(values[0])
        balance_field.set(values[1])
        
def write_tag():
    name = name_field.get()
    balance = float(balance_field.get())
    adjustment = float(adjustment_field.get())
    balance += adjustment
    
    text = name + "/" + str(balance)
    reader.write(text)
    balance_field.set(str(balance))
    adjustment_field.set("0")
            
PushButton(app, text="SCAN", command=read_tag, align="left", grid=[0,0])

Text(app, text="Name", align="left", grid=[1,0])
name_field = TextBox(app, text="-", align="left", width=20, grid=[1,1])
Text(app, text="Balance", align="left", grid=[2,0])
balance_field = TextBox(app, text="", align="left", width=10, grid=[2,1])
Text(app, text="Amount to + or -", align="left", grid=[4,0])
adjustment_field = TextBox(app, text="0", align="left", width=10, grid=[4,1])

PushButton(app, text="SAVE", command=write_tag, align="left", grid=[5,0])

app.display()