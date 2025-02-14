##mystery_dict = {}
##my_keys = []
##my_values = []
##def key_fetcher(*keys):
##    for key in keys:
##        my_keys.append(key)
##def value_fetcher(*vals):
##    for val in vals:
##        my_values.append(val)
##def dict_creator(key_list, val_list, dict = mystery_dict):
##    for i in range(len(key_list)):
##        dict[key_list[i]] = val_list[i]
##    return dict
##key_fetcher(1,2,3,4)
##value_fetcher('one', 'two', 'three', 'four')
##new_dict = dict_creator(my_keys, my_values)
##print(new_dict)

# with open("Mohit/Python Intermediate/candy_text (1).txt","r")as f:
#     print(f.read())

    # candy_names=[]
    # for line in f:
    #     split1=line.split(",")
    #     candy_names.append(split1[0])
    # print(candy_names)

# with open("Mohit/Python Intermediate/long_poem (1).txt") as f_o:
#     for line in f_o:
#         print(f_o.readline())

# with open ("Python Intermediate/second_poem (1).txt","r")as f:
#     for line in f:
#         if line != "/n":
#             print(line)
#         else:
#             f.readline()

# with open ("Python Intermediate/all_coders.txt","a") as f:
#     name = input("enter ur name")
#     f.write(name + "\n")

# with open ("Python Intermediate/file_knowledge.txt","w")as f:
#     f.write("a file object is a variable holding a file so you can interact with it\nwrite mode is the most dangerous to use because it starts from the begining of a file and deletes everything else.")

with open ("Python Intermediate/pattern.txt","w") as w:
    for i in range(10,0,-1):
        w.write("*"* i)
        for i in range(1):
            w.write("\n")

        