def repeat (val):

    if(val > 0):
        print(val-1)
        val = val - 2
        repeat(val)




repeat(6)