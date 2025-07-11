# sum of geometric series

def summation_geom_series():
  isRunning = True
  while isRunning == True:
    n_geom = int(input("Enter the value of n: "))
    r = float(input("Enter the value of r: "))
    a1_geom = float(input("Enter the first term: "))
    print(    "The sum of the series is: " + str(a1_geom * (1 - r ** n_geom) / (1 - r)))
    question = input("Would you like to do another one after this? (y/n): ")
    if question=="n":
      isRunning = False
  
  return

# sum of arithmetic series

def summation_arithmetic_series():
  isRunning = True
  while isRunning == True:
    n_arithm = int(input("Enter the value of n (number of terms): "))
    d = float(input("Enter the value of d (common difference): "))
    a1_arithm = float(input("Enter the first term (a1): "))
    print("The sum of the series is: " + str(n_arithm * (2 * a1_arithm + (n_arithm - 1) * d) / 2))
    question = input("Would you like to do another one after this? (y/n): ")
    if question =="n":
      isRunning = False
  
  return
