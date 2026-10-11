total_days = int(input("enter total days of working: "))
present_days = int(input("enter present days:"))
absent_days = total_days - present_days 
attendance_percentage = (present_days/total_days)*100
print("present_days:" ,present_days)
print("Absent_days:" ,absent_days)
print("attendance_percentage:" ,attendance_percentage)

if attendance_percentage >= 75:
    print("employee is eligible for bonus:")
else:
    print("employee is not eligible for bonus:")