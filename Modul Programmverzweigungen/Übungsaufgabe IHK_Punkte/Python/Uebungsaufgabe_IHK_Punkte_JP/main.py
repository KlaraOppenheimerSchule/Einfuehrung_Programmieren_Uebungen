def get_grade_by_points(points):
    #Quelle: https://1a-pruefung.de/wp-content/uploads/2017/11/notenschluessel.png
    if points > 5:
        if points <= 11 and points > 5:
            return 5.9
        elif points <= 16 and points >= 12:
            return 5.8
        elif points <= 22 and points >= 17:
            return 5.7
        elif points <= 28 and points >= 23:
            return 5.6
        elif points == 29:
            return 5.5
        elif points == 30 or points == 31:
            return 5.4
        elif points == 32 or points == 33:
            return 5.3
        elif points == 34 or points == 35:
            return 5.2
        elif points == 36 or points == 37:
            return 5.1
        elif points == 38 or points == 39 or points == 40:
            return 5.0
        elif points == 41 or points == 42:
            return 4.9
        elif points == 43 or points == 44:
            return 4.8
        elif points == 45 or points == 46:
            return 4.7
        elif points == 47 or points == 48:
            return 4.6
        elif points == 49:
            return 4.5
        elif points == 50 or points == 51:
            return 4.4
        elif points == 52 or points == 53:
            return 4.3
        elif points == 54:
            return 4.2
        elif points == 55 or points == 56:
            return 4.1
        elif points == 57 or points == 58:
            return 4.0
        elif points == 59 or points == 60:
            return 3.9
        elif points == 61:
            return 3.8
        elif points == 62 or points == 63:
            return 3.7
        elif points == 64:
            return 3.6
        elif points == 65:
            return 3.5
        # 66 fehlt auf der Seite
        elif points == 66 or points == 67:
            return 3.4
        elif points == 68 or points == 69:
            return 3.3
        elif points == 70:
            return 3.2
        elif points == 71 or points == 72:
            return 3.1
        elif points == 73:
            return 3.0
        elif points == 74 or points == 75:
            return 2.9
        elif points == 76:
            return 2.8
        elif points == 77 or points == 78:
            return 2.7
        elif points == 79:
            return 2.6
        elif points == 80:
            return 2.5
        elif points == 81:
            return 2.4
        elif points == 82:
            return 2.3
        elif points == 83:
            return 2.2
        elif points == 84:
            return 2.1
        elif points == 85 or points == 86:
            return 2.0
        elif points == 87:
            return 1.9
        elif points == 88:
            return 1.8
        elif points == 89:
            return 1.7
        elif points == 90:
            return 1.6
        elif points == 91:
            return 1.5
        elif points == 92 or points == 93:
            return 1.4
        elif points == 94 or points == 95:
            return 1.3
        elif points == 96 or points == 97:
            return 1.2
        elif points == 98 or points == 99:
            return 1.1
        elif points >= 100:
            return 1.0
        else:
            return 0.0
    else:
        return 6.0
    
try:
    points = int(input('How many Points did you achieve?\n>>> '))
except ValueError:
    print('Please only input Integers!')
    quit()

grade = get_grade_by_points(points)
if grade != 0.0:
    print(f'With {points} Points you would achieve the Grade: {grade}')
else:
    print('Invalid Points')