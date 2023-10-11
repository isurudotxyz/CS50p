expression = input("Expression: ").strip()
x , y, z = expression.split(" ")
num2 = float(z)
num1 = float(x)

match y:
  case "/":
    result = num1 / num2
    print(f"{result:.1f}")
  case "+":
    result = num1 + num2
    print(f"{result:.1f}")
  case "-":
    result = num1 - num2
    print(f"{result:.1f}")
  case "*":
    result = num1 * num2
    print(f"{result:.1f}")
  case _:
    print("Invalid usage")