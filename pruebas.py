width = 4
height= 3

boardOut = [["*" for i in range(width)] for j in range(height)]

num = 1
print("  " , end='')
for i in range(1 , width + 1):
        print(i , end="  ")
print("")
for i in boardOut:
    print( num , end=" ")
    num+=1
    for j in i:
        print(j , end="  ")
    print()
