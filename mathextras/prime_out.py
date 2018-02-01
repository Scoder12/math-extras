"""prime_out.py
A version of prime.py, but is more
user-friendly and has timing fuctionality.  

Author: @Scoder12

Available under the MIT license.  
"""
def prime_out(num):
    """prime_out(num)
    User-friendly version of prime().
    Prints output and has timing functionality.
    Usage:
    prime_out(num)
    num is an int that to be evaluated as prime.  
    """
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    strnum = str(num)
    count = num - 1
    print("Calculating whether " + strnum + " is prime...")
    def remain (div):
        quotient = num / div
        strdiv = str(div)
        foo = num % div
        if foo == 0:
            print (strnum +" is divisible by " + strdiv)
            return True
        else:
            return False
    while count > 1:
        if remain (count):
            t1_stop = time.perf_counter()
            t2_stop = time.process_time()
            print(strnum + " isn't Prime.  Done! ")
            print("--------------------------------------------------")
            print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
            print("or %.1f [min]" % ((t1_stop-t1_start)/60))
            print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))
            print("or %.1f [min]" % ((t1_stop-t1_start)/60)))
            print("--------------------------------------------------") 
            return
            count = 1
        else:
            count = count - 1
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print (strnum + " is prime! Done! ")
    print("--------------------------------------------------")
    print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
    print("or %.1f [min]" % ((t1_stop-t1_start)/60))
    print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))
    print("or %.1f [min]" % ((t1_stop-t1_start)/60)))
    print("--------------------------------------------------") 

    return
    
if __name__ == "__main__":
    print("prime.py")
    print("\tA prime number detector.  ")
    print("\tWARNING: Large numbers may cause significant CPU load. ")
    def ask():
        numberstr = input("Number: ")
        number = int(numberstr)
        prime_out(number)
        print("\n")
        ask()
        return
    ask()
        
