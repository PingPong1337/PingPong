def type_check(x):
    if type(x) == str:
        print(x[1])
    elif type(x) == int:
        print(x+1)
    else:
        print("Blargh!")
(type_check(2))
(type_check(3.14))
(type_check("Hej!"))
