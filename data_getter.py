from selenium import webdriver

#when you run the program in your terminal, make sure that you use python3 -i data_getter.py
#this will make sure that the website doesn't immediately
#executable_path='/usr/local/bin/chromedriver_'
class WikiBot:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": "~/GoogleDrive/PDF-Files-Hackathon", #Change default directory for downloads
            "download.prompt_for_download": False, #To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
        })
        driver = webdriver.Chrome(options = options) #make sure that you have the chrome webdriver installed and placed in path
        driver.get("https://simple.wikipedia.org")

    def get_list_articles(self):
        print("hello how are you doing")

    


bot = WikiBot()

