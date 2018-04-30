class DriverException(Exception):
    pass


# commented lines work if we comment 'else:'

people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
# driver = None
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break

# if driver is None:
else:
    raise DriverException('Driver not found.')