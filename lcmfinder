def findlcm(num1, num2, limit=10):
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
