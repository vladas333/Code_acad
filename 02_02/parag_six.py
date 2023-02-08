# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.

# gyveno karta nykstukas su kepure
# mazas mazas medis auga miske
# zalia zole kuri yra pjaunama
# varztas medvarstis sraigtas ir namas
# baltas popieriaus lapas suristas virvele

sent_one = input('Please insert first sentence in 5 words: ').split(' ')
sent_two = input('Please insert second sentence in 5 words: ').split(' ')
sent_three = input('Please insert third sentence in 5 words: ').split(' ')
sent_four = input('Please insert fourth sentence in 5 words: ').split(' ')
sent_five = input('Please insert fifth sentence in 5 words: ').split(' ')

#
print(sorted(sent_one, reverse=True))
print(sorted(sent_two, reverse=True))
print(sorted(sent_three, reverse=True))
print(sorted(sent_four, reverse=True))
print(sorted(sent_five, reverse=True))

