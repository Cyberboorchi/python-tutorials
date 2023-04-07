#import requests library
import requests

#the website URL
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
# url = 'https://yts.mx/api/v2/list_movies.json'

url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
result = requests.get(url_link).text
print(result)

# a = requests.get(url,headers)
# print(a.content)

