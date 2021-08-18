from selenium import webdriver
import os
from time import sleep

class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome()
        #self.driver.get('https://instagram.com/')
        
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username_input = self.driver.find_element_by_name('username')
        password_input = self.driver.find_element_by_name('password')
        

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_btn = self.driver.find_element_by_xpath('//button[@type="submit"]')
        login_btn.click()
        sleep(8)
        notnow_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        notnow_btn.click()
        sleep(2)

    def search_tag(self, tag):
        """
        Naviagtes to a search for posts with a specific tag on IG.

        Args:
            tag:str: Tag to search for
        """

        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))

   
    def nav_user(self, user):
        """
        Navigates to a users profile page

        Args:
            user:str: Username of the user to navigate to the profile page of
        """

        self.driver.get('https://www.instagram.com/{}/'.format(user))

    
    
    def like_latest_posts(self, user, n_posts, like=True):
        """
        Likes a number of a users latest posts, specified by n_posts.

        Args:
            user:str: User whose posts to like or unlike
            n_posts:int: Number of most recent posts to like or unlike
            like:bool: If True, likes recent posts, else if False, unlikes recent posts

        TODO: Currently maxes out around 15.
        """

        action = 'Like' if like else 'Unlike'
    
        self.nav_user(user)

        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))

        for img in imgs[:n_posts]:
            img.click() 
            time.sleep(1) 
            try:
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(action)).click()
            except Exception as e:
                print(e)

            #self.comment_post('beep boop testing bot')
            self.driver.find_elements_by_class_name('ckWGn')[0].click()

    def like_photo(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(2)
        for i in range(1, 3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)

        #searching for pic link
        hrefs = self.driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs] 
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'photo:' + str(len(pic_hrefs)))
        for pic_href in pic_hrefs:
            self.driver.get(pic_href)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.driver.find_element_by_link_text("Like").click()
                sleep(18)
            except Exception as e:
                sleep(2)





if __name__ == "__main__":
    ig_bot = InstaBot('username', 'password')
    #ig_bot.search_tag('ghana')
    #ig_bot.like_latest_posts('johngfisher', 2, like=True)
    ig_bot.like_photo('ghana')

    #print(ig_bot.username)