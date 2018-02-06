mathextras

A package with useful math functions.  
Authors:
@Scoder12
@Poipt

We're on pip! Run pip install mathextras. (Version may not be up to date. Check PIPLOG.txt for more information)

Code licensed under the MIT license.  

Usage:

mathextras.prime(num)
	Return true or false based on whether or not num is prime.  WARNING: Large numbers can slow down your program or machine.  
	Example:
	>>> mathextras.prime(31)
	True
	
mathextras.prime_out(num):
	User friendly version of mathextras.prime. Also calculates time and CPU processed time.
	>>> mathextras.prime_out(17)
	Calculating whether 6481543 is prime...
	6481543 is prime! Done! 
	--------------------------------------------------
	Elapsed time: 6.8 [sec]
	or 0.1 [min]
	CPU process time: 3.4 [sec]
	or 0.1 [min]
	--------------------------------------------------
	
mathextras.fac(num)
	Returns an array of a number's factors in order of greatest to least.  
	Example: 
	>>> mathextras.fac(12)
	[1, 2, 3, 4, 6, 12]
	
mathextras.lcm(num1, num2, limit)
	*limit is optional.
	Returns the least common multiple of num1 and num2.  
	Example: 
	>>> mathextras.lcm(4, 7)
	28
	
mathextras.mode(nums)
	Returns the mode (number that occurs most offen in a set of data) of the list nums.
	Example:
	>>> mathextras.mode([4, 6, 6])
	6
	
mathextras.mean(nums)
	Returns the mean (average) of the list nums.
	Example
	>>> mathextras.mean([6, 11, 7])
	8

mathextras.bubbleSort(nums)
	*code credit to interactivepython.org
	Sorts the list nums using the bubble sort method.
	Example:
	>>> mathextras.bubbleSort([4, 6, 3])
	[3, 4, 6]
	
mathextras.median(nums)
	Returns the median of the list nums.
	Example:
	>>> mathextras.median([2, 4, 6])
	4

mathextras.gcf(num1, num2)
	Returns the greatest common factor of num1 and num2.
	Example:
	>>> mathextras.gcf([6, 12])
	6

Please make sure to report any bugs you may find either in the issues section of GitHub, or to pymathextras@gmail.com.
Thanks for using mathextras. It means a lot to us! <3 =)
