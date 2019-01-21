## program to display Gratuity and Sub Total

subTotal = eval(input("Enter Subtotal : "))
gratuity = eval(input("Enter the gratuity  :"))


gratuity = int(subTotal * 15) / 100
print(gratuity)
total = gratuity + subTotal;
print(total)
