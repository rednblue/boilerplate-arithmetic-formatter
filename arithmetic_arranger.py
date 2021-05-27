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

    line1 = (" " * (max_len - a_len + 2)) + str(a) + (" " * 4)
    line2 = problem[operator_position] + (" " * (max_len - b_len + 1)) + str(b) + (" " * 4)
    line3 = "-" * (max_len + 2) + (" " * 4)
    line4 = (" " * (max_len + 2 - len(str(total)))) + str(total) + (" " * 4)

    output.append([line1, line2, line3, line4])
  
  range_list = 3
  if solutions is True:
    range_list = 4

  for i in range(range_list):
      for j in range(len(output)):
        arranged_problems += output[j][i]
      arranged_problems = arranged_problems[:-4] + "\n"
      

  return arranged_problems[:-1]