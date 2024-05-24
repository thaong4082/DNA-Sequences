import os.path
from LongestCommonSubstring import *
from LCS import *
from EditDistance import *
from needlemanWunsch import *

def main():
  chosenAlgorithm = 0
  userIsDone = False
  fileIsEmpty = True
  print("Welcome to DNA Sequence Checker!")
  
  # Check if file is empty
  while fileIsEmpty:
    # Check that queryFilename is valid
    queryFilename = input("\nWhat is the name of the file that contains the query sequence? ")
    while not (os.path.isfile(queryFilename)):
      print("File does not exist! Please try again.")
      queryFilename = input("\nWhat is the name of the file that contains the query sequence? ")
  
    # Check that sequenceFilename is valid
    sequencesFilename = input("\nWhat is the name of the file that contains all of the sequences to be searched against the query? ")
    while not (os.path.isfile(sequencesFilename)):
      print("File does not exist! Please try again.")
      sequencesFilename = input("\nWhat is the name of the file that contains all of the sequences to be searched against the query? ")
  
    # Get the query sequence t & check for invalid file format
    with open(queryFilename, 'r') as file:
      t = file.read().replace('\n', '').upper()
      fileIsEmpty = checkFileIsEmpty(t)
      if fileIsEmpty:
        print("Please input a non-empty query file!")
        continue
      elif len(t) == 0 or t[0] == ">": 
        fileIsEmpty = True
        print("Query file is in the wrong format!")
        continue
    
    # Create a dictionary that stores the sequence header as the key and the sequence itself as the value & check for invalid file format
    D = {}
    with open(sequencesFilename, 'r') as file:
      f = file.readlines()
      fileIsEmpty = checkFileIsEmpty(f)
      if fileIsEmpty:
        print("Please input a non-empty sequence file!")
      elif len(f) == 0 or f[0][0] != ">":
        fileIsEmpty = True
        print("Sequence file is in the wrong format!")

  # Parse through the sequence file and add all header-sequence pairs to a dictionary
  for line in f:
    if line[0] == ">":
      seqHeader = line[1:].strip() # sequence header is line without the ">"
      D[seqHeader] = ""
    else:
      D[seqHeader] = D[seqHeader] + line.strip().upper()

  chooseAlgorithm(D, t)

# Check if entire file is empty
def checkFileIsEmpty(f):
  if len(f) == 0:
    return True
  for line in f:
    if line != "\n":
      return False
    if line == f[len(f) - 1]:
      return True

# User chooses an algorithm to use then the results are printed
def chooseAlgorithm(D, t):
  chosenAlgorithm = 0
  userIsDone = False
  
  # Program keeps running until user is done
  while not userIsDone:
    # Ask the user which algorithm to use
    algorithmNames = ["Longest Common Substring", "Longest Common Subsequence", "Edit Distance", "Needleman-Wunsch Algorithm"]
    chosenAlgorithm = 0
    
    # Ask the user which algorithm they want to use and proceed if the input number corresponds to an algorithm
    while not (chosenAlgorithm in [1,2,3,4]):
      print("\nHere is a list of algorithms that can be used to search the sequences:\n1) Longest Common Substring \n2) Longest Common Subsequence \n3) Edit Distance \n4) Needleman-Wunsch Algorithm \n")

      chosenAlgorithm = ""
      while not chosenAlgorithm.isdigit():
        chosenAlgorithm = input("Please choose the number corresponding to the algorithm you would like to use:  ")
        if not chosenAlgorithm.isdigit():
          print("Invalid input. Please try again.\n")
          continue
      chosenAlgorithm = int(chosenAlgorithm)
    
    bestSeqHeader, bestSim = None, None
  
    # Use algorithm corresponding to each number
    if chosenAlgorithm == 1:
      bestSeq, bestSim = findMostSimilarSeq(longestCommonSubstring, t, D)
    elif chosenAlgorithm == 2:
      bestSeq, bestSim = findMostSimilarSeq(LCS, t, D)
    elif chosenAlgorithm == 3:
      bestSeq, bestSim = findMostSimilarSeq(editDistance, t, D)
    elif chosenAlgorithm == 4:
      bestSeq, bestSim = findMostSimilarSeq(needlemanWunsch, t, D)
  
    # Find the corresponding header for the best sequence
    for key in D.keys():
      if D[key] == bestSeq:
        bestSeqHeader = key
  
    print("\nThe most similar sequence using " + algorithmNames[chosenAlgorithm-1] + " is " + bestSeqHeader + " with a score of " + str(bestSim) + ".")

    quitOrContinue = input("\nPress 'Q' to quit or type anything else to continue: ")
    if quitOrContinue.upper() == 'Q':
      userIsDone = True
      print("\nThank you for using the DNA Sequence Checker!")
      

# algorithmName: name of an algorithm's function
# t: a query sequence
# D: dictionary of sequences to be searched
def findMostSimilarSeq(algorithmName, t, D):
  DKeys = D.keys()
  bestSim = float('-inf')
  bestSeq = None
  # Slightly different process for editDistance algorithm
  if algorithmName == editDistance:
    bestSim = float('inf')
    for key in DKeys:
      sim = algorithmName(D[key], t, 0) # 0 is the starting score
      print("Score is " + str(sim) + " for sequence " + str(key))
      if sim < bestSim: # lower score is better
        bestSim = sim
        bestSeq = D[key] # store best s_i sequence
        
  # Needleman Wunsch asks user for gap score      
  elif algorithmName == needlemanWunsch:
    # additional feature: ask user for gap score
    gap_score = input("Enter desired gap penalty score: ")
    gap_score = -abs(int(gap_score))
    for key in DKeys:
      sim = algorithmName(D[key], t, gap_score) # returns length of the best sequence
      print("Score is " + str(sim) + " for sequence " + str(key))
      if sim > bestSim: # higher score is better
        bestSim = sim
        bestSeq = D[key] # store best s_i sequence
        
  # Any other algorithm
  else: 
    for key in DKeys:
      sim = algorithmName(D[key], t) # returns length of the best sequence
      print("Score is " + str(sim) + " for sequence " + str(key))
      if sim > bestSim: # higher score is better
        bestSim = sim
        bestSeq = D[key] # store best s_i sequence

  return bestSeq, bestSim

main()

