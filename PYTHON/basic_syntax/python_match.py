

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("It's the weekend")
    

month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print('A weekday in april!')
   
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print('A weekday in may')
    case _:
        print('No match!')