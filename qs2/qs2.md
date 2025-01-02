- Here:- Directly define parameters when you expect a fixed number of arguments and  don't need the flexibility of *
`like the qs2 here -> breadth,height only needed`

# Use of * in Functions

- Packing Arguments (Variable Number of Arguments):-Use *args in a function when you don't know the exact number of arguments that will be passed and want to collect them in a tuple.
- `when we don't know how many args gonna be in calling`
```python
def print_numbers(*args):  # *args is a way to receive any number of arguments
    for number in args:
        print(number)

# Calling function with multiple arguments:
print_numbers(1, 2, 3)
# Output:
# 1
# 2
# 3

```
  
- Passing List/Tuple as Separate Arguments:- Use * to unpack arguments when you're passing a list/tuple as individual arguments to a function.
  ```python
  def add(a, b, c):
    return a + b + c

	numbers = [1, 2, 3]
	# Unpacking the list so its elements are passed as separate arguments:
	result = add(*numbers)  # equivalent to add(1, 2, 3)
	print(result)  # Output: 6 
	```