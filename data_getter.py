from selenium import webdriver

#when you run the program in your terminal, make sure that you use python3 -i data_getter.py
#this will make sure that the website doesn't immediately
#executable_path='/usr/local/bin/chromedriver_'
driver = webdriver.Chrome()
class WikiBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": "~/GoogleDrive/PDF-Files-Hackathon", #Change default directory for downloads; this will only work for Kushal so far, working on putting a folder and sharing it with the rest of you guys
            "download.prompt_for_download": False, #To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
        })
        #options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options = options) #make sure that you have the chrome webdriver installed and placed in path
        driver.get("https://simple.wikipedia.org")

    def get_list_articles(self):
        print("hello how are you doing")

    def put_intro_into_txt(self):
        print("mic testing")
    
    def print_current_URL(self):
        driver.implicitly_wait(5)
        print(driver.current_url)

    


#bot = WikiBot()


