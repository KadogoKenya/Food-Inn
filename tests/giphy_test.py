import unittest
from ..models import Giphy
from app.models import User

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

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)


    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

        def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('banana'))

if __name__ == "__main__":
    unittest.main()

         