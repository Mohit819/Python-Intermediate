### I am writing a book about a small dinosaur
### this program will help me pick the best title
##titles = ["the littlest dinosaur", "tiny dinosaur",\
##"itsy bitsy dino", "the dinosaur that never growed"]
### there is a mistake! Use item assignment to change the item
### the dinosaur that never growed to the dinosaur that never grew
### titles should have proper capitalization, let's change that
##for i in range(len(titles)):
##    titles[i] = titles[i].title()
##print(titles)
### my publisher tells me shorter titles are better!
##long_titles = []
##good_titles = []
##for title in titles:
##    if len(title) > 20: # 20 characters is the limit
##        long_titles += [title]
##    else:
##        good_titles += [title]
### now we split it up into long and short titles
##print(long_titles)
##print(good_titles)
##best_title = good_titles[0]
### replace ? with the index of your favourite

##list = ['a', 'b', 'c', 'e', 'f']
##list.append('g') # notice we DO NOT write list =list.append('g')
##print(list)
##list.insert(3, 'd') # insert item 'd' at index 3
##print(list)
##list.extend([7,8]) # extend needs a list as input!
##print(list)
##list.remove('b') # remove the ITEM 'b' from the list
##print(list)
##x = list.pop(1) # remove item at INDEX 1, and store item in x
##print(x)
##print(list)
##a = list.sort()
##print(list)
##list.reverse() # now our list is reversed
##print(list)

##numbers = [3,2,1]
##numbers.sort()
##print(numbers) # the list stored in numbers is DIFFERENT now
##student = "Liam"
##student.upper()
##print(student) # what does this print?

##student = student.upper()
##print(student) # now we print "LIAM"!

##weekdays = ['monday', 'tuesday']
##weekdays.append('wednesday')
##print(weekdays)

##cities = ['oakville', 'niagara falls', 'toronto', 'vaughn']
##cities.append('brampton')
##first = cities[0]
##cities[0] = cities[0].upper()
##print(cities[1].upper())

animal=["elephant","lion","tiger","duck","chicken"]
animal.insert(1,"Charizard")
animal.sort()
animal.remove("chicken")
for i in range(len(animal)):
    animal[i] = animal[i] + "!"

print(animal)
best_animals=[animal[0:1:],animal[1:2:],animal[2:3:]]
print(animal)
print (best_animals)
