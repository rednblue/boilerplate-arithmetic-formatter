def arithmetic_arranger(problems, *args):
  
  solutions = False
  arranged_problems = ""
  output = []

  for arg in args:
    solutions = arg

  if len(problems) > 5:
    return "Error: Too many problems."
  
  for problem in problems:
    operator_position = max(problem.find("+"), problem.find("-"))

    if operator_position == -1:
      return "Error: Operator must be '+' or '-'."

    a = problem[0:operator_position-1]
    b = problem[operator_position+2:]

    a_len = len(a)
    b_len = len(b)
    if a_len > 4 or b_len > 4:
      return "Error: Numbers cannot be more than four digits."

    try:
      a = int(a)
      b = int(b)
    except:
      return "Error: Numbers must only contain digits."

    if problem[operator_position] == "+":
      total = a + b
    else:
      total = a - b

    max_len = max(a_len, b_len)

    line1 = str(a) + (" " * 4)
    line2 = problem[operator_position] + str(b) + (" " * 4)
    line3 = "-" * (max_len + 2) + (" " * 4)
    

    output.append([line1, line2, line3])

  for i in range(3):
      for j in range(len(output)):
        arranged_problems += output[j][i]
      arranged_problems += "\n"

  return arranged_problems