## 3. Class Syntax ##

class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"

black_honda_accord = Car()

print(black_honda_accord.color)

class Team():
    def __init__(self):
        self.name = "Tampa Bay Buccaneers"

bucs = Team()

print(bucs.name)

## 4. Instance Methods and __init__ ##

class Team():
    def __init__(self, name):
        self.name = name
        
giants = Team("New York Giants")

## 6. More Instance Methods ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# The NFL data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
        
    # Your method goes here
    def count_total_wins(self):
        total_wins = 0
        for team in nfl:
            if team[2] == self.name:
               total_wins += 1
        return total_wins
                    
    
bucs = Team("Tampa Bay Buccaneers")
bucs.print_name()

broncos_wins = Team("Denver Broncos").count_total_wins()
chiefs_wins = Team("Kansas City Chiefs").count_total_wins()

## 7. Adding to the init Function ##

import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
    
jaguars_wins = Team("Jacksonville Jaguars").count_total_wins()
 

## 8. Wins in a Year ##

import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self, year):
        count = 0
        for row in self.nfl:
            if row[2] == self.name and row[0] == year:
                count = count + 1
        return count
    
niners_wins_2013 = Team("San Francisco 49ers").count_total_wins("2013")
    