import backend as be

def frontend():
    year = int(input("Year: "))
    print(f"Yes, {year} is a leap year") if be.is_leap_year(year) else print(f"No, {year} is not a leap year.")

frontend()