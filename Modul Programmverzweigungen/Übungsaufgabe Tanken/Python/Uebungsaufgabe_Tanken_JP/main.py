def calculate_cost(fuel_amount,fuel_cpl):
    calculated_cost = 0
    if fuel_amount > 0:
        if fuel_amount >= 100:
            calculated_cost = round((fuel_amount * fuel_cpl)-(fuel_amount * fuel_cpl * 5 / 100), 2)
            return calculated_cost
        calculated_cost = round(fuel_amount * fuel_cpl, 2)
        return calculated_cost

try:
    fuel_amount = int(input('Fuel Amount (in l) >>> '))
    selected_fuel_sort = int(input('Which Fuel do you want to buy?\n\n1 - Disel\n2 - Fuel2\n\n>>> ')) 
except:
    print('No valid input')
    quit()

if selected_fuel_sort == 1:
    fuel_cpl = 3
elif selected_fuel_sort == 2:
    fuel_cpl = 2
else:
    print('We dont have this fuel sort!')
    quit()

print(f'To buy {fuel_amount}L it will cost you {str(calculate_cost(fuel_amount,fuel_cpl))}€')