import pickle
import notification

# event list in saved_protests.dat will be tuples in form of:
# (title, date, link

def check_reminders():
    events = pickle.load(open("saved_protests.dat", "rb"))

    if not events:
        for event in events:
            notification.check_alert(event[1])