import unittest
from contracts import contract


@contract
def factorize(x):
    """ 
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """ 
        Провіряє, чи при передаваємих аргументах типа float 
        чи str викликає TypeError 
        :return:
        """
        for x in ('string', 1.5):
            with self.subTest(x=x):
                with self.assertRaises(TypeError):
                    factorize(x)

    def test_negative(self):
        """
        Провіряє, чи при передача в функцію factorize 
        від'ємного числа викликає ValueError
        :return:
        """
        for x in (-1, -10, -100):
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        """
        Провіряє, чи при передаванні в функцію 0, 1 
        повертаються відповідні кортежі (0,) i (1,)
        :return:
        """
        for x in (0, 1):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        """
        Перевіряє, чи при передаванні в функцію factorize 
        простих чисел повертаються відповідні кортежі
        :return:
        """
        for x in (3, 13, 29):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        """
        Перевіряє, чи при передаванні в функцію factorize 
        чисел для яких функція повинна повертати кортежі 
        з числом елементів рівним 2
        :return:
        """
        test_cases = (
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11)),
        )
        for x, expected in test_cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), expected)

    def test_many_multipliers(self):
        """
        Перевіряє, чи при передаванні в функцію factorize 
        чисел для яких функція повинна повертати кортежі 
        з числом елементів більшим 2
        :return:
        """
        test_cases = (
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
        )
        for x, expected in test_cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), expected)


if __name__ == "__main__":      
  unittest.main()