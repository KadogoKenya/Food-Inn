import unittest
from .models import food

Food=food.Food

class FoodTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the displayed food list
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_food = Food(1234,'Python Must Be Crazy','2019-10-10')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_food,Food))

if __name__ == "__main__":
    unittest.main()

         