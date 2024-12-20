####my_name = "Jaymit"
####first_letter = my_name[0]
####print(first_letter)
####last_letter = "Jaymit"[len("Jaymit") - 1]
####print(last_letter) # what is printed here?
####
####secret_word = "Cat"[0] + "Dog"[1] + "Bird"[3] + "Snake"[4] + "r"
####print(secret_word)
##
##string = "Blueberry Pancakes!"
##print(string[0:9:2])
### step is 2, meaning our slice includes index 0, 2, 4, ...
### so this will print "Bubry"
##print(string[4:9:1]) # this prints 'berry'
### We do not need to use 3 inputs all the time
### If you omit the step, it assumes you want your step to be 1
##print(string[4:9]) # so this is the same! it also prints 'berry'
### You don't even need to give it a start or end!
### If you omit the start, it starts at the beginning
##print(string[:9])
### this is the same as string[0:9:1], so it prints "Blueberry"
### If you omit the end, Python assumes you want to go to the end
##print(string[10:])
### this is the same as string[10:19:1] so it prints "Pancakes!"
### What if you omit everything?
##print(string[:]) # what will be printed here?
### What about a negative index?
##print(string[19:9:-1])
### this starts with index 19, then moves -1 steps to index 18
### then 17, 16, all the way until (but not including) index 9
### So this prints '!sekacnaP', which is 'Pancakes!' backwards!
### with negative indices, start has to be BIGGER than the end
##print(string[::-1])
### this is how you omit start and end but include a step
### what should this print?

##i="Strawberry Shortcake"
##print(i[0:1])
##print(i[11:12])
##print(i[-9:-8])
##print(i[-20:-19])

##name = input("whats ur name")
##print(name[0:1])
##print(name[len(name)::-1])

##message = "ccowdcionygy nrzuclwepsq!q"
##print(message[0::2])

##name = "Justin Timberlake"
##name2 = (name[7:] + name[:6])
##print(name2)

secret = "isagbnxiwrptysu ctuueogbyal hlklrae qweoinbkp zusoyY"
secret2 = secret[::-1]
print(secret2)
print(secret2[::2])
