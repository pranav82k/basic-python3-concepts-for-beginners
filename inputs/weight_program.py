weight = float(input("Please enter your weight "))
unit = input("Please unit as (K)g or (L)bs ").upper()

if unit == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

