def add(x,y):
    return x+y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print (" 1: add"
     " 2: subtract"
      "3: multiply"
      "4: divide"
      )
while True:
   choice = input("select your choice: ")
   if choice in('1', '2', '3', '4'):
       try:
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
       except ValueError:
          print("invalid choice")
          continue
       if choice == '1':
          print(num1, "+" ,num2, "=", add(num1, num2)) 
       elif choice == '2':
          print(num1, "-", num2, "=", subtract(num1, num2))
       elif choice == '3':
          print(num1, "*", num2, "=", multiply(num1, num2))
       elif choice == '4':
          print(num1, "/", num2, "=", divide(num1, num2))
       else:
          print("invalid input")

       next_calculation = input("try again?(yes/no)")
       if next_calculation == "no":
        break
   else:
       print("invalid inputt")


    
    






