print("\n******** Digital Calculator *********")

while True:
    print("\nChoose from the following options:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Quit           (or type q / quit)")

    result = None

    # === Get first number - loop until valid
    while True:
        try:
            num1_str = input("Enter first number: ").strip()
            if num1_str.lower() in ["q","quit"]:
                print("Goodbye!, See you next time!👍")
                print("=" *40)
                exit()
            num1 = float(num1_str)
            break
        except ValueError:
            print("❌ That's not a valid number. Please try again.")

    # === Get operation/choice - loop until valid ===
    while True:
        choice = input("Enter your choice (1/2/3/4/5 or + - * / or q): ").strip()
        if choice.lower() in ["q","quit",'5']:
            print("Goodbye!, See you next time!👍")
            print("=" * 40)
            exit()

     # Convert choice to standard operation symbol
        if choice in ["1", "+"]:
            op = "+"
            break
        elif choice in ["2", "-"]:
            op = "-"
            break
        elif choice in ["3", "*"]:
            op = "*"
            break
        elif choice in ["4", "/"]:
            op = "/"
            break
        else:
            print("❌ Invalid choice. Use 1–5 or + - * / or q")

    # === Get second number - loop until valid ===
    while True:
        try:
            num2_str = input("Enter second number: ").strip()
            if num2_str.lower() in ['q','quit']:
                print("Goodbye!, See you next time!👍")
                print("=" * 40)
                exit()
            num2 = float(num2_str)
            break
        except ValueError:
            print("❌ That's not a valid number. Please try again.")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("❌ Error: Cannot divide by zero!")
            print("=" * 40)
            continue  # go back to main menu
        result = num1 / num2

    print(f"\nResult: {num1} {op} {num2} = {result}")
    print("-" * 40)
