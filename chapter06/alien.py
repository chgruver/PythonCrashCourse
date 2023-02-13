alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_1['x_position']}")

# Move the alien to the right
# Determine how far to move the alienbased on its current speed.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
    
# The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New position: {alien_1['x_position']}")