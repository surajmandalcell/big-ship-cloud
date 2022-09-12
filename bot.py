from selenium import webdriver
from UserAgents import ua as importedUA
# from MainWindows import MainWindow
import threading
import os


# Installing Chrome Drivers
# chromedriver.install() 

drivers = []
bot_count_for_instance = 0
# Bot count for threads to get correct user agent
# ua_index = 0

def bot_count_for_instance_updater(number):
    bot_count_for_instance+int(number)

class EcoBot():
    def __init__(self, link, bot_count, headless_checkbox, bot_multiplier_checkbox, black_video_checkbox):
        self.link = link
        self.bot_count = bot_count
        self.bot_multiplier_checkbox = bot_multiplier_checkbox
        self.headless_checkbox = headless_checkbox
        self.black_video_checkbox = black_video_checkbox
    
    def createChromeBotInstance(self,ua_index):
        driver_path = os.path.join(os.getcwd(),'chromedriver.exe')
        chrome_options1 = webdriver.ChromeOptions()
        
        if self.headless_checkbox == True:
            chrome_options1.add_argument('--headless')
        if self.black_video_checkbox:
            chrome_options1.add_extension('ext.crx')
        chrome_options1.add_argument('--user-agent="' + str(importedUA[ua_index]) + '"')
        
        driver1 = webdriver.Chrome(options=chrome_options1, executable_path=driver_path)
        driver1.get(self.link)
        drivers.append(driver1)
        print("Bot sent, Number : ", len(drivers))

        if self.bot_multiplier_checkbox == True:
        # Second Bot Hit
            # driver_path = os.path.join(os.getcwd(),'chromedriver.exe')
            # chrome_options2 = webdriver.ChromeOptions()
            # chrome_options2.add_extension('ext.crx')
            # chrome_options2.add_argument('disable-popup-blocking')
            # # chrome_options2.add_argument('--headless')
            chrome_options1.add_argument('--user-agent="' + str(importedUA[ua_index+1]) + '"')
            driver2 = webdriver.Chrome(options=chrome_options1, executable_path=driver_path)
            driver2.get(self.link)
            drivers.append(driver2)
            print("Bot sent, Number : ", len(drivers))

        


    def createFirefoxBotInstance(self,ua_index):
        
        extension_path = os.path.join(os.getcwd(),'jp_video_block.xpi')
        driver_path = os.path.join(os.getcwd(),'geckodriver.exe')
        profile1 = webdriver.FirefoxProfile()
        profile1.set_preference("general.useragent.override", str(importedUA[ua_index]))
        options1 = webdriver.FirefoxOptions()
        if self.headless_checkbox == True:
            options1.headless = True
        driver1 = webdriver.Firefox(firefox_profile=profile1, options=options1, executable_path=driver_path)
        if self.black_video_checkbox:
            driver1.install_addon(extension_path)
        driver1.get(self.link)
        drivers.append(driver1)
        print("Bot sent, Number : ", len(drivers))

        if self.bot_multiplier_checkbox == True:
            # Second Bot Hit
            profile1.set_preference("general.useragent.override", str(importedUA[ua_index+1]))
            driver2 = webdriver.Firefox( firefox_profile=profile1, options=options1, executable_path=driver_path)
            if self.black_video_checkbox:
                driver2.install_addon(extension_path)

            driver2.get(self.link)
            drivers.append(driver2)
            print("Bot sent, Number : ", len(drivers))
    
    def createEdgeInstance(self,ua_index):
        # Not satisfied with Edge
        driver_path = os.path.join(os.getcwd(),'msedgedriver.exe')
        
        edge_options1 = webdriver.EdgeOptions()
        # edge_options1.enable_mobile= True
        if self.headless_checkbox == True:
            edge_options1.add_argument('--headless')
        edge_options1.add_argument('--user-agent="' + str(importedUA[ua_index]) + '"')
        driver1 = webdriver.Edge(options=edge_options1, executable_path=os.path.join(os.getcwd(),driver_path))
        driver1.get(self.link)
        drivers.append(driver1)
        print("Bot sent, Number : ", len(drivers))

        if self.bot_multiplier_checkbox == True:
            # Second Bot Hit
            edge_options1.add_argument('--user-agent="' + str(importedUA[ua_index+1]) + '"')
            driver2 = webdriver.Edge(options=edge_options1, executable_path=os.path.join(os.getcwd(),driver_path))
            driver2.get(self.link)
            drivers.append(driver2)
            print("Bot sent, Number : ", len(drivers))

    def createOperaInstance(self,ua_index):
        # Not working at all
        driver_path = os.path.join(os.getcwd(),'operadriver.exe')
        # driver1 = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),driver_path))
        
        opera_options1 = webdriver.ChromiumEdge()
        opera_options1.add_argument('--headless')
        opera_options1.add_argument('--user-agent="' + str(importedUA[ua_index]) + '"')
        driver1 = webdriver.ChromiumEdge(executable_path=driver_path)
        driver1.get(self.link)
        drivers.append(driver1)
        print("Bot sent, Number : ", len(drivers))

        # Second Bot Hit

    def createHtmlInstance(self,ua_index):

        # driver_path = os.path.join(os.getcwd(),'operadriver.exe')
        # driver1 = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),driver_path))
        
        
        # opera_options1.add_argument('--headless')
        # opera_options1.add_argument('--user-agent="' + str(importedUA[ua_index]) + '"')
        driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
        driver.get(self.link)
        drivers.append(driver)
        print("Bot sent, Number : ", len(drivers))

        # Second Bot Hit
        
        

    def run_chrome(self):
        for i in range(self.bot_count):
            thread = threading.Thread(target=self.createChromeBotInstance, args=(len(drivers)+1+i*2,))
            # append len(driver) if there are existing active bots
            thread.start()
            # ua_index+1

        print("Yayy!!! Task Started")

    def run_firefox(self):
        for i in range(self.bot_count):
            thread = threading.Thread(target=self.createFirefoxBotInstance, args=(len(drivers)+1+i*2,))
            # append len(driver) if there are existing active bots
            thread.start()
            # ua_index+1

        print("Yayy!!! Task Started")

    def run_edge(self):
        for i in range(self.bot_count):
            thread = threading.Thread(target=self.createEdgeInstance, args=(len(drivers)+1+i*2,))
            # append len(driver) if there are existing active bots
            thread.start()
            # ua_index+1

        print("Yayy!!! Task Started")

    def run_opera(self):
        for i in range(self.bot_count):
            thread = threading.Thread(target=self.createOperaInstance, args=(len(drivers)+1+i*2,))
            # append len(driver) if there are existing active bots
            thread.start()
            # ua_index+1

        print("Yayy!!! Task Started")

    def run_html(self):
        for i in range(self.bot_count):
            thread = threading.Thread(target=self.createHtmlInstance, args=(len(drivers)+1+i*2,))
            # append len(driver) if there are existing active bots
            thread.start()
            # ua_index+1

        print("Yayy!!! Task Started")


        
    @staticmethod
    def stop():
        print('Self Destruction Started')
        print(f'Ending {len(drivers)} tasks')
        for ele in drivers:
            thread = threading.Thread(target=create_stop_bot_thread, args=(ele,))
            thread.start()
        


class CreateBasicBotThread(threading.Thread):
    # Creates bot per Thread
    def __init__(self, link,bot_multiplier):
        threading.Thread.__init__(self)
        self.bot_multiplier = bot_multiplier
        self.link = link
        self.ua = bot_count_for_instance
        self.driver_len = len(drivers)
        # bot = EcoBot(self.link)
        # bot.createBotInstance(self.driver_len+bot_multiplier)
        for i in range(bot_multiplier):        
        #     print("arg = ", self.driver_len+1+i*2, "driver len =",self.driver_len)
            bot = EcoBot(self.link)
            bot.createBotInstance(self.driver_len+bot_multiplier)
        #     bot = EcoBot(self.link)
        #     bot.createBotInstance(self.driver_len+2+i*2)
      
    # def run(self, ua):
    #     # Get ua_index
    #     for i in range(2):
    #         bot = EcoBot(self.link)
    #         print("ua+i=", ua+i)
    #         bot.createBotInstance(ua+i)









def create_stop_bot_thread(driver):
    driver.quit()
    drivers.remove(driver)