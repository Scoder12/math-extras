'''
Doc String
kys
'''

def faclist(num):
    # Gets list of factors of variable num
    output = []
    # Creates list for output
    for x in range(1, num + 1):
    # Loop with variable x
        if num % x == 0 and not num % x in output:
            # Tests if x goes into num and if x is already in output
            output.append(x)
return output
