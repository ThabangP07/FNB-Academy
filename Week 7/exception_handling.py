try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
finally:
    print("Execution completed")
    

try:
    print(y)
except NameError:
    print("Variable y is not defined")
else:
    print("Everything went wrong")
    
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")