highest = 0
lowest = 0
s = []
for i in range (6):
    score = int (input("enter performan score:"))
    s.append (score)
    if score >=80:
        print ("excellent")
    elif score >=60:
        print("good")
    elif score >=40:
        print ("average") 
    else:
        print("poor")
        for score in 5:
            if score > highest:
              if score < lowest:
                  lowest = score
                  print("highest score:",highest)
                  print("lowest score:",lowest)




