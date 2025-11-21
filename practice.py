def sieve(n):
    if n < 2:
        return []

    # Start assuming every number is prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark multiples of p starting at p*p
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    # Collect primes
    list_of_primes = [num for num, prime in enumerate(is_prime) if prime]
    return list_of_primes


def common_characters(a, b):
    result = []
    b_list = list(b)  # so we can remove matched characters

    for ch in a:
        if ch in b_list:
            result.append(ch)
            b_list.remove(ch)

    return "".join(result)


def fizzbuzz(n):
    if n < 1:
        return ""

    # handle first value
    result = "1"

    # loop for remaining values
    for i in range(2, n + 1):
        if i % 15 == 0:
            piece = "FizzBuzz"
        elif i % 3 == 0:
            piece = "Fizz"
        elif i % 5 == 0:
            piece = "Buzz"
        else:
            piece = str(i)

        result += "," + piece

    return result


def is_palindrome(text):
    # keep only letters and numbers, and make lowercase
    cleaned = ""
    for ch in text:
        if ch.isalnum():
            cleaned += ch.lower()

    # check if cleaned text reads the same forward and backward
    return cleaned == cleaned[::-1]


def valid_number(n):
    if n.isdigit() or (n.startswith("-") and n[1:].isdigit()):
       number=int(n)
       return number
    else:
         return None

def valid_string(s):
    if not not s and any(ch.isalnum() for ch in s):
        return s
    else:
        return None


def do_sieve():
    print()
    while True:
        num_input = input("Enter a limit n for primes: ")
        number = valid_number(num_input)    
        if number is not None:
            print(sieve(number))
            return
        else:
            print("That is not a valid number. Please try again.")


def do_common_characters():
    print()
    print("Finding common characters between two strings.")
    print()
    while True:
        str1 = input("Enter the first string: ")
        if valid_string(str1) is not None:
            break
        else:
            print("That is not a valid string. Please try again.")

    while True:
        str2 = input("Enter the second string: ")
        if valid_string(str2) is not None:
            break
        else:
            print("That is not a valid string. Please try again.")  

    print("Common characters:", common_characters(str1, str2))


def do_fizzbuzz():
    print()
    while True:
            num_input = input("Enter a limit n for fizzbuzz: ")
            number = valid_number(num_input)    
            if number is not None:
                print(fizzbuzz(number))
                return
            else:
                print("That is not a valid number. Please try again.")
 

def do_is_palindrome():
    print()
    while True:
        str1 = input("Enter a string for a palindrome test: ")
        if valid_string(str1) is not None:
            if is_palindrome(str1):
                print(str1, "is a palindrome.")
            else:
                print(str1, "is not a palindrome.")
            return
        else:
            print("That is not a valid string. Please try again.")


def main():
    do_sieve()
    do_common_characters()
    do_fizzbuzz()
    do_is_palindrome()
    print()


main()

