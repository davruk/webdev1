print("Hy, I convert km into miles!")

while True:
    km = float(input("Please, enter the value in km: "))

# conversion factor = 0.62138
    miles = km * 0.62138
    print(f"{km} {miles}")

    user_convert_again = input("Would you like to do another conversion (y/n)")
    if user_convert_again != "y":
        print("By,by! Thank you!")
