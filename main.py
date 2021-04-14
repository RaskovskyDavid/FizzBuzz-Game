#Write your code below this row 👇

divisible_3 = 'Fizz'
divisible_5 = 'Buzz'
for number in range(1, 101):
  if number%3 ==0 and number%5 == 0:
    print(divisible_3+divisible_5)
  else:
    if number%3 ==0:
      print(divisible_3)
    if number%5 ==0:
      print(divisible_5)
  if number%3 !=0 and number%5 != 0:
    print(str(number))