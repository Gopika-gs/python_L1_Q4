num = int(input("Enter a number "))
list = []
for i in range( 1 ,num + 1):
    if num % i == 0:
        list.append(i)
print("The divisior of" , num , " are" , list)

