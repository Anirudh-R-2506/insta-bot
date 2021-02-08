from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from os import listdir
import stdiomask
def un():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    followers = ()
    following = ()
    class UnfollowBot:
        def __init__(self,user,pwd):
            self.browserprofile = webdriver.ChromeOptions()
            self.browserprofile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            self.browser = webdriver.Chrome(listdir('C:/Program Files (x86)/Google/Chrome/Application')[0][:9]+'.exe', chrome_options=self.browserProfile)
            sleep(1)
            self.username = user
            self.password = pwd
        def unfollow(self):
            self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            sleep(1)
            user = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
            user.send_keys(keys.CONTROL + "a")
            user.send_keys(Keys.DELETE)
            user.send_keys(self.username)
            sleep(1)
            pword = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
            pword.send_keys(Keys.CONTROL + "a")
            pword.send_keys(Keys.DELETE)
            pword.send_keys(self.password)
            sleep(1)
            login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
            login.click()
            sleep(1)
            print("[*]SUCCESFULLY LOGGED IN[*]")
            profile = self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
            profile.click()
            sleep(1)
            followers_button = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
            number1 = int(followers_button.text)
            follwers_button.click()
            sleep(1)
            xp1 = "/html/body/div[4]/div/div[2]/ul/div/li["
            xp2 = "]/div/div[1]/div[2]/div[1]/a"
            for i in range(1,number1+1):
                xpa = xp1 + str(i) + xp2
                followerz = self.browser.find_elements_by_xpath(xpa)
                followers += followerz.text,
                self.browser.execute_script("window.scrollby(0,100);")
            following_button = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
            number2 = int(following_button.text)
            following_button.click()
            sleep(1)
            xp3 = "/html/body/div[4]/div/div[2]/ul/div/li["
            xp4 = "]/div/div[2]/div[1]/div/div/a"
            for i in range(1,number2 + 1):
                xpa1 = xp3 + str(i) + xp4
                following += self.browser.find_elements_by_xpath(xpa1).text,
                if i==1:
                    self.browser.find_elements_by_xpath(xpa1).click()
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
                    sleep(1)
                    follow_button.click()
                    sleep(1)
                    unfollow_button = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]")
                    sleep(1)
                    unfollow_button.click()
                    sleep(1)
                print("[*]ACCOUNTS UNFOLLOWED[*]\n")
                print(file.read())
                file.close()
    unfollows = UnfollowBot(usr,pwod)
    unfollows.unfollow()
def exit():
    print('\n\n\nHAVE A NICE DAY :)')
    input('PRESS ANY KEY TO QUIT THE BOT...')
try:
    chromedriver_path = 'chromedriver.exe'#DOWNLOAD THE CHROMEDRIVER FOR YOUR CHROME VERSION AND PLACE IT IN THE SAME FOLDER AS THIS PROGRAM
    webdriver = webdriver.Chrome(listdir('C:/Program Files (x86)/Google/Chrome/Application')[0][:9]+'.exe')
    sleep(1)
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    usr ='12e_memes_' #str(input('[*]ENTER YOUR USERNAME[*] '))
    pwd = 'devaraj'#stdiomask.getpass(prompt="[*]ENTER YOUR PASSWORD[*] ")
    sleep(1)
    username = webdriver.find_element_by_name('username')
    username.send_keys(Keys.CONTROL + "a")
    username.send_keys(Keys.DELETE)
    username.send_keys(usr)
    sleep(1)
    password = webdriver.find_element_by_name('password')
    password.send_keys(Keys.CONTROL + "a")
    password.send_keys(Keys.DELETE)
    password.send_keys(pwd)
    sleep(1)
    login = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    login.click()
    sleep(1)
    hashtags1 = str(input('\n\n[*] ENTER HASHTAGS WHICH ARE RELEVENT TO YOUR TOPIC '))#('nature','photographers','like4like','picoftheday','photooftheday','instagood','photography','sunset','photographylovers','photographyeveryday')#TYPE ALL THE HASHTAGS WHICH YOU WANT HERE
    hashtags=hashtags1.split(' ')
    followed = ()
    tag = -1
    follow = 0
    likes = 0
    comments = 0
    
    for hashtag in hashtags:
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/'+ hashtags[tag] + '/')
        sleep(1)
        first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

        first_thumbnail.click()
        sleep(randint(1,2))
        try:
            for x in range(1,200):
                username = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text

                if username not in prev_user_list:

                    if webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                        webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                        followed+=username,
                        follow += 1


                        button_like = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

                        button_like.click()
                        likes += 1
                        sleep(randint(18,25))


                        comm_prob = randint(1,20)
                        print('{}_{}: {}'.format(hashtag, x,comm_prob))
                        if comm_prob > 7:
                            comments += 1
                            webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                            comment_box = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                            if (comm_prob < 7):
                                comment_box.send_keys('Really cool!')#TYPE IN ALL THE COMMENTS YOU WANT TO GIVE IN ALL THESE SEND_KEYS FIELDS (MINIMUM 9 OR 10)
                                sleep(1)
                            elif (comm_prob > 6) and (comm_prob < 9):
                                comment_box.send_keys('Nice work :)')
                                sleep(1)
                            elif comm_prob == 9:
                                comment_box.send_keys('Fantastic gallery!!')
                                sleep(1)
                            elif comm_prob == 10:
                                comment_box.send_keys('So cool! :)')
                                sleep(1)
                            elif comm_prob >10 and comm_prob <14:
                                comment_box.send_keys('Absolutely mindblowing!')
                                sleep(1)
                            elif comm_pob >=14 and comm_prob <= 17:
                                comment_box.send_keys('Great work :)')
                                sleep(1)
                            elif comm_prob == 18:
                                comment_box.send_keys('Great Gallery :)')
                                sleep(1)
                            elif comm_prob == 19:
                                comment_box.send_keys('Cool work :)')
                                sleep(1)
                            elif comm_prob == 20:
                                comment_box.send_keys('Hats off to you...')
                                sleep(1)
                            comment_box.send_keys(Keys.ENTER)
                            sleep(randint(22,28))


                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(25,29))
                else:
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(20,26))
        except:
            continue
    file = open("db.txt","w+")

    file.write("[*]PEOPLE FOLLOWED[*]\n"+followed)
    file.write("[*]POSTS LIKED[*]\n"+likes)
    file.write("[*]POSTS COMMENTED ON[*]\n"+comments)

    print("[*]DO YOU WANT TO START THE UNFOLLOWING BOT NOW?(Y/N)[*] ",end='')
    choice = input()
    if choice.upper() != 'Y':
        print("[*]QUITTING THE BOT[*]")
        print(exit())
    if choice.upper() == 'Y':
        print(un())

except KeyboardInterrupt:
    print('\n[*]YOU HAVE STOPPED THE BOT[*]')
    print(exit())
