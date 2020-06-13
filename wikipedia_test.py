import wikipediaapi
import requests
#from data_getter import WikiBot

#bot = WikiBot()
simple_wiki = wikipediaapi.Wikipedia('simple')
normal_wiki = wikipediaapi.Wikipedia('en')
page_py = simple_wiki.page('Talk:Green')
print(page_py.summary[:])