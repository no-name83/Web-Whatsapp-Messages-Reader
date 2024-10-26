import argparse
import locale
import os
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)
from webdriver_manager.chrome import ChromeDriverManager
def write_messages(messages):
    with open("wp_messages.txt", 'w') as file:
        for message in messages:
            file.write(message+"\n")

def chrome_options():
        chrome_options = Options()


        chrome_options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")


        return chrome_options


browser = webdriver.Chrome(

                options=chrome_options()
            )



parser = argparse.ArgumentParser(description='')
parser.add_argument('-l', type=int, nargs='?', const=1, help='Shows the last message or the specified number of last messages.')
parser.add_argument('-d', type=str, help='Date Format=(d.m.y) or (d/m/y)')
parser.add_argument('-n', type=str, required=True, help='wp username or wp group name')

args = parser.parse_args()


browser.get("https://web.whatsapp.com/")
browser.maximize_window()

print("Please Wait...")
try:
    time.sleep(15)

    user_name = args.n
    user = browser.find_element(By.XPATH, f"//span[@title='{user_name}']")
    user.click()
    print("User Found")
    time.sleep(15)
    try:
        messages = browser.find_elements(By.CLASS_NAME, 'copyable-text')
        myname_messages = []
        locale.setlocale(locale.LC_TIME, '')
        current_format = "%d.%m.%Y" if datetime.now().strftime("%x").count('.') == 2 else "%d/%m/%Y"
        filter_date = None
        filtered_records = []

        if messages:
            for message in messages:
                message_text = message.text
                time_stamp = message.get_attribute('data-pre-plain-text')
                if message_text is not None and time_stamp is not None:
                    combined_message = f"{time_stamp} - {message_text}"
                    if combined_message not in myname_messages:
                        myname_messages.append(combined_message)
            if args.d:
                try:
                    filter_date = datetime.strptime(args.d, current_format)
                except ValueError:
                    print("Date format is not correct.")
            #Get all messages
            if args.l is None and filter_date is None:
                for record in myname_messages:
                    print(record)
                    filtered_records.append(record)
                    write_messages(filtered_records)
            else:
                if args.l:
                    last_n = args.l if args.l > 0 else 1
                    print(f"Last {last_n} messages:")
                    for record in myname_messages[-last_n:]:
                        print(record)
                        filtered_records.append(record)
                        write_messages(filtered_records)
                if filter_date:
                    print(f" Messages after the date:{filter_date.strftime('%d.%m.%Y')}")
                    for record in myname_messages:
                        time_str = record.split(' - ')[0]

                        try:
                            time_str = time_str.split('[')[1].split(']')[0]
                            message_date = datetime.strptime(time_str, "%H:%M, %d.%m.%Y")
                            if message_date > filter_date:
                                print(record)
                                filtered_records.append(record)
                                write_messages(filtered_records)
                        except Exception as e:
                            print(f"Date format error: {e}")

        else:
            print("Messages not found.")
    except Exception as e:
        print(f"Error: {e}")

    browser.quit()







except Exception as e:
    print("Please scan qr code")
    time.sleep(35)

    browser.quit()







