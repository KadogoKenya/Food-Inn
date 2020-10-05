import unittest
from models import Giphy

Giphy=giphy.Giphy

class GiphyTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the displayed food list
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_giphy = Giphy(1234,'Python Must Be Crazy','2019-10-10')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_giphy,Giphy))

if __name__ == "__main__":
    unittest.main()

         