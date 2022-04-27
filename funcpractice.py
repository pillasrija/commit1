# write a python function to find the max of three numbers

def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(3, 6, -5))


# write a python function to sum all the numbers in a list

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


print(sum((8, 2, 3, 0, 7)))


# write a python function to multiply all the numbers in a list

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

a_list = [8,2,3,-1,7]

print(f"Multiplying all numbers in a list :  {multiply(a_list)}")

# write a python program to reverse a string

def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))

# write a python function to calculate the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Input a number to compute the factorial : "))

print(factorial(n))

# write a python function to check whether a number falls in a given range

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else:
        print("The number is outside the given range")
test_range(5)


