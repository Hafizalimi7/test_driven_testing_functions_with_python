## Test Driven Metholodgy 

- User can add up numbers
- User can muliptipy numbers 
- User can divide numbers
- User can subtract numbers

- Checks whether password is correct
- Checks whether greeting function return correct response


## Ways To Run Test

- cd [directory]
-  $ python -m unittest test.test_greeting

- Running a single test case or test method:
- Also you can run a single TestCase or a single test method:
- $ python3 -m unittest test.test_greeting.Test_Greet
- $ python3 -m unittest test.test_greeting.Test_Greet.testing_greet
# Running all tests:

- You can also use test discovery which will discover and run all the tests for you, they must be modules or packages named test*.py (can be changed with the -p, --pattern flag):

- cd [directory]
-$ python3 -m unittest discover or python3 -m unittest
