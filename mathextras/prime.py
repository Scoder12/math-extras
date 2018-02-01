"""Prime.py
Program to find whether or not a number is prime.  
"""
import time

# Importer
def prime (num):
    """prime(num)
    Returns true or false depending on whether or not a number is prime.
    num is and int to process.  
    """
    strnum = str(num)
    count = num - 1
    def remain (div):
        quotient = num / div
        strdiv = str(div)
        foo = num % div
        if foo == 0:
            #print (strnum +" is divisible by " + strdiv)
            return True
        else:
            #print (strnum + " is not divisible by " + strdiv + "...")
            return False
    while count > 1:
        if remain (count):
            return False
            count = 1
        else:
            count = count - 1
    return True
    #print (strnum + " is prime! Done! ")
    #print("--------------------------------------------------")
    #print("Elapsed time: %.1f [min]" % ((t1_stop-t1_start)))
    #print("CPU process time: %.1f [min]" % ((t2_stop-t2_start)))
    #print("--------------------------------------------------") 
    return

    
