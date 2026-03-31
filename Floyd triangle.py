rows = int(input("Please enter the total number of rows: "))

number = 0

print("Floyd's Triangle")

for i in range(1, rows + 1):
    
    for j in range(1, i + 1):
        
        print(number, end = ' ')
       
        number = number + 10
    
    print()