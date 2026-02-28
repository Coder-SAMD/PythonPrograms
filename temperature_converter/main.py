#Learning to code with version control systems!
print("Hello Git and GitHub!!")
#Program to convert temperature from degree Fahrenheit to degree Celsius
def f2c():
    fahrenheit1,fahrenheit2 = eval(input("Enter 2 temperatures in degree Fahrenheit, separated by a comma: "))
    celsius1 , celsius2 = (fahrenheit1-32)*(5/9) , (fahrenheit2-32)*(5/9)
    print("The temperatures in degree celsius are: ",celsius1 , " ", celsius2)
def c2f():
    celsius1, celsius2 = eval(input("Enter 2 temperatures in degree celsius, separated by a comma: "))
    fahrenheit1, fahrenheit2 = (1.8*celsius1) + 32 , (1.8*celsius2) + 32
    print("The temperatures in degree fahrenheit are: ", fahrenheit1, " ", fahrenheit2)

print("This is a temperature converter.")
user_input = input("Press 1 for converting temperature from degree celsius to degree fahrenheit." +
                "\nPress 2 for converting temperature from degree fahrenheit to degree celsius.")

if user_input == "1":
    c2f()
elif user_input == "2":
    f2c()
else:
    print("Invalid input.Try again; Type the number 1 or 2.")
