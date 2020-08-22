import pickle
import notification

# event list in saved_protests.dat will be tuples in form of:
# (title, date, link)

# executes on start-up
# checks to see if there are reminders for today
def check_reminders():
    events = pickle.load(open("saved_protests.dat", "rb"))

    if not events:
        for event in events:
            if (notification.check_alert(event[1])):
                notification.send_notification(event[0], event[2])
                events.remove(event)

# saves protest information into pre-existing list
def add_protest(title, date, link):
    events = pickle.load(open("saved_protests.dat", "rb"))
    protest_event = title, date, link
    events.append(protest_event)
    pickle.dump(events, open("saved_protests.dat", "wb"))

# returns a list containing the User's saved protests
def get_saved_protest_list():
    events = pickle.load(open("saved_protests.dat", "rb"))
    return events

# deletes a protest from the saved protest list given the protest title
def delete_protest(title):
    events = pickle.load(open("saved_protests.dat", "rb"))
    for event in events:
        if event[0] == title:
            events.remove(event)

check_reminders()