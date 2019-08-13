from guizero import *
import RPi.GPIO as GPIO
import SimpleMFRC522


reader = SimpleMFRC522.SimpleMFRC522()

app = App(title="Money Box", layout="grid", width=350, height=170)
    
def read_tag():
    id, text = reader.read()
    if id:
        values = text.split("/")
        if len(values) == 2:
            name_field.value = values[0]
            balance_field.value = values[1]
        
def write_tag():
    name = name_field.value
    balance = float(balance_field.value)
    adjustment = float(adjustment_field.value)
    balance += adjustment
    
    text = name + "/" + str(balance)
    reader.write(text)
    balance_field.value = str(balance)
    adjustment_field.value = "0"
            
PushButton(app, text="SCAN", command=read_tag, align="left", grid=[0,0])

Text(app, text="Name", align="left", grid=[0,1])
name_field = TextBox(app, text="-", align="left", width=20, grid=[1,1])
Text(app, text="Balance", align="left", grid=[0,2])
balance_field = TextBox(app, text="", align="left", width=10, grid=[1,2])
Text(app, text="Amount to + or -", align="left", grid=[0,3])
adjustment_field = TextBox(app, text="0", align="left", width=10, grid=[1,3])

PushButton(app, text="SAVE", command=write_tag, align="left", grid=[0,4])

try:
    app.display()
finally:
    print("cleaning up")
    GPIO.cleanup()
