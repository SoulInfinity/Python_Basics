try:
  numerator = 10
  denominator = 0
  result = numerator/denominator
  numbers = [10,20,30]
  print(numbers[9])

  print(result)
except IndexError:
    print("Error : IndexError ")
except ZeroDivisionError:
  print("Zero division error")