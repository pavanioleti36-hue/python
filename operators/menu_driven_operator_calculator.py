def operator_calculator():
    while True:
        print("\n--- Operator Calculator Menu ---")
        print("1. Arithmetic Operations (+, -, *, /, %)")
        print("2. Assignment Operations (+=, -=, *=, /=)")
        print("3. Comparison Operations (==, !=, >, <, >=, <=)")
        print("4. Logical Operations (and, or, not)")
        print("5. Membership Operations (in, not in)")
        print("6. Identity Operations (is, is not)")
        print("7. Bitwise Operations (&, |, ^, <<, >>)")
        print("8. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Addition:", a + b)
            print("Subtraction:", a - b)
            print("Multiplication:", a * b)
            print("Division:", a / b)
            print("Modulus:", a % b)
        elif choice == 2:
            a = int(input("Enter a number: "))
            print("Original:", a)
            a += 5
            print("After += 5:", a)
            a -= 2
            print("After -= 2:", a)
            a *= 3
            print("After *= 3:", a)
            a /= 2
            print("After /= 2:", a)

        elif choice == 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Equal:", a == b)
            print("Not Equal:", a != b)
            print("Greater:", a > b)
            print("Less:", a < b)
            print("Greater or Equal:", a >= b)
            print("Less or Equal:", a <= b)
        elif choice == 4:
            x = True
            y = False
            print("x and y:", x and y)
            print("x or y:", x or y)
            print("not x:", not x)

        elif choice == 5:
            lst = [10, 20, 30, 40]
            num = int(input("Enter a number: "))
            print(num, "in list?", num in lst)
            print(num, "not in list?", num not in lst)

        elif choice == 6:
            a = [1, 2, 3]
            b = a
            c = [1, 2, 3]
            print("a is b:", a is b)
            print("a is c:", a is c)
            print("a is not c:", a is not c)

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Bitwise AND:", a & b)
            print("Bitwise OR:", a | b)
            print("Bitwise XOR:", a ^ b)
            print("Left Shift a<<1:", a << 1)
            print("Right Shift a>>1:", a >> 1)

        elif choice == 8:
            print("Exiting Operator Calculator...")
            break

        else:
            print("Invalid choice! Try again.")
operator_calculator()