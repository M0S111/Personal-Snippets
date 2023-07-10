import unittest
from timed import reg_time

class Timed_tests(unittest.TestCase):
	
	def test_basic(self): #always start method names with test
		testcase = '01:00 AM'
		expected = '01:00'
		self.assertEqual(reg_time(testcase),expected)
		
	def test_empty(self):
		testcase = ''
		expected = 'Nothing Entered!'
		self.assertEqual(reg_time(testcase),expected)
		
		
unittest.main()