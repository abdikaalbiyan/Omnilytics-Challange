import random
import string


class GenerateRandom:
        
    def randomAlphaString(self, start, end):
        random_ranges = random.randint(start, end)
        return ''.join(random.choice(string.ascii_letters) for randomNum in range(random_ranges))
    
    def randomRealNumber(self, start, end):
        return random.uniform(start, end)

    def randomIntegers(self, start, end):
        return random.randint(start, end)
    
    def randomAlphaNum(self, start, end):
        random_ranges = random.randint(start, end)
        alphaNum = string.ascii_letters + string.digits
        alphaNumResult = ''.join((random.choice(alphaNum) for randomNum in range(random_ranges)))
        return alphaNumResult
    
    
