name=input("Enter your Name: ")
current_year=int(input("Enter the Cuurent Year:  "))


born_year=int(input("Enter the Year of birth:  "))
age=current_year-born_year
print(name,"Your age is ",age)

find=int(input("After How many years i will turn:" ))
future_age=find-age
print("After",future_age,"years you will turn",find)