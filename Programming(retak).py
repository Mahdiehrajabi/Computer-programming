# first step, install these libraries

import pandas as pd
import matplotlib.pyplot as plt

#first section (energy usage)
Elec_Bill = []
months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
elecBill = int(input("what is your average monthly electricity bill in euoros? "))
gasBill = int(input("what is your average monthly natural gas bill in euoros? "))
fuelBill = int(input("what is your average monthly fuel bill for transportation in euoros? "))
result1 = (elecBill*12*0.0005) + (gasBill*12*0.0053) + (fuelBill*12*2.32)
print (result1)



Month = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

table = {'Month':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'],
         'Electricity':elecBill,
         'Gas':gasBill,
         'Fuel':fuelBill,
         'Total':result1
         }
Total=pd.DataFrame(table)
print(Total)

#use the pandas library and the to_excel() function for transition to excel file
Total.to_excel("energ_amount.xlsx")


#seccond section (waste)
Waste = []
months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
waste = int(input("how much waste do you generate per month in kilograms? "))
recycled = int(input("how much of that waste is recycled ? "))
print((waste*12*0.57)-recycled)

table = {'Month':['January','Febuary','March','April','May','June','July','August','September','October','November','December'],
         'Waste Generated': Waste,
         'Carbon Generated ':Total,
         }
Total2=pd.DataFrame(table)
print(Total2)

Total2.to_excel("Waste_amount.xlsx")


#third section (business travel)
kilometersOfTravel= int(input("How many kilometers do your employees travel per year for business purposes ? "))
fuelEfficiency =  int(input("what is the averange fuel efficiency of the vehicles used for business travel in liters per 100 kilometers ? "))
total=  kilometersOfTravel * (1/fuelEfficiency) * 2.31
print(f"the result is:{Total} ")

Total.to_excel("Travel_amount.xlsx")


#show table with year and travel
plt.figure("Per year - kilometersOfTravel",figsize=[12,6])
plt.title("Per year - Travel")
plt.xlabel('year')
plt.ylabel('Travel')
plt.show()


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
