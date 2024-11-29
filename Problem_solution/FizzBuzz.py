# print 1...100
# print "Fizz" if divisible by 3
# print "Buzz" if divisible by 5
# print "FizzBuzz" if divisible by 3 and 5
# print "Fazz" if 23

for n in range(1, 101):
    
    if n == 23:
        print("Fazz")
    elif n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)