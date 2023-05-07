digits = [1, 3, 4, 5, 10, 25]
ops = ['+', '-', '*', '/']

def operate(x, y, op) -> float:
    return float(x + y) if op == '+' \
      else float(x - y) if op == '-' \
      else float(x * y) if op == '*' \
      else float(x / y) if op == '/' \
      else None

def branch(num, digits, target, hist):
  if digits == []:
    return
  
  for digit in digits: # for every digit (1, ... 25)
    for op in ops: # for every operator (+, -, *, /)
      num_new = operate(num, digit, op) # get the new, operated number
      hist_new = hist.copy()
      digits_new = digits.copy()

      hist_new.append((str(num) + op + str(digit) + "=" + str(num_new)))
      digits_new.remove(digit) # remove the digit that was used in the operation

      if num_new == target:
        print("hist_new: ", hist_new)
        return
      else:
        branch(num_new, digits_new, target, hist_new)

# start the recursion
for digit in digits:
  digits_new = digits.copy()
  digits_new.remove(digit)
  branch(digit, digits_new, 86, [])