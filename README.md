# Web Whatsapp Messages Reader

With this script, you can retrieve messages from the  Web Whatsapp. You only need to scan the QR code to log in.After scanning the QR code, run the script again. It will start fetching messages then.It saves the messages to a file named wp_messages.txt.

Installation
To install the libraries, run the following command:

pip install -r requirements.txt

How to use:

1.Example:
wp_messages_crawler.py -n "username" -l (fetches the latest message for the  user "username" or the group "username".) 

2.Example:
wp_messages_crawler.py -n "username" -l7(fetches the last 7 messages for the  user "username" or the group "username".)

3.Example:
wp_messages_crawler.py -n "username" -d 24.10.2024 (retrieves messages for the  user "username" or the group "username" from the specified date and onwards. The date format can be in d.m.y or d/m/y.)

4.Example:
wp_messages_crawler.py -n "username" (retrieves as many messages as it can synchronize.)


The program has been tested with Python 3.13 on the Windows operating system.
Google Chrome must be installed on your computer.

