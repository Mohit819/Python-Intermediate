##lst = []
##while lst == lst:
##    country = input("add a country")
##    country = country.title()
##    lst.append(country)
##    i = input("are you done adding")
##    if i == "done":
##        break
##a = lst.sort()

##lst = ["a","b","c","d"]
##while len(lst)>1:
##    i = lst.pop(0)
##    print(i)

##cities = ["Portland", "San Francisco", "Houston", "Boston"]
##states = ["Oregon", "California", "Texas", "Massachusetts" ]
### Using a for loop, create this list below, use 'append'
####city_state = ["Portland, Oregon", "San Francisco, California",\
####"Houston, Texas", "Boston, Massachusetts"]
##city_state = []
##city_state.append(cities[0:1:])
##city_state.append(states[0:1:])
##city_state.append(cities[1:2:])
##city_state.append(states[1:2:])
##city_state.append(cities[2:3:])
##city_state.append(states[2:3:])
##city_state.append(cities[3:4:])
##city_state.append(states[3:4:])
##print(city_state)

days = ["monday", "wednesday", "thursday"]
# use the insert method to add "tuesday" in the right position
# use the append method to add "friday"
# use the extend method to add the weekend into the list
days.insert(1,"tuesday")
days.append("friday")
days.extend(["saturday","sunday"])
print(days)
