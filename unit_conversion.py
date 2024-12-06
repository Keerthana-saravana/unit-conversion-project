#project unit conversion 
def meters_to_feet(meters):
    return meters*3.28084
def feet_to_meters(feet):
    return feet/3.28084
def pounds_to_kilogram(kg):
    return kg/2.20462
def kilogram_to_pounds(pounds):
    return pounds*2.20462
def celcius_to_farenheat(F):
    return (F*9/5)+32
def farenheat_to_celcius(c):
    return (c-32)*5/9

#getting name of the user 
name=input("enter your name:")
print(f"welcome {name} to my unit conversion program!!")
def display_menu():
    
   
    #declaring the options available in the program
    print("\nThe following options are available:")
    print("1.convert from meters to feet and vice versa ")
    print("2.convert from pounds to kilogram and vice versa")
    print("3.convert from celcius to farenheat and viceversa")
    print("4.exit")

while True:
    display_menu()
    #getting input as choice from the user
    choice=input("enter your choice to proceed:")

    if choice=='1':
        print("\nlength conversion:")
        print("a.meters to feet")
        print("b.feet to meters")
        sub_choice=input("enter your choice (a/b):")
        if sub_choice=="a":
            length=float(input("enter the length in meters:"))
            print(f"{length} meters is equal to {meters_to_feet(length)} feet.")
        elif sub_choice=="b":
            length=float(input("enter the lenght in feet:"))
            print(f"{length} feet is equal to {meters_to_feet(length)} meters.")
        else:
            print("invalid choice!,enter the valid choice")
    elif choice=='2':
        print("\nweight conversion:")
        print("a.pounds to kilogram")
        print("b.kilogram to pounds")
        sub_choice=input("enter your choice (a/b):").lower()
        if sub_choice=="a":
            weight=float(input("enter the weight in pounds:"))
            print(f"{weight} pounds is equal to {pounds_to_kilogram(weight)} kilogram.")
        elif sub_choice=="b":
            weight=float(input("enter your weight in kilogram:"))
            print(f"{weight} kilogram is equal to {kilogram_to_pounds(weight)} pounds.")
        else:
            print("invalid choice!,enter the valid choice")
    elif choice=='3':
        print("\ntemperature conversion:")
        print("a.celcius to farenheat")
        print("b.farenheat to celcius")
        sub_choice=input("enter your choice (a/b):").lower()
        if sub_choice=="a":
            temp=float(input("enter the temperature in celcius:"))
            print(f"{temp} celcius is equal to {celcius_to_farenheat(temp)} farenheat.")
        elif sub_choice=="b":
            temp=float(input("enter your choice (a/b):")).lower()
            print(f"{temp} farenheat is equal to {farenheat_to_celcius(temp)} celcius. ")
        else:
            print("invalid choice!,enter the valid choice")
    elif choice=='4':
        print("Thank you for using my unit conversion!")
        print("Good bye!!")
        break
    else:
        print("invalid choice !,try again later!!")
