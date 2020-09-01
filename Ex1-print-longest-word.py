# Test 1:
# Assert that the dynamic text (the lorem ipsum text block) on the page contains a word at least 10 characters in length.
# Stretch goal:
# Print the longest word on the page.


from lxml import html
import requests

# Get request to url
page = requests.get('https://the-internet.herokuapp.com/dynamic_content')

# extract information from an HTML document.
tree = html.fromstring(page.content)

#This will create a list of lorem ipsum text block
text_view = tree.xpath('//*[@id="content"]/div[*]/div[2]/text()')

longestWord=''
# loop through all text blocks and Print the longest word on the page.
for txValue in text_view:
    words = txValue.split(' ')
    for word in words:
        word = word.rstrip('\n')
        if len(word) >= 10 and len(word) > len(longestWord):
            longestWord = word
print("longest word : " + longestWord)