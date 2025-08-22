def display_binary(num):
    """Return a string of binary with prefix and spacing"""
    return f"{num} (bin: {bin(num)})"


def bitwise_menu():
    print("\nBitwise Operations Menu")
    print("1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("4. NOT (~)")
    print("5. Shift Left (<<)")
    print("6. Shift Right (>>)")


def main():
    print("=== Bitwise Operations Demonstrator ===")
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))

    while True:
        bitwise_menu()
        choice = input("Select an operation (1-6) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting program.")
            break

        if choice == '1':
            result = a & b
            print(f"\n{a} & {b} = {display_binary(result)}")

        elif choice == '2':
            result = a | b
            print(f"\n{a} | {b} = {display_binary(result)}")

        elif choice == '3':
            result = a ^ b
            print(f"\n{a} ^ {b} = {display_binary(result)}")

        elif choice == '4':
            print(f"\n~{a} = {display_binary(~a)}")
            print(f"~{b} = {display_binary(~b)}")

        elif choice == '5':
            shift = int(input("Enter shift amount: "))
            print(f"\n{a} << {shift} = {display_binary(a << shift)}")
            print(f"{b} << {shift} = {display_binary(b << shift)}")

        elif choice == '6':
            shift = int(input("Enter shift amount: "))
            print(f"\n{a} >> {shift} = {display_binary(a >> shift)}")
            print(f"{b} >> {shift} = {display_binary(b >> shift)}")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    