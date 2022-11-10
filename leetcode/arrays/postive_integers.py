from math import sqrt


def check_perfect_number(num):
    postive_divisors = [1]
    print(int(sqrt(6)))
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            postive_divisors.append(i)
            postive_divisors.append(int(num/i))

    print(postive_divisors)

    if sum(postive_divisors) == num:
        return True 
    else:
        return False


print(check_perfect_number(28))