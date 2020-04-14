"""
This script solve the problem for the
ternary balance
Author: Daniel Rodriguez
E-mail: danielrs9705@gmail.com
"""

"""
This section is about the arithmetic concerning the balance ternary
"""

"""
The sum_base is a dictionnary that maps the 9 basic sums and their results
this is use to make complex sums in ternary balanced base using as information this
basic sums. Because each complex sums can be express in the end in this nine expressions.
"""
sum_base = {
    'T+T': 'T1',
    'T+0': 'T',
    'T+1': '0',
    '0+T': 'T',
    '0+0': '0',
    '0+1': '1',
    '1+T': '0',
    '1+0': '1',
    '1+1': '1T'
}


def result_sum_two_digits(d1, d2):
    """
    This function return the sum representation of two
    digits
        --d1, d2: Digits to sum represent it as strings
    In here we use the sum base to transform this kind of expression: d1+d2 to a single
    expression that is the result. For example, if d1 = 0 and d2 = 0 then th result is the
    sum_base["0+0"] = '0'. All posible combinations of the sum d1+d2 are in the sum_base dictionnary.
    """
    return sum_base["{}+{}".format(d1, d2)]


def ternary_sum(a, b):
    """
    This function is going to sum to number that are
    balance ternaries and give another balance ternary
        a, b: Strings that represent balance ternaries number to sum
    """
    result = ""
    numbers = [a, b]
    # Sort the numbers by length of theirs string representations
    numbers.sort(key=len, reverse=True)
    numbers[1] = "0"*(len(numbers[0]) - len(numbers[1])) + numbers[1]
    # This two line reverse the numbers to properly sum them from right to left
    #    <--
    #  0100 +
    #  10T0
    # -----
    #  11T0
    # We use in here the sum_base to obtain for each sum of digits
    # 0+0, 0+T, 1+0, 0+1 the results.
    numbers[0] = numbers[0][::-1]
    numbers[1] = numbers[1][::-1]
    carry = ""
    for index, val in enumerate(numbers[0]):
        digit_result = result_sum_two_digits(val, numbers[1][index])
        if (len(carry) != 0):
            digit_result = result_sum_two_digits(val, carry)
            carry = ""

        # In here we see if we get some carry like in the base 10 sum
        # That occurs with to results
        #   - T+T ----> T1
        #   - 1+1 ----> 1T
        if (len(digit_result) == 2):
            carry = digit_result[0]
            digit_result = digit_result[1]
        result = digit_result + result

    return carry + result


def balance_number(number):
    """
    This function balance an number in 
    a base 3 representation
        -- number: String. receives a base 3 unbalanced number
    """
    result = ""
    sums_to_do = []
    count = 0
    # This loops transform all the 2's in 1T's
    # This is to know the sums to do to original number
    for digit in number:
        if (digit == "2"):
            aux = "1T" + ("0"*(len(number) - count - 1))
            sums_to_do.append(aux)
            result += "0"
        else:
            result += digit
        count += 1

    for number in sums_to_do:
        result = ternary_sum(result, number)
    return result


def base_10_to_base_3(number):
    """
    This function take a number on base 10 and return its
    equivalent in base 3 this base 3 is unbalanced. It is unbalanced
    because this base contains the number 2 in its alphabet (0,1,2 --> ternary unbalanced alphabet)
    """
    if (number == 0):
        return "0"
    base_3 = ""
    aux = number
    while (aux != 0):
        digit = aux % 3
        base_3 = str(digit) + base_3
        aux = aux // 3

    return base_3


def balance_the_weight(balanced_ternary, base_number):
    """
    This function provides an answer to
    the problem of balancing given a number
    in base 10
    """
    print("To weight {} in right cup of balance, one needs to place the ternary weights in the left (L) and right (R) as follows:".format(base_number))
    pw = len(balanced_ternary) - 1
    for digit in balanced_ternary:
        if (digit == "1"):
            print("L : {}".format(3**pw))
        elif (digit == "T"):
            print("R : {}".format(3**pw))
        pw -= 1


if __name__ == "__main__":
    try:
        number = int(input())
        if (number <= 0):
            print("This number {} is not allowed to balance it. Putting default: 100".format(number))
            number = 100
        balance_the_weight(balance_number(base_10_to_base_3(number)), number)
    except ValueError:
        print("The input must be an integer")
