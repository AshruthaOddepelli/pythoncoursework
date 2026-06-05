products={
    'laptop':0,
    'mouse':10,
    'charger':5,
    'phone':30,
    'keyboard':0
    }
product = input("enter the product: ")
if product in products:
        if products[product]!=0:
            print(f"you can buy{product}!!")
        else:
            print(f"{product} is out of stock")
else:
    print(f"{product} is not avaliable")
              
