import unittest
from balance import result_sum_two_digits, ternary_sum, base_10_to_base_3, balance_number

alphabet = ['T', '0', '1']
sum_base_results = [
    'T1',
    'T',
    '0',
    'T',
    '0',
    '1',
    '0',
    '1',
    '1T'
]
class TestBalanceMethods(unittest.TestCase):
    
    def test_result_sum_two_digits(self):
        iterator = 0
        for digit1 in alphabet:
            for digit2 in alphabet:
                result = result_sum_two_digits(digit1, digit2)
                self.assertEqual(result, sum_base_results[iterator])
                iterator += 1

    def test_ternary_sum(self):
        a = "0100"
        b = "10T0"
        result = ternary_sum(a, b)
        self.assertEqual(result, "11T0")

    def test_base_10_to_base_3(self):
        base_10 = 10
        base_3 = "101"
        result = base_10_to_base_3(base_10)
        self.assertEqual(result, base_3)

    def test_balance_number(self):
        base_3_unbalanced = "102"
        base_3_balanced = "11T"
        result = balance_number(base_3_unbalanced)
        self.assertEqual(result, base_3_balanced)


if __name__ == '__main__':
    unittest.main()