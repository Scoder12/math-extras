"""__init__.py
Calls other files in the package.
"""


def fac(num):
    # Gets list of factors of variable num
    output = []
    # Creates list for output
    for x in range(1, num + 1):
    # Loop with variable x
        if num % x == 0 and not num % x in output:
            # Tests if x goes into num and if x is already in output
            output.append(x)
    return output

def lcm(num1, num2, limit=10):
  num1ls = [num1]
  num2ls = [num2]
  mult = list(range(2, limit + 1))
  for x in mult:
    num1ls.append(num1 * x)
    num2ls.append(num2 * x)
    if num1ls[-1] in num2ls:
      return num1ls[-1]
    elif num2ls[-1] in num1ls:
      return num2ls[-1]
    else:
      continue
  return


def prime (num):
    """prime(num)
    Returns true or false depending on whether or not a number is prime.
    num is and int to process.  
    """
    import time
    strnum = str(num)
    count = num - 1
    def remain (div):
        quotient = num / div
        strdiv = str(div)
        foo = num % div
        if foo == 0:
            return True
        else:
            return False
    while count > 1:
        if remain (count):
            return False
            count = 1
        else:
            count = count - 1
    return True
    return

def prime_out(num):
    """prime_out(num)
    User-friendly version of prime().
    Prints output and has timing functionality.
    Usage:
    prime_out(num)
    num is an int that to be evaluated as prime.  
    """
    import time
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
            print("or %.1f [min]" % ((t1_stop-t1_start)/60))
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
    print("or %.1f [min]" % ((t1_stop-t1_start)/60))
    print("--------------------------------------------------") 

    return

def mean(nums):
    output = 0
    for x in range(len(nums)):
        output += nums[x]
    return output / len(nums)
    

def mode(inlist):
    bubbleSort(inlist)
    streak = 1
    array = 1
    longest = 0
    while array < len(inlist) - 1:
        print("trying value ", inlist[array])
        if inlist[array] == inlist[array + 1]:
            streak = streak + 1
        else:
            if streak > longest:
                longest = streak
                modeo = inlist[array]
                streak = 1
        array = array + 1
    return modeo
    
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def median(listin):
	bubbleSort(listin)
	listo = 0
	length = len(listin)
	for x in range(int(length / 2) - 1):
		del listin[0]
		del listin[-1]
	if len(listin) == 2:
		listo = (int(listin[0] + listin[1]) / 2)
	else:
		listo = listin[1]
	return listo

def gcf(nums1, nums2):
	nums1 = fac(nums1)
	nums2 = fac(nums2)
	both = []
	if len(nums1) > len(nums2):
		loop = len(nums1)
		loopls = nums1
		loopo = nums2
	else:
		loop = len(nums2)
		loopls = nums2
		loopo = nums1
	for x in range(loop - 1):
		if loopls[x] in loopo:
			both.append(loopls[x])
	return both[-1]
