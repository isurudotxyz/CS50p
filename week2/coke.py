import sys

amount_due = 50 
while True:
    print(f"Amount Due: {amount_due}")
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in [5,10,25]:
        amount_due -= inserted_coin
        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
            sys.exit()
