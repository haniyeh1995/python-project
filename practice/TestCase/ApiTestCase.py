from TestCase import TestCase
from datetime import datetime

class ApiTestCase(TestCase):
    def __init__(self, test_name: str, api_route: str, test_log: str  = "", related_test_cases=None):
        super().__init__(test_name, test_log, related_test_cases)
        self.api_route = api_route
    
    def run_test(self):
        self.startedTime = datetime.now()
        if "https://" in self.api_route:
            result = True
        else:
            result =  False
        self.finishedTime = datetime.now()
        return result

# test3 = ApiTestCase("apiTest", "https://www.sheypoor.com/s/azarshahr/bicycles", "listing in azarshahr")
# print(test3.run_test())

# test4 = ApiTestCase("apiTest", "http://www.sheypoor.com", "listing in all iran")
# print(test4.run_test())