def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)
no1=eval(input("Enter the first number-> "))
no2=eval(input("Enter the second number-> " ))
print("select the option")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while(True):
    choice=int(input("Enter the choice from (1/2/3/4/5)-->"))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("Addition of two number",no1,"and",no2,"is-> ",add(no1,no2))
        elif choice==2:
            print("Subtraction of two number",no1,"and",no2,"is-> ",subtract(no1,no2))
        elif choice==3:
            print("Multiplication of two number",no1,"and",no2,"is-> ",multiply(no1,no2))
        elif choice==4:
            print("Division of two number",no1,"and",no2,"is-> ",divide(no1,no2))
        elif choice==5:
            print("Thank you:) ")
            exit()
    else:
             print("invalid choice try again")   

