'''Write a Python program that iterates through integers from 1 to 50. 
For each multiple of three, print "Fizz" instead of the number; for each multiple of five, print "Buzz". 
For numbers that are multiples of both three and five, print "FizzBuzz".
For numbers which don't match the above conditions, print the number itself.
'''




def fizzbuzz(i):
    if isinstance(i, (int, float)) and i > 0:
        i = int(i)
        if i % 3 == 0 and i % 5 == 0:     #ewentualnie: if i % 15 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return  "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        else:
            return i
    return None
