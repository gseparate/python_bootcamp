import unittest

def split_booty(*args):
    result = tuple()
    middle_ariphmetic = sum(i.get("gold_ingots") for i in args if "gold_ingots" in i)
    module = middle_ariphmetic % len(args)
    middle_ariphmetic //= len(args)
    for i in range(len(args)):
        if(module):
            result += ({"gold_ingots":middle_ariphmetic+1},)
            module -= 1
        else:
            result += ({"gold_ingots":middle_ariphmetic},)
    return result


class TestCase(unittest.TestCase):
    def test_general(self):
        self.assertEqual(split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}),
                         ({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1}))
        
    def test_addition(self):
        self.assertEqual(split_booty({"gold_ingots": 45}, {"gold_ingots": 10}, {"gold_ingots": 4},{"gold_ingots": 100}, {"gold_ingots": 56}, {"gold_ingots": 99}),
                         ({'gold_ingots': 53}, {'gold_ingots': 53}, {'gold_ingots': 52}, {'gold_ingots': 52}, {'gold_ingots': 52}, {'gold_ingots': 52}))

if __name__ == '__main__':
    unittest.main()

