import unittest

# Load all test files in test directory
loader = unittest.TestLoader()
start_dir = 'test/'
suite = loader.discover(start_dir)

# Run all tests
runner = unittest.TextTestRunner()
runner.run(suite)