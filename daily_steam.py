#! python 3

import requests
import bs4
import re
import smtplib
import time

na = re.compile(r"N(/)?A")
numbers = re.compile(r"(\d*)(\W)(\s)(\W)(\d*)(\W?)+(\d*?)(\W)+")

todaysdate = time.strftime("%m/%d/%Y")
sender_email = #sender's email here
receiver_email = #receiver's email here

steam = requests.get('https://steamspy.com')
if steam.raise_for_status() != None:
    print('Steamspy is down.')
    pass

steam_data = bs4.BeautifulSoup(steam.text)

def get_steam():
    '''Gets the Steam Rank, the title, the Score, the User Score, and the Metascore from SteamSpy. Checks to see if the list has any "N/A." '''
    for element in steam_data.find_all("td", {"class" : "t768"}):
            if na.search(str(element.contents)) == None and (int(numbers.search(str(element.contents)).group(1)) > 88 and int(numbers.search(str(element.contents)).group(5)) > 80): #Can tweak these numbers
                if int(numbers.search(str(element.contents)).group(7) != ''):             
                    yield (element.parent.find_all("td")[0].text, element.parent.find_all("td")[1].text, int(numbers.search(str(element.contents)).group(1)),
                           int(numbers.search(str(element.contents)).group(5)), int(numbers.search(str(element.contents)).group(7)))
                else:
                    yield (element.parent.find_all("td")[0].text, element.parent.find_all("td")[1].text, int(numbers.search(str(element.contents)).group(1)),
                           int(numbers.search(str(element.contents)).group(5)), None)
def get_body():
    '''Saves the messages from the function "get_steam".'''
    message = ''
    for rank, title, scorerank, userscore, meta in get_steam():
        message+=(str('Rank: {0}, Title:{1}, Score Rank: {2}, User\'s Score: {3}, Metascore: {4}\n').format(rank,title,scorerank,userscore,meta))
    return message

def use_email(email_message):
    '''Uses the sender's email address to forward the trending list to the designated email address.'''
    #Refer to the sender's email web service's SMTP protocol
    #Below is an example of outlook/hotmail's SMTP address
    sm = smtplib.SMTP('smtp-mail.outlook.com', 587) 
    if sm.starttls()[0] != 220:
        sm.quit()
        print('Failed to start TLS connection.')
    else:
        sender_password = str(input('What is the login password? '))
        if sm.login(sender_email, sender_password)[0] != 235:
            sm.quit()
            print('Failed to login, so just quitting.')
        else:
            letter = '''Subject:{0} SteamSpy Trending List
            
            Here is the list:
            {1}'''.format(todaysdate, email_message)
            
            sm.sendmail(sender_email, receiver_email, letter)
            print('Finished.')
            sm.quit()

def main():
    body = get_body()
    use_email(body)

main()