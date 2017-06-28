def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return n
    return "BuzzFizz"
    
def fizzbuzz(n):
    if n == 1:
        return n
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Fizz"
    elif n % 3 == 0:
        return "Buzz"
    else:
        # Check Prime
        return is_prime(n)

# Main
num = input("Enter the number of elements in fibonacci series: ") 
if num == 0:
    print "No Fibonacci Series was generated for input",num
first = 0
second = 1

# Generate Fibonacci Series
for i in range(num):
    if i == 0 or i == 1:
        next = i
        print next
        continue
    else:
        next = first + second
        first = second
        second = next

    # Check Fizz Buzz
    print fizzbuzz(next)

