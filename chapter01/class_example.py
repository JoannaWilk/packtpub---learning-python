class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")


# create a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the objects we have, instances of the Bike class.
print("The red bike colour is: ", red_bike.colour)
print("The red bike frame material is: ", red_bike.frame_material)
print("The blue bike colour is: ", blue_bike.colour)
print("The blue bike frame material is: ", blue_bike.frame_material)

# let's brake!
red_bike.brake()
