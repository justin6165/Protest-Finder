from win10toast import ToastNotifier
from datetime import datetime

# date will come in "(first 3 letters of month) (day)" format
# example: Aug 29
# returns true if this date is today

#set up today
today = datetime.today().date()
today_str = str(datetime.today().date())
month = today.strftime("%b") #gives shortened ver of month
today_reformatted = month + ' ' + today_str[8:]


def check_alert(date):
    return today_reformatted == date


# sends a notification with the protest title and protest link
def send_notification(protest_title, protest_link):
    #protest_title = protest.title
    #protest_link = protest.link

    notif = ToastNotifier()
    notif.show_toast(str(protest_title) + " is today." , "Here is the link to your event: " + str(protest_link))


def check_and_notify(date):
    check_alert(date)
    if check_alert(date) == True:
        send_notification("hi", "henlo")


#thank you for the hard carry 