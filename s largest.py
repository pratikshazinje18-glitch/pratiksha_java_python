marks=[17,20,25,21,23,40]
hmark=0
shmark=0
for i in marks:sz
    if i>hmark:
        shmark=hmark
        hmark=i
    elif i>shmark and i!=hmark:
        shmarks=i
print("the second highestis",shmark)            