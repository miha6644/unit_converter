print("Hello! I'm the unit converter 66. I convert kilometres to miles.")

kilometres = float(input("Please enter the number of kilometres you'd like to convert: "))
print(kilometres * 0.62137)

while True:
    loop = input("Do you want to do another conversion? Please answer with 'Yes' or 'No': ")

    if loop.lower() == "yes":
        kilometres = float(input("Please enter the number of kilometres you'd like to convert: "))
        print(kilometres * 0.62137)

    if loop.lower() == "no":
        print("Goodbye!")
        break
