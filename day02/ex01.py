import unittest
from collections import Counter
from collections.abc import Iterable
from random import randint

class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
    def play(self, player1, player2):
        player1.acting.clear()
        player2.acting.clear()
        for i in range(self.matches):
            player1.result = (bool(player1), bool(player2))
            player2.result = (bool(player2), bool(player1))
            if(player1 and player2):
                self.registry[player1.__class__.__name__] += 2
                self.registry[player2.__class__.__name__] += 2
            elif(player1 and not player2):
                self.registry[player1.__class__.__name__] -= 1
                self.registry[player2.__class__.__name__] += 3
            elif(not player1 and player2):
                self.registry[player1.__class__.__name__] += 3
                self.registry[player2.__class__.__name__] -= 1
            player1.filling_acting()
            player2.filling_acting()
    
    def varieties(self, random=0):
        vars = [CopyCat(), Cooperator(), Grudger(), Detective(), CopyKitten(), Simpleton(), Cheater(), My(self.matches)]
        if(random):
            vars.append(Random())
        for i in range(len(vars)):
            for j in range(i+1, len(vars)):
                self.play(vars[i], vars[j])

    def top3(self):
        print('\n'.join([i[0] for i in self.registry.most_common(3)]))

class Player:
    def __init__(self):
        self.result = tuple()
        self.acting = list(())
    def filling_acting(self):
        self.acting.append(self.result)

    def __bool__(self):
        return self.behaviour()

    def behaviour(self):
        return bool(randint(0,1))

class CopyCat(Player):
    def behaviour(self):
        return (not self.acting or self.acting[-1][1] == 1)

class Cheater(Player):
    def behaviour(self):
        return False
    
class Cooperator(Player):
    def behaviour(self):
        return True

class Grudger(Player):
    def behaviour(self):
        return bool(not [i[1] for i in self.acting if i[1] == False])
    
class Detective(Player):
    def behaviour(self):
        if(len(self.acting) == 0 or len(self.acting) == 2 or len(self.acting) == 3):
            return True
        elif(len(self.acting) == 1):
            return False
        else:
            if(bool(not [i[1] for i in self.acting if i[1] == False])):
                return False
            else:
                return bool(not self.acting or self.acting[-1][1] == 1)

class CopyKitten(Player):
    def behaviour(self):
        return (len(self.acting) < 2 or (self.acting[-1][1] == True and self.acting[-2][1] == True))
    
class Random(Player):
    def behaviour(self):
        return super().behaviour()

class Simpleton(Player):
    def behaviour(self):
        if(len(self.acting) == 0):
            return True
        elif(self.acting[-1][1] == True):
            return self.acting[-1][0]
        elif(self.acting[-1][1] == False):
            return not self.acting[-1][0]
        
class My(Player):
    def __init__(self, match):
        super().__init__()
        self.matches = match
    def behaviour(self):
        if len(self.acting) == 0 or (len(self.acting) < self.matches - 1 and self.acting[-1][1] == True):
            return True
        elif len(self.acting) == self.matches - 1 or self.acting[-1][1] == False:
            return False

a = Game(5)
a.varieties(1)
a.top3()

class TestCase(unittest.TestCase):
    def test_general(self):
        a = Game(5)
        a.varieties()
        self.assertEqual([i[0] for i in a.registry.most_common(3)], ['My', 'CopyCat', 'Grudger'])
    def test_min(self):
        a = Game(1)
        a.varieties()
        self.assertEqual([i[0] for i in a.registry.most_common(3)], ['Cheater', 'CopyCat', 'Cooperator'])
    def test_long(self):
        a = Game(100)
        a.varieties()
        self.assertEqual([i[0] for i in a.registry.most_common(3)], ['My', 'CopyCat', 'Simpleton'])
if __name__ == '__main__':
    unittest.main()