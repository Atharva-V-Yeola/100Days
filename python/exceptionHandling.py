# divide(4, 2) will return 2 and print Division Complete
# divide(4, 0) will print error and Division Complete
# Finally block will be executed in all cases

def divide(a, denominator):
    try:
        return a/denominator
    except ZeroDivisionError as e:
        print('Divide by Zero!! Terminated')
    finally:
        print('Divsion Complete.')

divide(3,1)