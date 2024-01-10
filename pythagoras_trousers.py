# The function takes an array and returns true or false.

def pt(any_array):
    x = False
    if len(any_array) == 3:
        any_array.sort()
        if (any_array[1]**2 + any_array[0]**2) == any_array[2]**2:
            x = True
        else:
            x = False
    else:
        print("Try again")

    return x
