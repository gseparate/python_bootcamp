import unittest
class Key:
    passphrase = "zax2rulez"
    def __str__(self) -> str:
        return "GeneralTsoKeycard"
    def __len__(self):
        return 1337
    def __gt__(self, other):
        return (other <= 9000)
    def __getitem__(self, key):
        return 3 if key == 404 else 0
    



class TestCase(unittest.TestCase):
    def test_general(self):
        key = Key()
        self.assertEqual(key.passphrase, "zax2rulez")
        self.assertEqual(str(key), "GeneralTsoKeycard")
        self.assertEqual(len(key), 1337)
        self.assertGreater(key, 9000)
        self.assertEqual(key[404], 3)
            
if __name__ == '__main__':
    unittest.main()