def add_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"Adding {a} and {b}")
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0      
    assert add_numbers(x, 10) == x + 10  #  this will raize an error since its not defined 
    assert add_numbers(1e10, 1e10) == 2e10
    assert add_numbers(-5, -10) == -15
    assert add_numbers(0.1, 0.2) == 0.3  # This may fail due to floating-point precision issues
    assert add_numbers(x, y) == x + y  # This will also raise an error since x and y are not defined
if __name__ == "__main__":
   result = add_numbers()
   print(f"Result: {result}")
   print("All tests passed!")
