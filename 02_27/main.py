# Use any of virtual environment option,
# install random-word package and 
# create shot python script which would print 
# out 5 random word (names must be all capital letter and sorted.)

from random_word import RandomWords
r = RandomWords()

# Return a single random word
r.get_random_word()
print(f"Try to print: {r}") 