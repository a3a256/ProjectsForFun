from pathlib import Path
import datetime
import re
import time
import pandas as pd

import win32com.client  #pip install pywin32

def msa_check(x):
    merge = 'stopword1'
    start = 'stopword2'
    stop = 'stopword3'
    if merge in x.lower() and start not in x.lower() and stop not in x.lower():
        return True
    
    return False


# Create output folder
output_dir = Path.cwd() / "Output_merge"
output_dir.mkdir(parents=True, exist_ok=True)

# Connect to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Connect to folder
name = "Some name"
inbox = outlook.Folders(name).Folders("Inbox")
# inbox = outlook.GetDefaultFolder(6)
# https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
# DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

# Get messages
messages = inbox.Items

print("The amount of messages")

print(len(messages))

pdfs = 0

df = pd.read_excel(r"path")

nums = 'Company Reg Number'

vals = df[nums].fillna("").values

start = time.time()
matched = []

for message in messages:
    subject = message.Subject
    body = message.body
    attachments = message.Attachments

    # Create separate folder for each message, exclude special characters and timestampe
    # current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # target_folder = output_dir / re.sub('[^0-9a-zA-Z]+', '', subject) / current_time
    # target_folder.mkdir(parents=True, exist_ok=True)

    # Write body to text file
    # Path(target_folder / "EMAIL_BODY.txt").write_text(str(body))
    flag = False

    for i in vals:
        if str(i) in body and i != "" and "cancel" in body:
            matched += [i]
            print(i)
            break


    # Save attachments and exclude special
    # for attachment in attachments:
    #     title = attachment.FileName
    #     if title.endswith(".pdf"):
    #         if msa_check(title):
    #             pdfs += 1
    #             flag = True
    #             filename = re.sub('[^0-9a-zA-Z\.]+', '', attachment.FileName)
    #             attachment.SaveAsFile(output_dir/title)

end = time.time()

dd = dict()
dd['Cancelled'] = matched
pd.DataFrame(dd).to_excel("Possibly cancelled.xlsx", index=False)

print("Count of pdfs files")

print(len(matched))

print("Time required: {}".format(end-start))