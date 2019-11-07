def get_wordlist():
	myFile = open("words.txt", "r")
	words = {line.strip() : 1 for line in myFile}
	myFile.close()
	return (words)

def permutation(a, lo, hi, words, h_memo, word_set):
	if (lo == hi):
		string = ''.join(a)
		if (string in words):
			word_set.add(string)
			h_memo[string] = 1
	else:
		for i in range(lo, hi):
			a[i], a[lo] = a[lo], a[i]
			permutation(a, lo + 1, hi, words, h_memo, word_set)
			a[i], a[lo] = a[lo], a[i]

def ispalindrome(word):
	if(len(word) % 2 == 1):
		word = word[:len(word) // 2] + word[len(word) // 2 + 1:]
		print(word)
	stack = []
	for i in range(len(word)):
		if (len(stack) == 0 or stack[-1] != word[i]):
			stack.append(word[i])
		else:
			stack.pop()
	return(len(stack) == 0)

def flip(pancakes):
    if(len(pancakes) == 1):
        return(pancakes)
    else:
        # find index of largest element
        l_index = pancakes.index(max(pancakes)) 
        # create sub list from largest pancake to top pancake
        s_list = pancakes[l_index:]
        # reverse so that largest pancake is on top
        s_list.reverse()
        # combine pancakes with pancakes that you flipped
        pancakes = pancakes[:l_index] + s_list
        # reverse so that the largest is on bottom-most position
        pancakes.reverse()
        # return list of pancakes[0] (largest element) and the rest of the pancakes flipped
        return([pancakes[0]] + flip(pancakes[1:]))


def main():
	#Question 1
	print("Question 1: WordList as dictionary define largest set of words that are anagrams")
	words = get_wordlist()
	h_memo = {}
	anagram_sets = []
	for word in words.keys():
		if (word not in h_memo and len(word) < 5):
			word_set = set()
			permutation(list(word), 0, len(word), words, h_memo, word_set)
			if (len(word_set) > 1):
				anagram_sets.append(word_set)
	anagram_sets.sort(key=len)
	print(anagram_sets[-1])
	print()

	#Question 2
	print("Question 2: Use a stack implementation to evaulate if a string is a palondrum")
	test = "radar"
	results = ispalindrome(test)
	print(results)

	#Question 7 
	print("Question 7: Pancake Examples")
	pancakes = [23, 17, 3, 9, 11]
	print(pancakes)
	newPancakes = flip(pancakes)
	print(newPancakes)



main()