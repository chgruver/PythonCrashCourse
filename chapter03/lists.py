bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

# Replace 'honda' in the list with 'ducati'
motocycles[0] = 'ducati'
print(motocycles)

# Add 'honda' back to the list at the end
motocycles.append('honda')
print(motocycles)

motorcycles2 = []

motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')

print(motorcycles2)

motorcycles2.insert(0, 'ducati')
print(motorcycles2)

del motorcycles2[0]
print(motorcycles2)

last_owned = motorcycles2.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

cars = ['bmw', 'audi', 'toyota', 'subaru', 'honda']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)