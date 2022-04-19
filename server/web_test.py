from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

import time
import pymongo
import random
# connect to mongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.user_list
collection = db.test2

# define the URL
url = 'http://127.0.0.1:5001/'
# max number of test
i_max = 120


def main():
    # set the driver for browser (Microsoft Edge)
    s = Service(r"D:\Edge Driver\msedgedriver.exe")

    i = 0
    while i < i_max:
        # start the driver
        driver = webdriver.Edge(service=s)
        # load the web page according to the URL
        driver.get(url)

        # do something
        start_time = time.perf_counter()
        # get the invocation and response times
        invoke_time = driver.find_element(By.ID, 'invocation')
        response_time = driver.find_element(By.ID, 'response')

        t1 = int(invoke_time.text)
        t2 = int(response_time.text)
        print('inTIME: ' + invoke_time.text + ' ms, INT: ' + str(t1))
        print('reTIME: ' + response_time.text + 'ms')

        num = random.randint(1001, 1010)
        # find the input box for user id and send something
        id_input = driver.find_element(By.ID, 'uid')
        id_input.send_keys(num)

        # find the input box for the password and send something
        psw_input = driver.find_element(By.ID, 'upsw')
        psw_input.send_keys(num)

        # store to MongoDB
        data = {
            'invoke time': t1,
            'response time': t2,
            'user': num
        }
        collection.insert_one(data)
        time.sleep(1)
        # find the login button and click
        button = driver.find_element(By.ID, 'log')
        button.click()
        time.sleep(2)

        if i < i_max - 1:
            driver.close()
        elif i == i_max - 1:
            driver.quit()

        end_time = time.perf_counter()
        time_used = end_time - start_time
        print('[TEST ' + str(i + 1) + '] Time Used: ' + str(time_used) + ' s')
        i += 1

    print('Progress Completed with i = ' + str(i))


if __name__ == '__main__':
    main()
