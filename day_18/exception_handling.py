x = "10"
y = "0"

try:
    z = int(x) / int(y)
    print("Division Result:", z)
except ZeroDivisionError as e:
    print("Division by zero exception caught:", e)
    z = None
except TypeError as e:
    print("Type error exception caught:", e)
    z = None
except Exception as e:
    print(f"Generic exception caught: {type(e).__name__} - {e}")

print("Program continues execution smoothly...")
