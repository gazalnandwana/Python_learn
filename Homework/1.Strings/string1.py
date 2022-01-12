# 1) Ask user to enter a long sentence through console. You have to prepare a report of the the following
  # a) number of words in the sentence (to be done)
  # b) number of characters in the sentence
  # c) total number of spaces in the sentence
  # d) convert the sentence into lowercase
  # e) convert the sentence into uppercase


user_input = input('Tell me about yourself: ')
words = user_input.split(' ')
count = len(words)
print(f'Total number of words are: {count}')
print(f'User entered "{len(user_input)}" number of charaters')
print(f'There are {user_input.count(" ")} number of space in the sentence')
print(f'Sentence are in lower case: {user_input.lower()}')
print(f'Sentence are in upper case {user_input.upper()}')