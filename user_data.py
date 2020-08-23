import notice_dialog
import scrapping
import pickle
import notification
import scrapping
import os
import gui


# pickle.dump(LIST_NAME, open(".dat FILE_NAME", "wb"))
# pickle.load(open(".dat FILE_NAME", "rb"))

# executes on start-up
# checks to see if there are reminders for today
def check_reminders():
    try:
        events = pickle.load(open("saved_protests.dat", "rb"))
    except:
        pickle.dump([], open("saved_protests.dat", "wb"))
        return

    if not events:
        for event in events:
            if (notification.check_alert(event.date)):
                notification.send_notification(event.title, event.link)
                events.remove(event)


def update_protests_list():
    try:
        os.remove("nearby_protests_list.dat")
    except:
        pass
    address = get_home_address()
    if address != "":
        pickle.dump(scrapping.generate_protests_list(address), open("nearby_protests_list.dat", "wb"))


def get_nearby_protests_list():
    try:
        protests = pickle.load(open("nearby_protests_list.dat", "rb"))
        return protests
    except:
        return []


def check_new_protest():
    original_protests_list = get_nearby_protests_list()
    if get_home_address() != "" and original_protests_list:
        protests_list = scrapping.generate_protests_list(get_home_address())
        if set(protests_list) - set(original_protests_list):
            notification.protest_nearby_notification("New Protest(s)!", "New protest(s) have appeared in your area!")
            try:
                os.remove("nearby_protests_list.dat")
            except:
                pass
            pickle.dump(protests_list, open("nearby_protests_list.dat", "wb"))


# saves protest information into pre-existing list
def add_protest(protest, layout):
    # check to see if it's already been added
    try:
        events = pickle.load(open("saved_protests.dat", "rb"))
    except:
        events = []
        pickle.dump(events, open("saved_protests.dat", "wb"))

    exists = False
    for event in events:
        if protest.title == event.title:
            exists = True
            break

    if not exists:
        events.append(protest)
        pickle.dump(events, open("saved_protests.dat", "wb"))
        notice_dialog.NoticeDialog("Saved!", False)

    gui.Window.load_saves(layout)


# returns a list containing the User's saved protests
def get_saved_protest_list():
    try:
        events = pickle.load(open("saved_protests.dat", "rb"))
        return events
    except:
        return []


# deletes a protest from the saved protest list given the protest title
def delete_protest(title, layout):

    events = pickle.load(open("saved_protests.dat", "rb"))
    for x in range(len(events)):
        if events[x].title == title:
            print("found it")
            events.pop(x)
            pickle.dump(events, open("saved_protests.dat", "wb"))
            print("Success")
            break
    gui.Window.load_saves(layout)


# saves the home address into a .dat file called "user_address.dat"
# if there already exists a home address. Overwrite the previous address
def add_home_address(address):
    if check_home_address() is False:
        pickle.dump(address, open("user_address.dat", "wb"))
    else:
        os.remove("user_address.dat")
        pickle.dump(address, open("user_address.dat", "wb"))

    update_protests_list()


def check_home_address():
    try:
        pickle.load(open("user_address.dat", "rb"))
        return True
    except:
        return False


# returns the previously saved home address
def get_home_address():
    if check_home_address() is True:
        return "Home Address: " + pickle.load(open("user_address.dat", "rb"))
    else:
        return "No home address set"
