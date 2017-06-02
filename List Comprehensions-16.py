## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ships[i])
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [ price * 2 for price in apple_prices]
apple_prices_lowered = [ price - 100 for price in apple_prices]


## 5. Counting Female Names ##

name_counts = {}

for row in legislators:
    if row[3] == "F" and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = [(value is not None and value > 30) for value in values]

print(checks)

## 8. Highest Female Name Count ##

max_value = None

for count in name_counts:
    if max_value is None or name_counts[count] > max_value:
        max_value = name_counts[count]

## 9. The Items Method ##

plant_types = {
    "orchid": "flower",
    "cedar": "tree",
    "maple": "tree"
}

for key, value in plant_types.items():
    print(key)
    print(value)
    

## 10. Finding the Most Common Female Names ##

top_female_names = [(name) for name, count in name_counts.items() if count == 2]

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_names_count = {}

# Creating a disctionary with all the male names and their counts

for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        name = row[1]
        if name in male_names_count:
            count = male_names_count[name]
            male_names_count[name] = count + 1
        else:
            male_names_count[name] = 1

# Establishing which name is the most common

highest_male_count = None

for name, count in male_names_count.items():
    if highest_male_count is None or highest_male_count < count:
        highest_male_count = count
        
top_male_names = [(name) for name, count in male_names_count.items() if count is highest_male_count]