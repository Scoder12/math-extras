"""__init__.py
Contains all functions and data for the package.  
"""
# π constant (500 digits)
#PI = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912
# π symbol (just because)
PI_SYMBOL = "π"

def bubbleSort(inlist):
	"""BubbleSort: Returns the array specified sorted  
	Args:
		ainlist (array): inlist to be sorted
	Returns:
		array: inlist sorted from greatest to least
	Code credit: interactivepython.org
	"""
	for passnum in range(len(inlist)-1,0,-1):
		for i in range(passnum):
			if inlist[i]>inlist[i+1]:
				temp = inlist[i]
				inlist[i] = inlist[i+1]
				inlist[i+1] = temp
	return inlist

def fac(num):
    """fac: Returns an array of factors for the given number
    Args: 
    	num (int): number to list factors for
    Returns:
    	array: factors of num
    """
    output = []
    # Creates inlist for output
    for x in range(1, num + 1):
    # Loop with variable x
        if num % x == 0 and not num % x in output:
            # Tests if x goes into num and if x is already in output
            output.append(x)
    return output

def lcm(num1, num2, limit=10):
  """lcm: finds the least common multiple of two numbers
  Args:
	num1 (int): First number to calculate lcm of
	num2 (int): Second number to calculate lcm of
  Returns:
	int: the least common multiple (lcm) of num1 and num2
  """
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
    """prime: calclates whether or not a number is prime
    Args:
    	num (int): Number to be evaluated as prime
    Returns:
    	bool: True if the number is prime, False otherwise
    Note: prime() is mostly for internal use, for a more user User-friendly version,
    see prime_out()
    """
    count = num - 1
    def remain (div):
        ans = num % div
        if ans == 0:
        	# Divides, evenly, so not prime
            return True
        else:
        	# Try again
            return False
    while count > 1:
        if remain (count):
            return False
        else:
            count = count - 1
    # We're out of the loop, so it must be prime
    return True

def prime_out(num):
    """prime_out: A user-friendly tool to evaluate whether or not a number is prime. 
    Args:
    	num (int): Number to be evaluated as prime
    Returns:
    	Prints whether or not the number is prime and how long it took to evaluate.   
    """
    import time
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    strnum = str(num)
    count = num - 1
    print("Calculating whether " + strnum + " is prime...")
    def remain (div):
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
	"""mean: finds the mean of a list of numbers
	Args:
		nums (array): At least two numbers to find the mean of.
	Returns:
		Float: the exact mean of the numbers in the array.  
	"""
	output = 0
	for x in range(len(nums)):
		output += nums[x]
	return output / len(nums)
    

def mode(inlist):
	"""mode: finds the mode of an array of numbers
	
	Important note: This code does not support multiple modes!
	Even though technically there can be more than one mode of
	a data set, this code will return None if there is no clear
	mode, and only the first mode if there is more than one mode.
	We are sorry for the inconvenience, and hope to add this
	feature soon!
	
	Args:
		inlist (array): An array of numbers to find the mode of
	Returns:
		Int: the mode of the numbers given
		None if there is no clear mode
	"""
	bubbleSort(inlist)
	streak = 1
	array = 1
	longest = 1
	modeo = "nan"
	while array < len(inlist) - 1:
		if inlist[array] == inlist[array + 1]:
			streak = streak + 1
		else:
			if streak > longest:
				longest = streak
				modeo = inlist[array]
				streak = 1
				array = array + 1
	if modeo == "nan":
		modeo = None
	return modeo

def median(inlistin):
	"""median: Finds the median of the provided array.
	Args:
		inlistin (array): An array of numbers to find the median of
	Returns:
		Float: the median of the numbers given
	"""
	bubbleSort(inlistin)
	inlisto = 0
	length = len(inlistin)
	for x in range(int(length / 2) - 1):
		del inlistin[0]
		del inlistin[-1]
	if len(inlistin) == 2:
		inlisto = (int(inlistin[0] + inlistin[1]) / 2)
	else:
		inlisto = inlistin[1]
	return inlisto

def gcf(nums1, nums2):
	"""gcf: Finds the greatest common factor of the given numbers.
	Args:
		nums1 (int): The first number to find the greatest common factor of
		nums2 (int): The second number to find the greatest common factor of
	Returns:
		Int: the greatest common factor of the given numbers
	"""
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
