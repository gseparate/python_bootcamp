import unittest
import ex00

a = {'gold_ingots': 53}
def decorator_signalization(func):
    def wrap(a):
        print("SQUEAK")
        return func(a)
    return wrap


def add_ingot(purse):
    return ex00.add_ingot(purse)

def get_ingot(purse):
    return ex00.get_ingot(purse)

def empty(purse):
    return ex00.empty(purse)

add_ingot = decorator_signalization(add_ingot)
get_ingot = decorator_signalization(get_ingot)
empty = decorator_signalization(empty)


class TestCase(unittest.TestCase):
    def test_add_item(self):
        a = dict()
        a = add_ingot(a)
        b = add_ingot(a)
        self.assertEqual(b, {"gold_ingots" : 2})
        self.assertEqual(a, {"gold_ingots" : 1})
        a["gold_ingots"] = "1"
        self.assertEqual(add_ingot(a), None)
    
    def test_get_item(self):
        a = dict()
        self.assertEqual(get_ingot(a), None)
        a = add_ingot(a)
        b = get_ingot(a)
        self.assertEqual(b, {"gold_ingots" : 0})
        self.assertEqual(a, {"gold_ingots" : 1})
        self.assertEqual(get_ingot(b), None)
        a = add_ingot(a)
        a = add_ingot(a)
        self.assertEqual(get_ingot(a), {"gold_ingots" : 2})
    
    def test_empty_item(self):
        a = dict({"gold_ingots" : 3000})
        b = empty(a)
        self.assertEqual(b, dict())
        self.assertEqual(a, {"gold_ingots" : 3000})
    
    def test_general(self):
        self.assertEqual(add_ingot(get_ingot(add_ingot(empty({"gold_ingots": 1000, "stones" : 100})))), {"gold_ingots": 1})


if __name__ == '__main__':
    unittest.main()

