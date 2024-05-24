def longestCommonSubstring(s, t):
  #identify the longest substring that is common to both s and t. The sequence with the longest substring in common will be most similar.

  # get lengths of strings
  n = len(s)
  m = len(t)

  # turn strings into lists
  s_list = list(s)
  t_list = list(t)

  # create a table L to store the optimal subproblems
  L = [[0]*(m+1)for i in range(n+1)]

  # longest length of substring saved here
  longest = 0
  
  # loop through all elements to find substring
  for i in range(1,n+1):
    for j in range(1,m+1):
      if s_list[i-1] == t_list[j-1]: #if chars are equal
        #gets length from diagonally opposite in table and add one
        L[i][j] = L[i-1][j-1]+1 
        longest = max(L[i][j], longest) # check if it is longer than longest already found

  # return how long the longest is
  return longest

#Testing
#s = "ABCDABBBEEFX"
#t = "AAAXYBEEFF"

#s = "XYZHELLOK"
#t = "XBHELLO"
#print(longestCommonSubstring(s, t))