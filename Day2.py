if __name__ == '__main__':
    # The four primary built-in data structures offered in Python3 are:
    # List
    # Tuple
    # Dictionary
    # Set
    jon_snow = ["Jon Snow", "Winterfell", 30]
    print(jon_snow)

    # Indexing
    print(jon_snow[0])

    # Length
    print(len(jon_snow))  # Length of list is the number of elements

    # Lists are mutable
    jon_snow = ["Jon Snow", "Winterfell", 30]
    print(jon_snow[1])
    jon_snow[1] = 'Winter'
    print(jon_snow[1])

    # Using range() --> A range can further be converted into a list by using the list() casting.
    num_seq = range(0, 10)  # A sequence from 0 to 9
    print(type(num_seq))
    num_list = list(num_seq)  # The list() method casts the sequence into a list
    print(type(num_list))
    print(num_list)

    num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
    print(list(num_seq))

    world_cup_winners = [[2006, "Italy"], [2010, "Spain"], [2014, "Germany"], [2018, "France"]]
    print(world_cup_winners)

    # Indexing
    world_cup_winners = [[2006, "Italy"], [2010, "Spain"], [2014, "Germany"], [2018, "France"]]
    print(world_cup_winners[1])
    print(world_cup_winners[1][1])  # Accessing 'Spain'
    print(world_cup_winners[1][1][0])  # Accessing 'S'

    part_A = [1, 2, 3, 4, 5]
    part_B = [6, 7, 8, 9, 10]
    merged_list = part_A + part_B
    print(merged_list)

    # or

    part_A = [1, 2, 3, 4, 5]
    part_B = [6, 7, 8, 9, 10]
    part_A.extend(part_B)
    print(part_A)

    # append
    num_list = []  # Empty list
    num_list.append(1)
    num_list.append(2)
    num_list.append(3)
    print(num_list)

    # insert to a particular index
    num_list = [1, 2, 3, 5, 6]
    num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
    print(num_list)

    # remove element - pop()
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    last_house = houses.pop()
    print(last_house)
    print(houses)

    # remove()
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    print(houses)
    houses.remove("Ravenclaw")  # remove an element
    print(houses)

    populations = [["Winterfell", 10000], ["King's Landing", 50000],
                   ["Iron Islands", 5000]]
    print(populations)
    populations.remove(["King's Landing", 50000])
    print(populations)

    # List Slicing
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print(num_list[2:5])
    print(num_list[0::2])

    # Index Search
    cities = ["London", "Paris", "Los Angeles", "Beirut"]
    print(cities.index("Los Angeles"))  # It is at the 2nd index

    # In
    cities = ["London", "Paris", "Los Angeles", "Beirut"]
    print("London" in cities)
    print("Moscow" not in cities)

    # sort
    num_list = [20, 40, 10, 50.4, 30, 100, 5]
    num_list.sort()  # changes the order in list as well
    print(num_list)

    # List comprehension is a technique that uses a for loop and a condition to create a new list from an existing one.
    # The result is always a new list, so it’s a good practice to assign list comprehension to a new variable

    # without LC
    nums = [10, 20, 30, 40, 50]
    nums_double = []
    for n in nums:
        nums_double.append(n * 2)
    print(nums)
    print(nums_double)

    # with LC
    nums = [10, 20, 30, 40, 50]
    # List comprehension
    nums_double = [n * 2 for n in nums]
    print(nums)
    print(nums_double)

    # Adding a condition
    nums = [10, 20, 30, 40, 50]
    # List comprehension
    nums_double = [n * 2 for n in nums if n % 4 == 0]
    print(nums)
    print(nums_double)

    # Multi List
    list1 = [30, 50, 110, 40, 15, 75]
    list2 = [10, 60, 20, 50]
    sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]
    print(sum_list)

    # Tuple - a tuple is immutable
    # However, it can contain mutable elements like a list. These elements can be altered.
    car = ("Ford", "Raptor", 2019, "Red")
    print(car)

    # Length
    print(len(car))

    # Indexing
    print(car[1])

    # Slicing
    print(car[2:])

    # Merging Tuples
    hero1 = ("Batman", "Bruce Wayne")
    hero2 = ("Wonder Woman", "Diana Prince")
    awesome_team = hero1 + hero2
    print(awesome_team)

    # Nested Tuples
    hero1 = ("Batman", "Bruce Wayne")
    hero2 = ("Wonder Woman", "Diana Prince")
    awesome_team = (hero1, hero2)
    print(awesome_team)

    # Search
    cities = ("London", "Paris", "Los Angeles", "Tokyo")
    print("Moscow" in cities)

    # index()
    cities = ("London", "Paris", "Los Angeles", "Tokyo")
    print(cities.index("Tokyo"))

    # Immutability
    # Since tuples are immutable, we can’t add or delete elements from them.
    # Furthermore, it isn’t possible to append another tuple to an existing tuple.
    cities = ("London", "Paris", "Los Angeles", "Tokyo")
    # cities[2] = "Moscow" # Not supported
    # cities.append() # Not supported
    # cities.remove() # Not supported

    cities = ("London", "Paris", ["Los Angeles", "Mumbai"], "Tokyo")
    cities[2][0] = "Kolkata"  # As List is a mutable one, so we can change its elements
    # but we can not change a list to anything else
    # cities[2] = "Kolkata" # Not Supported

    # Dictionaries
    # A dictionary stores key-value pairs, where each unique key is an index which holds the value associated with it.
    # Dictionaries are unordered because the entries are not stored in a linear structure.
    empty_dict = {}  # Empty dictionary
    print(empty_dict)

    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}
    print(phone_book)

    # Since the dictionary is an unordered data structure, the order of the output will not necessarily match the order
    # in which we wrote the entries.
    # Key-value pairs are accessed in a random or unordered manner.
    #  dict() Constructor
    empty_dict = dict()  # Empty dictionary
    print(empty_dict)

    phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
    # Keys will automatically be converted to strings
    print(phone_book)

    # Alternative approach
    phone_book = dict([('Batman', 468426),
                       ('Cersei', 237734),
                       ('Ghostbusters', 44678)])
    print(phone_book)

    # Accessing Values
    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}
    print(phone_book["Cersei"])
    print(phone_book.get("Ghostbusters"))

    # Adding/Updating Entries
    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}
    print(phone_book)

    phone_book["Godzilla"] = 46394  # New entry
    print(phone_book)

    phone_book["Godzilla"] = 9000  # Updating entry
    print(phone_book)

    # Removing Entries
    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}
    print(phone_book)

    del phone_book["Batman"]
    print(phone_book)

    # If we want to use the deleted value, the pop() or popitem() methods would work better:
    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}
    print(phone_book)

    cersei = phone_book.pop("Cersei")
    print(phone_book)
    print(cersei)

    # Removes and returns the last inserted pair, as a tuple
    # In Python versions before 3.7, popitem() removes and returns the random item
    lastAdded = phone_book.popitem()
    print(lastAdded)

    # length
    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}
    print(len(phone_book))

    # Checking Key Existence / Search
    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}
    print("Batman" in phone_book)
    print("Godzilla" in phone_book)

    # Copying Contents / Adding
    phone_book = {"Batman": 468426,
                  "Cersei": 237734,
                  "Ghostbusters": 44678}

    second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

    # Add secondphone_book to phone_book
    phone_book.update(second_phone_book)
    print(phone_book)

    # Dictionary Comprehension
    # To iterate the dictionary, dict.items() operation which turns a dictionary into a list of (key, value) tuples.
    houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
    new_houses = {n ** 2: house + "!" for (n, house) in houses.items()}
    print(houses)
    print(new_houses)



















