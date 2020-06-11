import logging as log
from enum import Enum
import win32com.client
import time
import datetime as dt


class ActionCode(Enum):
    REPLIED = 102
    REPLIED_ALL = 103
    FORWARDED = 104


def list_folders(outlook_object):
    item_index = 0
    for item in outlook_object:
        yield item_index, item
        item_index += 1

def get_folder_id(outlook_object, name):
    for inx, folder in list_folders(outlook_object.Folders):
        if folder.Name == name:
            return inx


def main():

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    # for inx, folder in list_folders(outlook.Folders[1].Folders):
    #     # iterate all Outlook folders (top level)
    #     print("-" * 70)
    #     print(folder.Name)

    # for inx, subfolder in list_folders(outlook.Folders[1].Folders[1].Folders):
    #     print("(%i)" % inx, subfolder.Name, "=> ", subfolder)
    # setup range for outlook to search emails (so we don't go through the entire inbox)

    last_hour_date_time = dt.datetime.now() - dt.timedelta(hours=1)

    inbox_id = get_folder_id(outlook, "tomas.kabrt@axiscapital.com")
    inbox_folder_id = get_folder_id(outlook.Folders[inbox_id], "Inbox")
    FSISAC_folder_id = get_folder_id(outlook.Folders[inbox_id].Folders[inbox_folder_id], "FSISAC")

    messages = outlook.Folders[inbox_id].Folders[inbox_folder_id].Folders[FSISAC_folder_id].Items

    messages.Sort("[ReceivedTime]", True)
    messages_last_hour = messages.Restrict("[ReceivedTime] >= '" +last_hour_date_time.strftime('%m/%d/%Y %H:%M %p')+"'")

    for message in messages_last_hour:
        print(message.subject)
        print(message.ReceivedTime)

    # messages = inbox.Items
    # message = messages.GetLast()
    # body_content = message.body
    # print body_content

if __name__ == "__main__":
    main()