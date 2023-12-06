def calculate_leap_year(input_leap_year):
    if(input_leap_year % 4 == 0):
        if(input_leap_year % 100 != 0):
            return True