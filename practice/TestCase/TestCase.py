from datetime import datetime

class ValidationError(Exception):
    pass

class TestCase:
    def __init__(self, test_name:str, test_log: str = "", related_test_cases= None):
        self.test_name = self.validate_test_name(test_name)
        self.test_log = self.validate_test_log(test_log)
        self.related_test_cases = related_test_cases if related_test_cases else []
        self.startedTime = None
        self.finishedTime = None
    
    def validate_test_name(self, name: str):
        if not isinstance(name, str):
            raise ValidationError ("Test name must be a string!")
        elif len(name) > 50 :
            raise ValidationError ("Test name must not over than 50 characters")
        else:
            return name

    def validate_test_log(self, log: str):
        if not isinstance(log, str):
            raise ValidationError ("Test log must be a string!")
        elif len(log) > 300:
            raise ValidationError ("Test log must not over than 300 characters")
        else:
            return log
    
    def validate_related(self, tests):
        if not isinstance(tests, list):
            raise ValidationError("related tests must be a list")
        for i in tests:
            if not isinstance (i, TestCase):
                raise ValidationError ("All related items must be a type of TestCase")
        return tests
    
    def run_test(self):
        self.startedTime = datetime.now()
        if self.test_name and self.test_log:
            result = True
        else:
            result = False
        self.finishedTime = datetime.now()
        return result

    def report(self):
        return f"{self.test_name} - {self.startedTime} - {self.finishedTime} : {self.test_log}"
    
# test1 = TestCase("LoginTest", "Checking login functionality")
# print(test1.run_test())  

# test2 = TestCase("SignupTest", "")
# print(test2.run_test()) 
