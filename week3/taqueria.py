
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cart = {
}
price = 0
#  create program that enable to place order
while True:
  try :
      order = input("Item: ").strip().title()
      # if order not in menu:
      price += menu[order]
      #     pass
  except EOFError:
      print("")
      break
  except:
      pass
  else:
      # for order in menu:
          # price = menu[order]
          # cart.update({order:price})
      print(f"Total: ${price:.2f}")
    
# for items until user input control-d which end input loop7u88io
    
      