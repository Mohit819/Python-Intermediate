##lst = []
##while lst == lst:
##    country = input("add a country")
##    country = country.title()
##    lst.append(country)
##    i = input("are you done adding")
##    if i == "done":
##        break
##lst.sort()
##print(lst)

##lst = ["a","b","c","d"]
##while len(lst)>0:
##    i = lst.pop(0)
##    print(i)

##cities = ["Portland", "San Francisco", "Houston", "Boston"]
##states = ["Oregon", "California", "Texas", "Massachusetts" ]
### Using a for loop, create this list below, use 'append'
####city_state = ["Portland, Oregon", "San Francisco, California",\
####"Houston, Texas", "Boston, Massachusetts"]
##city_state = []
##for i in range(len(cities)):
##    city_state.append(cities[i])
##    city_state.append(states[i])
##print(city_state)

days = ["monday", "wednesday", "thursday"]
# use the insert method to add "tuesday" in the right position
# use the append method to add "friday"
# use the extend method to add the weekend into the list
days.insert(1,"tuesday")
days.append("friday")
days.extend(["saturday","sunday"])
print(days)

