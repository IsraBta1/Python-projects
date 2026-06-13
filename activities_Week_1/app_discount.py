"""
Student: Israel Betancourt
Course 111 Programming with functions
"""
from datetime import datetime                   # take a note of this
DISCOUNT_DAYS = [0, 1, 2, 3, 4]                 # Monday to friday
DISCOUNT_RATE = 0.1                             # 10% DISCOUNT
TAX_RATE = 0.06                                 # 0.06 DISCOUNT IS 6% DISCOUNT


"""Datetime"""
today = datetime.now()                          # take a note of this
dow = today.weekday()

"""Loop in python is while in spanish es ciclo con un finito de respiestas."""
subtotal = 0.0
quantity = 1
while quantity !=0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:                               # es necesario ponerlo porque de alli las demas input y string podra hacer su trabajo en funciones
        price = float(input("Enter the price: "))
        subtotal += quantity * price                # multiplicacion de cantidad por precio del producto

"""Subtotal"""
print (f"Total order {subtotal:.2f}")
discount = 0.0                                   # valor del descuento inicial

"""Conditional of the week"""
if dow in DISCOUNT_DAYS:
    if subtotal >= 50:                           # conditional mora than 50
        discount = round(subtotal * DISCOUNT_RATE, 2)    ## round(subtotal * DISCOUNT_RATE,2) ES PARA DECIMALES DE FORMA DIRECTA LA PONE EN 2 DECIMALES
        print (f"Discount {discount:.2f}")
    else:
        short = 50 - subtotal
        print(f"You can get a discount by ordering {short:.2f} more. ")

subtotal -= discount  
tax = round(subtotal * TAX_RATE, 2)                      ## round(subtotal * TAX_RATE) ES PARA DECIMALES DE FORMA DIRECTA LA PONE EN 2 DECIMALES
total = subtotal + tax

print (f"Tax {tax:.2f}")                        ### Es la forma mas facil y rapida de poner los decimales de 2 digit after of comma.
print (f"Total Due {total:.2f}")

"""
    Investigar mas sobre como realizar descuentos con ciclos con finidad.
    Para tener un parametro ya previsto para futuras oportunidades.
    Aprender un poco de contabilidad de inpuesto sobre la renta y porcentajes al cambio para traducirlo a codigo.
"""