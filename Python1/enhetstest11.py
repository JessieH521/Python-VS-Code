import unittest

# SVAR FRÅGA 1
def add_two_numbers(num1, num2):
    return num1 + num2

# SVAR FRÅGA 2
def to_uppercase(string):
    return string.upper()

# SVAR FRÅGA 3
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# SVAR FRÅGA 4
def combine_letters(lst):
    return "".join(lst)

# SVAR FRÅGA 5
def return_with_tuple(lst):
    return tuple(lst)



# RÖR EJ
class CustomTestResult(unittest.TextTestResult):
    def addFailure(self, test, err):
        super().addFailure(test, err)
        if "test_add_two_numbers" in str(test):
            print("Fail: Fråga 1")
        elif "test_to_uppercase" in str(test):
            print("Fail: Fråga 2")
        elif "test_check_even_or_odd" in str(test):
            print("Fail: Fråga 3")
        elif "test_combine_letters" in str(test):
            print("Fail: Fråga 4")
        elif "test_return_with_tuple" in str(test):
            print("Fail: Fråga 5")


# ALLA FRÅGOR (RÖR EJ)
class TestMathAndStringFunctions(unittest.TestCase):

    # Fråga 1 
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(3, 4), 7, "Testfall 1 misslyckades: 3 + 4 bör bli 7")
        self.assertEqual(add_two_numbers(-1, 1), 0, "Testfall 1 misslyckades: -1 + 1 bör bli 0")
        self.assertEqual(add_two_numbers(0, 0), 0, "Testfall 1 misslyckades: 0 + 0 bör bli 0")

    # Fråga 2
    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hej"), "HEJ", "Testfall 2 misslyckades: 'hej' bör bli 'HEJ'")
        self.assertEqual(to_uppercase("Sverige"), "SVERIGE", "Testfall 2 misslyckades: 'Sverige' bör bli 'SVERIGE'")
        self.assertEqual(to_uppercase("123"), "123", "Testfall 2 misslyckades: '123' bör förbli '123'")

    # Fråga 3 
    def test_check_even_or_odd(self):
        self.assertEqual(check_even_or_odd(4), "Even", "Testfall 3 misslyckades: 4 bör vara 'Even'")
        self.assertEqual(check_even_or_odd(7), "Odd", "Testfall 3 misslyckades: 7 bör vara 'Odd'")

    # Fråga 4 
    def test_combine_letters(self):
        self.assertEqual(combine_letters(["H", "A", "N", "S"]), "HANS", "Testfall 4 misslyckades: ['H', 'A', 'N', 'S'] bör bli 'HANS'")
        self.assertEqual(combine_letters(["J", "O", "H", "A", "N"]), "JOHAN", "Testfall 4 misslyckades: ['J', 'O', 'H', 'A', 'N'] bör bli 'JOHAN'")
        self.assertEqual(combine_letters([]), "", "Testfall 4 misslyckades: En tom lista bör ge en tom sträng")

    # Fråga 5 
    def test_return_with_tuple(self):
        self.assertEqual(return_with_tuple([1, 2, 3]), (1, 2, 3), "Testfall 5 misslyckades: [1, 2, 3] bör returneras som (1, 2, 3)")
        self.assertEqual(return_with_tuple([10, 20, 30]), (10, 20, 30), "Testfall 5 misslyckades: [10, 20, 30] bör returneras som (10, 20, 30)")
        self.assertEqual(return_with_tuple([]), (), "Testfall 5 misslyckades: En tom lista bör returneras som ()")

# RÖR EJ
if __name__ == '__main__':
    # Anpassa TestRunner för att använda vår egen CustomTestResult
    runner = unittest.TextTestRunner(resultclass=CustomTestResult)
    runner.run(unittest.makeSuite(TestMathAndStringFunctions))
