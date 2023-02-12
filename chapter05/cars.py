cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
print()
    
requested_toppings = ['mushrooms', 'extra cheese']

if 'anchovies' not in requested_toppings:
    print("Hold the anchovies")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!")