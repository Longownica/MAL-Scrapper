import random
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def main():

    print('Enter first account name:')
    user1 = input()
    print('Enter second account name:')
    user2 = input()

    url1 = "https://myanimelist.net/animelist/" + user1 + "?status=6"
    url2 = "https://myanimelist.net/animelist/" + user2 + "?status=6"

    #get anime list from first account
    driver = Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.get(url1)
    time.sleep(2)
    element = driver.find_elements(By.CLASS_NAME, "link.sort")
    element = element[4:]

    user1_titles = []
    for i in range(0,len(element)):
        user1_titles.append(element[i].text)
    user1_titles = list(set(user1_titles))
    user1_titles = user1_titles[1:]
    driver.quit


    #get anime list from second account
    driver = Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.get(url2)
    time.sleep(2)
    element = driver.find_elements(By.CLASS_NAME, "link.sort")
    element = element[4:]

    user2_titles = []
    for i in range(0,len(element)):
        user2_titles.append(element[i].text)
    user2_titles = list(set(user2_titles))
    user2_titles = user2_titles[1:]
    driver.quit

    
    #create intersection set of both lists
    final_list = []
    for elem in user1_titles:
        if elem in user2_titles and elem not in final_list:
            final_list.append(elem)

    #results
    print("\n")
    print("You both want to see:")
    print("\n")
    if(len(final_list) == 0):
        print("Nothing ):")
    else:
        for i in range(0, len(final_list)):
            print(" - " + final_list[i])
            print("\n")
        print("I think you should watch: " + random.choice(final_list))
    
if __name__ == '__main__':
    main()
    
