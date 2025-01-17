##secret = ['O', 'l', ' ', 'e'] # we are assembling a secret
##secret.insert(1, 'n') # message!
##secret.insert(3, 'y')
##secret.insert(5, 'g') # write the list down on paper
##secret.extend(['n', 'i', 'u']) # and track the changes
##secret.append('s') # to find out what the list
##secret.append('e') # becomes
##secret.append('s')
##for letter in " can read":
##    secret.append(letter)
##piece = " 012012t,,,h987i+++s823!" # when you are done,
### copy and run the code
##num = len(secret) # to see if you were right!
##for character in piece:
##    if character.isalpha() or character == " ":
##        secret.insert(num, character)
##        num += 1
##print(secret) # this will print a list of characters
##string = "".join(secret)
##print(string) # this will join the items of the list
### and make them into a string

##days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
##from datetime import datetime as dt
##print(days[dt.now().weekday()])

##import math as m
##num = int(input("enter an integer"))
##print(m.pow(num,2))

##import random as r
##employee = ["bob","bib","bab","beb","bub","bobby","bibby","babby","bebby","bubby","bobs"\
##,"bibs","babs","bebs","bubs"]
##group_size = int(input("how many people do you need"))
##print(r.sample(employee,group_size))

##import math as m
##diameter=int(input("what the diameter of circle"))
##circumference=(diameter*m.pi)
##print(circumference)

import turtle
bob = turtle.Turtle()
bob.pencolor("blue")
bob.forward(100)
bob.left(144)
bob.forward(100)
bob.left(144)
bob.forward(100)
bob.left(144)
bob.forward(100)
bob.left(144)
bob.forward(100)
bob.left(144)
