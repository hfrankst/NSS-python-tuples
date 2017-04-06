zoo = ('Panther', 'Elephant', 'Polar Bear', 'Spider Monkey', 'Giraffe', 'Macaw')

zoo.index('Panther') #finding the index of panther 
print(zoo.index('Panther'))

for each in zoo: #printing each animal in the zoo tuple
	print(each)

zoo_list = list(zoo) #converting the tuple to a list 
new_animals = ('Lizard', 'Fox', 'Cobra')
zoo_list.extend(new_animals)
print(zoo_list)

zoo_tuple = tuple(zoo_list)
print(zoo_tuple)