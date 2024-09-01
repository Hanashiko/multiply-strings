def multiply(num1: str, num2: str) -> str:
    num1_digit: int = int(num1)
    num2_digit: int = int(num2)
    multiplied: int = num1_digit * num2_digit
    return str(multiplied)

def main() -> None:
    print(multiply("2","3"))

if __name__ == "__main__":
    main()