userName = input("UserName : ")
passWord = input("Password : ")
if userName == "Puenx" and passWord == "271246":
    print("Success!")
    print("Welcome to HarryPotter Book Store")
    print("---------------------------------")
    print("1. Harry Potter______________220 THB")
    print("2. Chamber of Secrets________250 THB")
    print("3. Prisoner of Azkaban_______300 THB")
    book = int(input("Please select the book number :"))
    if book == 1:
            quantity = int(input("quantity :"))
            total = quantity*220
            print("total :",total,"THB")
    if book == 2:
            quantity = int(input("quantity :"))
            total = quantity*250
            print("total :",total,"THB")
    if book == 3:
            quantity = int(input("quantity :"))
            total = quantity*300
            print("total :",total,"THB")
else:
    print("Error")

print("Thank You")

