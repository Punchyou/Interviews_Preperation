"""
True for unique, False otherwise

"""


class UniqueCharacters():

    def __init__(self, s):
        self.char_string = s
    
    def find_un_char(self):
        """
        Find if a string contains unique charasters or not.
        """
        seen = set()
        for char in self.char_string:
            if char not in seen:
                seen.add(char)
                continue
            else:
                return False
        return True

s = "aaaabnsmfdpokerg"
s1 = "abtnei"
unique_charasters = UniqueCharacters(s)
unique_charasters.find_un_char()


"""
Solution
Fill out your solution below:
"""


def uni_char(s):
    u = set()
    for c in s:
        if c in u:
            return False
        else:
            u.add(c)
    return True
    pass


# another 1-line solution
def uni_char2(s):
    return len(set(s)) == len(s)



"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)