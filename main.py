LOOKUPS = (
    dict(zip("0123456789", (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))),
    dict(zip("0123456789", (0, 2, 4, 6, 8, 1, 3, 5, 7, 9))),
)  # TODO: consider acsii values for the lookup table, simple list instead of dict


def is_valid(digits: str) -> bool:
    return sum(LOOKUPS[i % 2][d] for i, d in enumerate(reversed(digits))) % 10 == 0


def main():
    try:
        assert is_valid("17893729974")
        assert not is_valid("17893729975")
        print("ok")
    except KeyError as k_e:
        print(f"{k_e} is not a valid number")


if __name__ == "__main__":
    main()
