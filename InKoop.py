class Student(object):

    def __init__(self, name):
        self.name = name
        self.costs = []
        self.ratings = []
        self.highestcost = 0
        self.cheapestcost = 0
        self.highestrating = 0
        self.cheapestrating = 0

    def __repr__(self):
        return '<' + self.name + ', ' \
              + 'high=' + str(self.highestcost) + ', ' \
              + 'cheap=' + str(self.cheapestcost) + ', ' \
              + 'high=' + str(self.highestrating) + ', ' \
              + 'cheap=' + str(self.cheapestrating) + ', ' \
              + 'avgcost=' + str(self.getAveragecost()) +', ' \
              + 'avgrating=' + str(self.getAveragerating()) + '>'

    def addCost(self, cost):
        self.costs.append(cost)
        self.highestcost = max(self.highestcost, cost)

    def addRating(self, rating):
        self.ratings.append(rating)
        self.highestrating = max(self.highestrating, rating)

    def lowCost(self, cost):
        self.costs.append(cost)
        self.cheapestcost = min(self.cheapestcost, cost)

    def lowRating(self, rating):
        self.ratings.append(rating)
        self.cheapestrating = max(self.cheapestrating, rating)


    def getAveragecost(self):
        l = len(self.costs)
        if l == 0:
            return 0
        else:
            return sum(self.costs) / l

    def getAveragerating(self):
        l = len(self.ratings)
        if l == 0:
            return 0
        else:
            return sum(self.ratings) / l

import csv

results = open ('Desktop/hotels.csv', "r+")
csv1 = csv.reader(results, delimiter=",")


data = {}
highscore = 0

for eachline in csv1:
    name = eachline[1]
    Ratings = int(eachline[4])

    tudent = data.get(name, None)
    if hotel == None:
        hotel = Hotel(name)
        data[name] = hotel

    cost = int(eachline[1])
    hotel.addCost(cost)

hotels = [data[key] for key in data]

sorted_alphabetically = sorted(hotels, key=lambda x:x.score)
sorted_by_highest_cost = sorted(hotels, key=lambda x:x.highestcost, reverse=True)
sorted_by_lowest_cost = sorted(hotels, key=lambda x:x.cheapestcost, reverse=True)
sorted_by_highest_rating = sorted(hotels, key=lambda x:x.highestcost, reverse=True)
sorted_by_lowest_cost = sorted(hotels, key=lambda x:x.cheapestcost, reverse=True)
sorted_by_avg_cost = sorted(hotels, key=lambda x:x.getAverage(), reverse=True)

print ('sorted_alphabetically =', sorted_alphabetically)
print ('sorted_by_highest_cost =', sorted_by_highest_cost)
print ('sorted_by_lowest_cost =', sorted_by_lowest_cost)
print ('sorted_by_highest_rating =', sorted_by_highest_rating)
print ('sorted_by_lowest_rating =', sorted_by_lowest_rating)
print ('sorted_by_avg_cost =', sorted_by_avg_cost)
