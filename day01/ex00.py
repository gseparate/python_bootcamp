import unittest
def add_ingot(purse):
    new_purse = dict(purse)
    if new_purse.get("gold_ingots") == None:
        new_purse["gold_ingots"] = 1
    elif isinstance(new_purse.get("gold_ingots"), int):
        new_purse["gold_ingots"] += 1
    else:
        print("type must be integer")
        new_purse = None
    return new_purse

def get_ingot(purse):
    new_purse = dict(purse)
    if (new_purse.get("gold_ingots") == None or 
        new_purse.get("gold_ingots") == 0 or 
        not isinstance(new_purse.get("gold_ingots"), int)):
        print("purse hasn'n gold_ingots or amount of gold_ingots isn't integer")
        new_purse = None
    else:
        new_purse["gold_ingots"] -= 1
    return new_purse

def empty(purse):
    return dict()

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

