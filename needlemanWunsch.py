# t : query sequence
# s : sequence to compare t to

def needlemanWunsch(t, s, gap_score):
  ## unless we want the gap score to be consistent, 
  # gap_score = -1
  match_score = 1
  mismatch_score = -1

  # initialize 2-D array
  m = len(t) + 1
  n = len(s) + 1
  memo = [[0] * n for i in range(m)]

  for i in range(1, m):
    memo[i][0] = memo[i - 1][0] + gap_score
  for j in range(1, n):
    memo[0][j] = memo[0][j - 1] + gap_score

  # filling up memo table
  for i in range(1, m):
    for j in range(1, n):
      #if the characters match or don't match, add accordingly
      if t[i - 1] == s[j - 1]:
        match = memo[i - 1][j - 1] + match_score
      else:
        match = memo[i - 1][j - 1] + mismatch_score

      #score obtained by the left box (inserting gap in seq. t)
      t_gap = memo[i - 1][j] + gap_score

      #score obtained by the upper box (inserting gap in seq. s)
      s_gap = memo[i][j - 1] + gap_score

      memo[i][j] = max(t_gap, s_gap, match)
  ## un-highlight if you want to see the table
  # return memo

  #return the goal which is the bottom right corner of memo table
  goal = memo[-1][-1]
  return goal


# #TESTING
# s = "CGACT"
# t = "CCGAC"
# score = needlemanWunsch(t, s)
# print(score)

## un-highlight if you want to see the table
# memo_table = needlemanWunsch(t, s)
# for row in memo_table:
#     print(row)
