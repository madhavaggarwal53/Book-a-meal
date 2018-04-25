import unittest
from api import *
from user import User
from caterer import Caterer

class FlaskTestCase(unittest.TestCase):
	"""docstring for FlaskTestCase"""
	def test_create_users(self):
		#Test if any of the entered values are empty
		results = User().signup('', '1234567', 9805)
		self.assertEqual(results, 'Please enter all the details', msg='There is an empty input')

		#Type check the data
		results4 = User().signup(45, 1234567, '9805')
		self.assertEqual(results4, 'Please enter a string value for username and password')

		results5 = User().signup('ian', '1234567', '9805')
		self.assertEqual(results5, 'User Id should be an integer!')

		#Creating a new user
		results1 = User().signup('ian', '1234567', 9805)
		self.assertEqual(results1, 'User successfully created', msg='Successful registration')

		#Checking if the user already exists
		results2 = User().signup('ian', '1234567', 9805)
		self.assertEqual(results2, 'User exists!', msg='The user already exists')

	def test_login_works_well(self):
		#Checking if all inputs are filled
		results = User().login('ian', '')
		self.assertEqual(results, 'Enter both username and password', msg='You need to enter both username and password')

		#Type check the data
		results1 = User().login(45, 1234567)
		self.assertEqual(results1, 'Please enter a string value for username and password')

		#Login error when user is not found
		results3 = User().login('iant', '#234')
		self.assertEqual(results3, 'No such user! Please create an account')

	def test_user_login(self):
		#Creating a new user
		User().signup('test', '1234567', 9805)
		#Correct login from new user
		results = User().login('test', '1234567')
		self.assertEqual(results, 'Loggin successful')

	def test_admin_login(self):
		#Correct login from admin
		results = User().login('admin', 'admin')
		self.assertEqual(results, 'Loggin successful, Welcome Admin')

	def logout(self):
		pass

	def test_post_meal(self):
		#Test if any of the entered values are empty
		results = Caterer().post_meal(1, "", 200, "", "Friday")
		self.assertEqual(results, 'Please enter all the details', msg='There is an empty input')

		#Creating a new meal
		results1 = Caterer().post_meal(1, "Kukutu", 200, "dinner", "Friday")
		self.assertEqual(results1, 'Meal successfully created', msg='Successful addition of meal')

		#Checking if the meal already exists
		results2 = Caterer().post_meal(1, "Kukutu", 200, "dinner", "Friday")
		self.assertEqual(results2, 'Meal exists!', msg='The meal already exists')

	def test_get_meal(self):
		Caterer().post_meal(1, "Kuku", 200, "lunch", "Friday")
		results = Caterer().get_meals()
		self.assertIsInstance(results, list, msg='Incorrect output type')

	def test_edit_meal(self):
		#Creating a new meal
		Caterer().post_meal(1, "Chicken", 200, "dinner", "Monday")

		#Check if meal doesn't exists
		results = Caterer().modify_meal(2, "beef", 200, "dinner", "Tuesday")
		self.assertEqual(results, 'Meal unavailable!', msg='The meal does not exist exists')

		#Modify meal
		results = Caterer().modify_meal(1, "beef", 200, "dinner", "Tuesday")
		self.assertEqual(results, 'Meal modification successful', msg='The meal was modified successfully')

	def test_delete_meal(self):
		#Creating a new meal
		Caterer().post_meal(3, "Chicken", 200, "dinner", "Monday")

		#Check if meal doesn't exists
		results = Caterer().delete_meal(2)
		self.assertEqual(results, 'Meal unavailable!', msg='The meal does not exist exists')

		#Modify meal
		results = Caterer().delete_meal(3)
		self.assertEqual(results, 'Meal Deleted successfully', msg='The meal was deleted successfully')

if __name__ == '__main__':
	unittest.main()