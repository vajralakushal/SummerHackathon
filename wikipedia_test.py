import wikipediaapi
from data_getter import WikiBot

bot = WikiBot()
wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Python_(programming_language)')
print(page_py.summary[:])
bot.print_current_URL()