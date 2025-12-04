ac=int(input("Enter the actual cost of item: "))
sc=int(input("Enter the selling cost of item: "))
if ac>sc:
    loss=ac-sc
    print("Loss is: ",loss)
elif sc==ac:
    ptint("No profit no loss")
else:
    profit=sc-ac
    print("profit is: ",profit)
