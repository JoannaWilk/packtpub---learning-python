print("for number in [0, 1, 2, 3, 4]:\n"
      "    print(number)")
for number in [0, 1, 2, 3, 4]:
    print(number)

print("\nfor number in range(5):\n"
      "    print(number)")
for number in range(5):
    print(number)

print("\nlist(range(10)):\n",
      list(range(10)))

print("\nlist(range(3, 8)):\n",
      list(range(3, 8)))

print("\nlist(range(-10, 10, 4)):\n",
      list(range(-10, 10, 4)))

print("\n-------------------\n")

print("surnames = ['Rivest', 'Shamir', 'Adleman']\n"
      "for position in range(len(surnames)):\n"
      "    print(position, surnames[position])")
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(position, surnames[position])

print("\n-------------------\n")

print("surnames = ['Rivest', 'Shamir', 'Adleman']\n"
      "for position in range(len(surnames)):\n"
      "    print(surnames[position][0], end='')")
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(surnames[position][0], end='')

print("\n-------------------\n")

print("surnames = ['Rivest', 'Shamir', 'Adleman']\n"
      "for surname in surnames:\n"
      "    print(surname)")
surnames = ['Rivest', 'Shamir', 'Adleman']
for surname in surnames:
    print(surname)

print("\n-------------------\n")

print("surnames = ['Rivest', 'Shamir', 'Adleman']\n"
      "for position, surname in enumerate(surnames):\n"
      "    print(position, surname)")
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)

print("\n-------------------\n")

print("surnames = ['Rivest', 'Shamir', 'Adleman']\n"
      "for position, surname in enumerate(surnames, 2):\n"
      "    print(position, surname)")
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames, 2):
    print(position, surname)

print("\n-------------------\n")

print("people = ['Jonas', 'Julio', 'Mike', 'Mez']\n"
      "ages = [25, 30, 31, 39]\n"
      "nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']\n"
      "for person, age, nationality in zip(people, ages, nationalities):\n"
      "    print(person, age, nationality)")
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)

print("\n-------------------\n")

print("people = ['Jonas', 'Julio', 'Mike', 'Mez']\n"
      "ages = [25, 30, 31, 39]\n"
      "nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']\n"
      "for data in zip(people, ages, nationalities):\n"
      "    person, age, nationality = data\n"
      "    print(person, age, nationality)")
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)
