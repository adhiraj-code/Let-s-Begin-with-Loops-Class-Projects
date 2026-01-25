medical = input("Do you have a medical certificate? Enter Y or N : ")

if medical == "N":
    print("You are not eligible for the exam")

else:
    print("You are eligible for the exam")

    attendance = int(input("Enter the attendance percentage : "))

    if attendance >= 75:
        print("You are allowed to take the exam")

    else:
        print("You are not allowed to take the exam")