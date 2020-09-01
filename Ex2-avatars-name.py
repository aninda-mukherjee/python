# Test 2:
# Assert that the "Punisher" image (silhouette with a skull on his chest) does not appear on the page.  This test may pass or fail on any given execution depending on whether the punisher happens to be on the page.
# Stretch goal:
# Give names to each avatar that can appear on the page and print out each avatars name.


from lxml import html
import requests

# Get request to url
page = requests.get('https://the-internet.herokuapp.com/dynamic_content')

# extract information from an HTML document.
tree = html.fromstring(page.content)

# Capture the full path of the avatar image files.
text_view = tree.xpath('//*[@id="content"]/div[*]/div[1]/img/@src')  

# Add Avatat names in a dictionary 
dict = {} 
dict['Original-Facebook-Geek-Profile-Avatar-1.jpg'] = 'Geeks'
dict['Original-Facebook-Geek-Profile-Avatar-2.jpg'] = 'Katara'
dict['Original-Facebook-Geek-Profile-Avatar-3.jpg'] = 'Punisher'
dict['Original-Facebook-Geek-Profile-Avatar-4.jpg'] = 'Toph Beifong'
dict['Original-Facebook-Geek-Profile-Avatar-5.jpg'] = 'Zuko'
dict['Original-Facebook-Geek-Profile-Avatar-6.jpg'] = 'Iroh'
dict['Original-Facebook-Geek-Profile-Avatar-7.jpg'] = 'Appa'
dict['Original-Facebook-Geek-Profile-Avatar-8.jpg'] = 'Momo'
dict['Original-Facebook-Geek-Profile-Avatar-9.jpg'] = 'Gyatso'
dict['Original-Facebook-Geek-Profile-Avatar-10.jpg'] = 'Pasang'

# function to return key for any value 
def get_key(keyStr): 
    for key, value in dict.items(): 
        if keyStr == key: 
             return value 
    return "Avatar doesn't exist"

# Loo through to Assert that the "Punisher" image does not appear on the page. 
# If it apprard then break from the loop. else call the get_key function to get the avatars name and print
for txValue in text_view:
    avatatFileName=txValue.split('/')[3]
    
    if avatatFileName=="Original-Facebook-Geek-Profile-Avatar-3.jpg":
        print('Punisher Image in this page. Test is failing.')
        break
    else:
        print(get_key(avatatFileName))

