"""
Now:
    - Simple implementation of the Luhn Algorithm
    - Stick to simple imperative programming

Later:
    - Don't assume that the input is a string of digits, add tests to cover other cases
    - General refactor
    - Consider functional formulation(stream of digits -> map -> reduce)
    - Lookup table 
"""
class LuhnAlgorithm():
    # The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm, 
    # is a simple checksum formula used to validate a variety of identification numbers, 
    # such as credit card numbers, IMEI numbers, National Provider Identifier numbers in the United States, Canadian Social
    def validate_check_digit(payload: str) -> bool:
        pass
    
    def calculate_check_digit(payload: str) -> str:
        pass

    @staticmethod
    def is_valid(payload: str) -> bool:
        total = 0
        for index, d in enumerate(reversed(payload[:-1])): #TODO: ideally avoid slicing # since python creates a new list
            if index % 2 == 0:
                multiplier = 2
            else:
                multiplier = 1
            x = int(d) * multiplier
            xx = x // 10 + x % 10 # sum of digits # by doubling a single digit number, we get a number between 1 and 18(inclusive)
            #for odd digits (single digits) eg: 9 % 10 = 9 # we ge the same number
            total += xx
        check_digit = (10 - (total % 10))
        return check_digit == int(payload[-1])
        

def main():
    
    assert LuhnAlgorithm.is_valid("17893729974") 
    assert not LuhnAlgorithm.is_valid("17893729975")
    print("LuhnAlgorithm tests passed")
    print('ok')
    
if __name__ == "__main__":
    main()



