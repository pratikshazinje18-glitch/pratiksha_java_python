age = int(input("enter age: "))
monthly_income = float(input("enter monthly income:"))
ceedit_score = int(input("entercredit score:"))
existing_loan = float(input("enter existing loan amount: "))
employment_years = float(input("enter employment years: "))

if age < 21:
    print("loan status: rejected")
    print("reason: age below 21:")

elif monthly_income < 30000:
    print("loan status: rejected")
    print("reason: monthly income below 30,000")
elif credit_score < 700:
    print("loan status: rejected")
    print("reason: employment less than 2 years")

elif existing_loan > 200000:
    print("loan status: rejected")
    print("reason: existing loan exceeds 200000")
else:
    interest =  "normal interest"      
    risk = "medium" 
if existing_loan == 0
   processing ="narmal processing"
else:
    processing = "additional verification"
print("loan status: approved")
print("risk level:", rick)
print("interest category:", 
      interest)
print("processing:", proccessing)       
