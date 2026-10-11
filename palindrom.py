number=int(input("enter the number:"))
revers = 0
original_num = number
while(number > 0):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
if(original_num == reverse):
    print("number is palindrome...!")
else:
    print("not a palindrome...!")    