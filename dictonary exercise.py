empty_dict={}
ask = input("do you want to modify the dictionary?")
while ask == "yes":
    ask2=input("do you want to add,delete,or change a value?")
    if ask2 == "add":
        add=input("what key do you want to add?")
        add2=input("what value do you want it to be?")
        var=empty_dict.get(add,0)
        if var == 0:
            empty_dict[add]=add2
        else:
            print("invalid key")
        print(empty_dict)
    elif ask2 == "delete":
        delete = input("what key do you want to delete?")
        var=(empty_dict.pop(delete,"invalid key"))
        print(var)
        print(empty_dict)
    else:
        change=input("what key do you want to change?")
        change2=input("what value do you want it to be?")
        var=empty_dict.get(change,0)
        if var == 0:
            print("invalid key")
        else:
            empty_dict[change]=change2
        print(empty_dict)
    ask = input("do you want to modify the dictionary?")
