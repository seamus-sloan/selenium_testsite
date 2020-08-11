# Selenium on Test Site

## Setup

1. User should have Python installed (At least version 3.0)
2. User should have Selenium installed (`pip install -U selenium`)
3. User should have Pytest installed (`pip install -U pytest`)

## Execution

`pytest test_home.py --browser=chrome` will execute the tests in test_home.py using chrome

`pytest test_home.py --browser=chrome --verbose --tb=no` will execute the tests in test_home.py using chrome. Will not output the entire pytest traceback messages for errors.

`pytest --browser=chrome --verbose --tb=no` will execute all files marked with `test_*.py` using chrome. Will not output any traceback for errors. 
