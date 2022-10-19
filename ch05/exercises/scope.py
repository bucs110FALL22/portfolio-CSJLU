def multiplication(num1, num2):
  result = 0
  for i in range(num2):
    result = result + num1
  return result


def exponential(num, expo):
  result = 1
  for i in range(expo):
    result = result * num
  return result


def square(num):
  return exponential(num, 2)

def main():
  testMulti = multiplication(5, 2)
  print(testMulti)
  testExpo = exponential(3, 5)
  print(testExpo)
  testSquare = square(6)
  print(testSquare)

  
main()
