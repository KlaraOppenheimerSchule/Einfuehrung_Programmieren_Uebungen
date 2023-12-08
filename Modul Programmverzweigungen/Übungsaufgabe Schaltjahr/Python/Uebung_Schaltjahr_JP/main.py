from leap_year import calculate_leap_year as cly

try:
    input_leap_year = int(input('Enter Year >>> '))
except ValueError:
    print('Please enter a valid year!')
    quit()

try:
    is_leap_year = cly(input_leap_year)
except:
    print('Error while calculating leap year status!')
    quit()

if is_leap_year:
    print(f'\nThe year: {input_leap_year} IS a leap year!')
else:
    print(f'\nThe year: {input_leap_year} IS NOT a leap year!')