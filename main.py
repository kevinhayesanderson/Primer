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


class LuhnAlgorithm:
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
        for index, d in enumerate(reversed(payload)):
            x = int(d) * (1 + index % 2)
            print(x)
            # 4, 7, 9, 9, 2, 7, 3 ,9, 8, 7, 1
            # 4, 14, 9, 18, 2, 14, 3, 18, 8, 14, 1
            total += x // 10 + x  # 4+1+4+9+1+8+2+1+4+3+1+8+8+1+4+1
        return total % 10 == 0  # 60 % 10 = 0


def main():

    assert LuhnAlgorithm.is_valid("17893729974")
    assert not LuhnAlgorithm.is_valid("17893729975")
    print("LuhnAlgorithm tests passed")
    print("ok")


if __name__ == "__main__":
    main()
