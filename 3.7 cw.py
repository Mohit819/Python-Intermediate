##def area_square(width):
##    return width * width
##def area_rectangle(width, length):
##    return width * length
##def area_triangle(base, height):
##    return base * height / 2
##def area_circle(length,height): # what information do you need?
##    return length*height
##print(area_square(4)) # what is printed?
##print(area_rectangle(6,10)) # what is printed?
##print(area_circle(10,10)) # call your circle function

##name = "Robert Downey Jr."
##title = "The Iron Giant"
### name and title are 'global
##
##def get_first_word(sentence):
##    space_index = sentence.index(' ')
##    first_word = sentence[:space_index]
##    # space_index, first_word, and sentence only exist here
##    # they are 'local' to this function!
##    # can you print name or title here? Try it out.no
##    return first_word
##
##print(sentence)
##print(space_index)
##print(first_word) # what do you think this would print? Try it out. it prints an error
##
##first_of_title = get_first_word(title)
##print(first_of_title)

##score = 0
##def check_guess(guess, answer):
##    global score
##    if guess.lower() == answer.lower():
##        score += 1 # an equals sign means you're reassigning score
##guess1 = input("What is the fastest mammal in the world?")
##check_guess(guess1, "Cheetah")

##def employee_info(name, position = "Labourer"):
##    print(name, "\t", position)
##employee_info("Jenna", "Manager")
##employee_info("Karim", "Supervisor")
##employee_info("Paula")
##employee_info("Lori")

##def max(*nums):
##    biggest_so_far = 0 # this only works for positive numbers
##    for num in nums: # nums is a collection!
##        if num > biggest_so_far:
##            biggest_so_far = num
##    return biggest_so_far
##print(max(1,2,34,7))
##print(max()) # what if we give it no arguments? it gives 0

##def employee_info(name, position = "Labourer"):
##    print(name, "\t", position)
### you can give them in any order if you use their names!
##employee_info(position="Supervisor", name="Kira")
##
##def max(*nums, positive = True):
##    if not positive:
##        return "This function only works for positive numbers!"
##    biggest_so_far = 0 # this only works for positive numbers
##    for num in nums: # nums is a collection!
##        if num > biggest_so_far:
##            biggest_so_far = num
##    return biggest_so_far
### the collections still must come first
##print(max(1,2,3,4))
##print(max(-2,-1,-10, positive = False))

###a global variable is a variable that can be accessed in the entire code
##hi = "hi"
###a local variable is a variable that can only be accessed in a function
##def print2():
##    hello = "hello"

#when you use a local variable outside of a function it gives a name error

##def min2(*nums):
##    smallest_so_far = 0
##    for nums in nums:
##        if nums < smallest_so_far:
##            smallest_so_far = nums
##    return smallest_so_far
##print(min2(40,38,19,-2))
##print(min2())

##def names():
##    name = []
##    no = input("add")
##    while no == "yes":
##        name.append(input("name pls"))
##        no = input("add")
##    for i in name:          
##        print(i,end="\t")
##names()

##def name(name="N/A",number="xxx-xxx-xxxx"):S
##    print(name,number)
##name("Mohit", "905-789,9868")
##name("Mohit",)
##name(name="N/A" ,number="905-789-9868")

##def area_rectangle(l,w=-1):
##    if w == -1:
##        print(l*l)
##    else:
##        print(l*w)
##area_rectangle(100)

##def sum_or_product(*nums,i):
##    if i == True:
##        result = 0
##        for num in nums:
##            result+=num
##        return result
##    else:
##        result = 1
##        for num in nums:
##            result*=num
##        return result
##print(sum_or_product(1,2,3,4,5,i = True))
##print(sum_or_product(1,2,3,4,5,i = False))

#optinal parameters are used when you don't need an argument and set something to a default.
# keyword parameters are used when you have an infinite amount of arguments for one parameter and->
#need to add the other argument
