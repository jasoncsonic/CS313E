#  File: Reducible.py

#  Description: A program that will print out the longest reducible word within a given text file of words.

#  Student Name: Peyton Breech

#  Student UT EID: pb23489

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/27/2019

#  Date Last Modified: 10/29/2019

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96 
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size (s, const):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % const
  stepSize = const - (hash_idx % const)
  return stepSize

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):

  #initial position that the word can be in from hashing
  position = hash_word(s, len(hash_table))

  #if the spot is not empty, then we proceed to see if there is another empty spot within the list for the word
  if (hash_table[position] != " "):
    newPos = step_size(s, 13)

    #while the spot is not empty we will continue to increment our algorithm until we find a new spot for the word
    i = 1
    while (hash_table[(position + newPos * i) % len(hash_table)] != " "):
      i += 1

    #once we find a spot that is empty, we will assign the word to that spot
    hash_table[(position + newPos * i) % len(hash_table)] = s

  #if the initial spot is empty, we will place the word in that spot
  else:
    hash_table[position] = s

# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise

#we pretty much do the same as the insert_word function, except instead of inserting a word, we are comparing all of the spots
# that our current word we are looking for is in the table. If the current word is in the table, we return True, if it is not then we
# will return false 
def find_word (s, hash_table):
  position = hash_word(s, len(hash_table))
  
  if (hash_table[position] == s):
    return True
  
  if (hash_table[position] != " "):
    newPos = step_size(s, 13)
    i = 1
    while (hash_table[(position + newPos * i) % len(hash_table)] != " "):
      if (hash_table[(position + newPos * i) % len(hash_table)] == s):
        return True
      i += 1
  return False
  
# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible (s, hash_table, hash_memo):

  #will first try to see if the word is inside the memo list
  if find_word(s, hash_memo):
    return True

  #if the word is down to one letter then we will return true if it is a correct single letter
  if len(s) == 1:
    return s == "a" or s == "i" or s == "o"

  #loop that will find the "children" words of a word then see if that child word is reducible and continue until wheter or not
  #the word is reducible
  for childWord in children(s, hash_table):
    if is_reducible(childWord, hash_table, hash_memo):
      insert_word(s, hash_memo)
      return True

  return False

#helepr function to find the reducible words, will go through each letter of the word and 
def children(s, hash_table):

  #empty list to store the result of the testing reducible word
  reducible = []

  #loop that will subtract a letter from each word and then take the word through the find_word function to see if it is a reducible word
  for i in range(len(s)):
    childWord = s[:i] + s[i+1:]
    if find_word(childWord, hash_table):
      reducible.append(childWord)
  return reducible

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):

  #empty list to store the longest words if there are multiple
  longestWords = []

  #length of the first word we encounter in the sorted list by length and will know that is the longest length to compare to
  longestLength = len(string_list[0])

  #loop that will check for once we run into a word that is no longer as long as the first word within our list, to return the
  #list of longestWords
  for i in range(len(string_list)):
    if len(string_list[i]) == longestLength:
      longestWords.append(string_list[i])
    else:
      return longestWords

def main():
  # create an empty word_list
  word_list = []

  # open the file words.txt
  with open("words.txt") as f:

      # read words from words.txt and append to word_list
      for word in f:
        curWord = word.strip()
        word_list.append(curWord)

      #appending the smallest letters so that are reducible words will take into account the following single letters
      #approved by TA to be handled this way
      word_list.append("a")
      word_list.append("i")
      word_list.append("o")

  # close file words.txt
  f.close()

  # find length of word_list
  length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  primeNum = length*2
  while (is_prime(primeNum) == False):
    primeNum += 1
  
  # create and empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(primeNum):
    hash_list.append(" ")

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for word in word_list:
    insert_word(word, hash_list)


  # create an empty hash_memo
  hash_memo = []

  # populate the hash_memo with M blank strings
  for i in range(primeNum):
    hash_memo.append(" ")

  # create and empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
    reducible = is_reducible(word, hash_list, hash_memo)
    if reducible:
      reducible_words.append(word)

  #creating an empty list that will be used to sort our reducible_words list by length
  lengthList = []
  for word in reducible_words:
    lengthList.append((len(word), word))
  lengthList.sort(reverse=True)

  #basically replacing the reducible_words list with the lengthList so that we can still use reducible_words in the below functions
  for i in range(len(lengthList)):
    reducible_words[i] = lengthList[i][1]

  # find words of the maximum length in reducible_words
  longestWords = get_longest_words(reducible_words)

  # print the words of maximum length in alphabetical order
  # one word per line
  longestWords.sort()
  for word in longestWords:
    print(word)

# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()