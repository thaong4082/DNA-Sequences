def LCS(X,Y):
  m = len(X) #length for dimmensions of 2D array
  n = len(Y) #length for dimmensions of 2D array
  L = [[0]*(n+1)for i in range(m+1)] #2D array for storing the LCS values

  #sets vals in row 0 to 0. When the 2nd string doesnt include a character, the LCS is 0
  for i in range(m): 
    L[i][0] = 0
  #sets vals in col 0 to 0. When the 1st string doesnt include a character, the LCS is 0
  for j in range(n):
    L[0][j] = 0
  
  for i in range(1,m+1):
    for j in range(1,n+1):
      if X[i-1] == Y[j-1]: #If chars match, add 1 to the value up and to the left
        L[i][j] = L[i-1][j-1] + 1
      else:#If they dont match take the larger value from above or to the left
        L[i][j] = max(L[i-1][j], L[i][j-1])
  
  
  return L[m][n]#Returns the LCS value
  