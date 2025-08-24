from TestCase import TestCase
from ApiTestCase import ApiTestCase

def main():
    test1 = TestCase("LoginTest", "Checking login functionality")
    print(test1.run_test())  

    test2 = TestCase("SignupTest", "")
    print(test2.run_test())

    test3 = ApiTestCase("apiTest", "https://www.sheypoor.com/s/azarshahr/bicycles", "listing in azarshahr")
    print(test3.run_test())

    test4 = ApiTestCase("apiTest", "http://www.sheypoor.com", "listing in all iran")
    print(test4.run_test())   

    print("Running Tests...\n")
    for test in [test1,test2,test3,test4]:
        result = test.run_test()
        print(f"Result: {result}")
        print(f"Report: {test.report()}")
        
if __name__ == "__main__":
    main()