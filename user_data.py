import pickle
import notification

# event list in saved_protests.dat will be tuples in form of:
# (title, date, link)

def check_reminders():
    events = pickle.load(open("saved_protests.dat", "rb"))

    if not events:
        for event in events:
            if (notification.check_alert(event[1])):
                notification.send_notification(event[0], event[2])
                events.remove(event)
