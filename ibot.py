def un():#FOR UNFOLLOWING
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from time import sleep

    followers = ()
    following = ()

    class UnfollowBot:
        def __init__(self,user,pwd):
            self.browserprofile = webdriver.ChromeOptions()
            self.browserprofile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
            sleep(2)
            self.username = user
            self.password = pwd
        def unfollow(self):
            self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            sleep(5)
            user = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
            user.send_keys(keys.CONTROL + "a")
            user.send_keys(Keys.DELETE)
            user.send_keys(self.username)
            sleep(5)
            pword = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
            pword.send_keys(Keys.CONTROL + "a")
            pword.send_keys(Keys.DELETE)
            pword.send_keys(self.password)
            sleep(5)
            login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
            login.click()
            sleep(3)
            print("[*]SUCCESFULLY LOGGED IN[*]")
            profile = self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
            profile.click()
            sleep(5)
            followers_button = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
            number1 = int(followers_button.text)
            follwers_button.click()
            sleep(3)
            xp1 = "/html/body/div[4]/div/div[2]/ul/div/li["
            xp2 = "]/div/div[1]/div[2]/div[1]/a"
            for i in range(1,number1+1):
                xpa = xp1 + str(i) + xp2
                followerz = self.browser.find_elements_by_xpath(xpa)
                followers += followerz.text,
                sleep(1)
            following_button = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
            number2 = int(following_button.text)
            following_button.click()
            sleep(3)
            xp3 = "/html/body/div[4]/div/div[2]/ul/div/li["
            xp4 = "]/div/div[2]/div[1]/div/div/a"
            for i in range(1,number2 + 1):
                xpa1 = xp3 + str(i) + xp4
                followingz = self.browser.find_elements_by_xpath(xpa1)
                following += followingz.text,
                sleep(1)
            print("[*]COMPARING FOLLOWERS AND FOLLOWING LIST[*]")
            count1 = 0
            count2 = 0
            not_following = ()
            for a in following:
                if a in followers:
                    count1 += 1
                else:
                    count2 += 1
                    not_following += a,
            print('[*]',count1,'ARE FOLLOWING YOU[*]\n[*]',count2,'ARE NOT FOLLOWING YOU[*]\n\n[*]UNFOLLOW THEM?(Y/N)[*]',end='' )
            choice = input()
            if choice.upper() == 'N':
                print('[*]QUITTING THE UNFOLLOW BOT[*]')
                return '[*]THANK YOU FOR USING OUR SERVICE[*]'
            else:
                print('[*]UNFOLLOWING',count2,'PEOPLE[*]')
                file = open("unfollowed.txt","w+")
                for a in not_following:
                    file.write(a + '\n')
                    url = "https://instagram.com/" + a + "/"
                    self.browser.get(url)
                    follow_button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
                    sleep(2)
                    follow_button.click()
                    sleep(3)
                    unfollow_button = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]")
                    sleep(2)
                    unfollow_button.click()
                    sleep(3)
                print("[*]ACCOUNTS UNFOLLOWED[*]\n")
                print(file.read())
                file.close()
    unfollows = UnfollowBot(usr,pwod)

    unfollows.unfollow()
def exit():#FOR EXITING
    print('\n\n\n[*]LOG FILE[*]')
    f = open("db.txt","r")
    print(f.read())
    print('\n\n\nHAVE A NICE DAY :)')
    input('PRESS ANY KEY TO QUIT THE BOT...')
