import random

#Part A
weeks = 16
classes = 5
tuition = 6000
classes_per_week=4
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)
print((weeks, type(weeks)), '\n', (classes, type(classes)), '\n', (tuition, type(tuition)), '\n', (classes_per_week, type(classes_per_week)), '\n', (cost_per_week, type(cost_per_week)), '\n', (cost_per_class, type(cost_per_class)))

#Part B
biglist = [5, 'S', 'Z', 0, 3.25]
john = random.choice(biglist)
print(john)