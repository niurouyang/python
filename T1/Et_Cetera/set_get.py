class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            raise ValueError("Radius cannot be negative.")

# Creating a Circle object
circle = Circle(5)

# Using the setter method to modify the 'radius' attribute
circle.radius = 10
print(circle.radius)  # Output: 10

# Trying to set an invalid radius
try:
    circle.radius = -5
except ValueError as e:
    print(e)  # Output: Radius cannot be negative.
