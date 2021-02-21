print("Hy, I convert km into miles")

while True:
    km = float(input("Please enter the value in km: "))

# conversion factor = 0.621371
    miles = km * 0.621371

    print("{0} km is {1} miles".format(km, miles))

    choice = input("Would you like to do another conversion (y/n)")
    if choice != "y":
        print("By,by")
        break
