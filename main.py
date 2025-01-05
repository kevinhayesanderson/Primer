"""
Later:
    - Don't assume that the input is a string of digits, add tests to cover other cases
    - Lookup table 
"""


class LuhnAlgorithm:
    # The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm,
    # is a simple checksum formula used to validate a variety of identification numbers,
    # such as credit card numbers, IMEI numbers, National Provider Identifier numbers in the United States, Canadian Social
    def validate_check_digit(self, payload: str) -> bool:
        pass

    def calculate_check_digit(self, payload: str) -> str:
        pass

    def is_valid_imperative(self, payload: str) -> bool:
        total = 0
        for index, d in enumerate(reversed(payload)):
            x = int(d) * (1 + index % 2)
            print(x)
            # 4, 7, 9, 9, 2, 7, 3 ,9, 8, 7, 1
            # 4, 14, 9, 18, 2, 14, 3, 18, 8, 14, 1
            total += x // 10 + x  # 4+1+4+9+1+8+2+1+4+3+1+8+8+1+4+1
        return total % 10 == 0  # 60 % 10 = 0

    # mapping function # sum of digits

    def f_i_d(self, i, d) -> int:
        x = int(d) * (1 + i % 2)
        return x // 10 + x

    def f_args(self, args) -> int:
        i, d = args
        return self.f_i_d(i, d)

    def is_valid_functional(self, payload: str) -> bool:
        return sum(map(self.f_args, enumerate(reversed(payload)))) % 10 == 0

    def is_valid_functional_idiomatic_python(self, payload: str) -> bool:
        # the statement self.f_i_d(i, d) for i, d in enumerate(reversed(payload)) returns a generator expression.
        # A generator expression is similar to a list comprehension, but instead of creating a list,
        # it returns a generator object that produces items one at a time and only when needed.
        # This can be more memory efficient for large datasets.
        return sum(self.f_i_d(i, d) for i, d in enumerate(reversed(payload))) % 10 == 0


def main():
    luhn_algorithm = LuhnAlgorithm()
    for is_valid in (
        luhn_algorithm.is_valid_imperative,
        luhn_algorithm.is_valid_functional,
        luhn_algorithm.is_valid_functional_idiomatic_python,
    ):
        assert is_valid("17893729974")
        assert not is_valid("17893729975")
    print("LuhnAlgorithm tests passed")
    print("ok")


if __name__ == "__main__":
    main()
