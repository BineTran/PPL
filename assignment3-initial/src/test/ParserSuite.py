import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """
                    a: array[2,2] of integer = { {1,3}, {1,4} };
                    c: array[2,2] of integer = { {1,2}, {2,1} };
                    b: integer = a[2];
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_full_vardecl(self):
        """Test full variable declaration"""
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_wrong_full_vardecl(self):
        """Test wrong full variable declaration"""
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program(self):
        """Test simple program"""
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_full_program(self):
        """Test full program"""
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
