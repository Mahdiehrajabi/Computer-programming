#first section (energy usage)

elecBill = int(input("what is your average monthly electricity bill in euoros? "))
gasBill = int(input("what is your average monthly natural gas bill in euoros? "))
fuelBill = int(input("what is your average monthly fuel bill for transportation in euoros? "))
result1 = (elecBill*12*0.0005) + (gasBill*12*0.0053) + (fuelBill*12*2.32)
print (result1)

#seccond section (waste)

waste = int(input("how much waste do you generate per month in kilograms? "))
recycled = int(input("how much of that waste is recycled ? "))
print((waste*12*0.57)-recycled)

#third section (business travel)

kilometersOfTravel= int(input("How many kilometers do your employees travel per year for business purposes ? "))
fuelEfficiency =  int(input("what is the averange fuel efficiency of the vehicles used for business travel in liters per 100 kilometers ? "))
total=  kilometersOfTravel * (1/fuelEfficiency) * 2.31
print(f"the result is:{total} ")

def generate_report(total_emissions):
    print("----- Carbon Footprint Report -----")
    print("Total carbon emissions: {:.2f} kg CO2e".format(total))
    print("Suggestions to reduce carbon footprint:")

if total > 10 :
        print("- Reduce energy consumption by using energy-efficient appliances and turning off unused electronics and use less Elevators because consume electricity.")

        print("- Use eco-friendly transportation for your employees like walking, cycling, or carpooling , use public transportation.")
        print("- Keep your temperature system on a moderate setting while you’re in the room.")
        print("- Implement recycling trashes to minimize waste.")

else:
        print("- Great! Your carbon footprint is already low.")


