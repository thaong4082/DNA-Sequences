# s: the sequence t is being matched with
# t: query sequence
# score: how well the sequences match by the number of necessary changes (lower number is better)
  # initially 0
  # characters match: +0
  # insertion, deletion, or substitution: +1
def editDistance(s, t, score):
  s_length = len(s)
  t_length = len(t)

  # Create a table c to store the optimal subproblems
  c = []
  for i in range(t_length+1):
    row = []
    for j in range(s_length+1):
        row.append(0)
    c.append(row)

  # Set the base cases
  c[t_length][s_length] = 0 # set bottom right to 0
  for i in range(t_length+1):
    for j in range(s_length+1):
      if i == t_length:
          c[t_length][j] = s_length - j
      if j == s_length:
          c[i][s_length] = t_length - i  

  # Build the subproblem table up one row at a time, starting at the bottom row
  for i in range(t_length - 1, -1, -1):
    for j in range(s_length - 1, -1, -1):
      # Characters match so don't change the score
      if t[i] == s[j]:
        c[i][j] = c[i+1][j+1] 

      # Store the minimum of insert, delete, substitute which each increase score by 1
      else:
        c[i][j] = min(c[i][j+1] + 1, c[i+1][j] + 1, c[i+1][j+1] + 1)

  return c[0][0]
