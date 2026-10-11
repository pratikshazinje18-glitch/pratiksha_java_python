balance=float(input("inter balance"))
amount=float(input("enter your amount"))
account=type=input("enter account type(saving/current)")
transaction_type=input("enter transaction type (withdrowal/deposit)")


   print("not allowed")

elif transaction_type == "deposit":
    balance = balance + amount
     print("balance:",balance)

 elif transaction_type =="withdraw")
      if amount > balance:
     print("transaction not allowed")
elif account_type =="saving"and balance<1000:
     print("tranasaction not allowed")
elif account_type =="current"and balance < 0:
     print ("not allowd")
else:
    balance = balance - ammount
   print ("new balance:,balance")