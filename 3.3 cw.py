##password = "U1tra_Secret_P@ssw0rd"
##c = 0
##s = 0
##d = 0
##for character in password:
##    if not (character.isalnum()):
##        s += 1
##    elif not character.isalpha() and character.isalnum():
##        d += 1
##    else:
##        c += 1
##if c >= 2 and d >= 2 and s >= 2:
##    print("That's a strong password!")
##else:
##    print("You should try to make a stronger password!")

##friends = ["Noah", "Marny", "Lisa", "Gurpreet", "Isaac"]
##friends = friends + ["Jenny"]
##print(friends)
##print(len(friends))
##for name in friends:
##    print(name, "is invited to my party!")

##string = "1234"
##string[0] = 3 # I want to change the first character to 3
## this produces an ERROR. You cannot change a string like this!
##list = [1,2,3,4]
##list[0] = 3 # this line does NOT cause an error!
##print(list) # what do you think will be printed?

##list = ['a', 'b', 'c', 'e', 'f']
##where_is_c = list.index('c') # where_is_c is the index of 'c'
##number_of_sevens = list.count(7)
##number_of_as = list.count('a')
##where_is_h = list.index('h') # what is in where_is_h ?

##jen = 0
##class_votes=["Jen", "Jayden", "Jared", "Jen", "Jen", "Jayden", "Jayden", "Jen"]
##for i in class_votes:
##    if i == "Jen":
##        jen +=1
##        
##jayden= class_votes.count("Jayden")
##jared = class_votes.count("Jared")
##
##if jen>jayden and jen > jared:
##    print("jen has the most votes")
##elif jayden> jen and jayden > jared:
##    print("jayden has the most votes")
##elif jared> jen and jared >jayden :
##    print("jared has the most votes")

jCount = 0
friends_names = ["jeremy", "jason", "jaymit", "river","lily", "jen", "ben", "harley", "frida"]
friends_names = friends_names + ["lisa","prisha","nathan"]
print(friends_names)
for i in friends_names:
    if i[0] == "j":
        jCount+=1
    else:
        jCount==jCount
print(jCount)
for f in friends_names:
    print(f.title())
