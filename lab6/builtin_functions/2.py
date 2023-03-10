#ord
def countof_up_and_low(string):
    lower = 0
    upper = 0
    for i in range(len(string)):
        if ord(string[i])>64 and ord(string[i])<91:
            upper+=1
        elif ord(string[i])>96 and ord(string[i])<123:
            lower+=1

    print("lower case char:", lower)
    print("upper case char:", upper)

string = "AlMaTy"
countof_up_and_low(string)