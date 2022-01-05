# 1) Ask user to enter a long sentence through console. You have to prepare a report of the the following
  # a) number of words in the sentence (to be done)
  # b) number of characters in the sentence
  # c) total number of spaces in the sentence
  # d) convert the sentence into lowercase
  # e) convert the sentence into uppercase


user_input = input('Tell me about yourself: ')
words = user_input.split(' ')
count = len(words)
# space = user_input.count(' ')
print(f'There are "{user_input.count(" ")}" spaces in the sentence.')
print('The words in the sentence are: ', count)
print(f'The number of characters are : {len(user_input)}')
print(f'Sentence in lower case : {user_input.lower()}')
print('Sentence in upper case :', user_input.upper())