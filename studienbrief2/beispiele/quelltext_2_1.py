#I. A. a. Violent Python (S. 102)
import sqlite3
import os

def printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, \
        country, emails, \
        datetime(profile_timestamp, \
        'unixepoch') FROM Accounts;")
    for row in c:
        print('\n--- Gefundener Account ---')
        print('User: '+str(row[0]))
        print('Skype Username: '+str(row[1]))
        print('Location: '+str(row[2])+','+
            str(row[3]))
        print('Email: '+str(row[4]))
        print('Profile Date: '+str(row[5]))

def printContacts(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city,\
        country, phone_mobile, birthday FROM Contacts;")
    for row in c:
        print('\n\t--- Gefundene Kontakte ---')
        print('\tUser : ' + str(row[0]))
        print('\tSkype Username : ' + str(row[1]))
    if str(row[2]) != '' and str(row[2]) != 'None':
        print('\tLocation : ' + str(row[2]) + ',' \
            + str(row[3]))
    if str(row[4]) != 'None':
        print('\tMobile Number : ' + str(row[4]))
    if str(row[5]) != 'None':
        print('\tBirthday : ' + str(row[5]))

# I. A. a. Violent Python (S.104)
def printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,\
        'unixepoch'), identity FROM calls,\
        conversations WHERE calls.conv_dbid =\
        conversations.id;")
    print('\n\t--- Gefundene Anrufe ---')
    for row in c:
        print('\tTime: '+str(row[0])+\
            ' | Partner: '+ str(row[1]))

def main():
    try:
        standardfolders= set([
            'Content', 'DbTemp', 
            'My Skype Received Files',
            'Pictures', 'shared.lck', 
            'shared.xml', 'shared_dynco',
            'shared_httpfe'])
        skypefolder = os.environ['appdata']+ \
            '\\Skype'
        users = set(os.listdir(skypefolder))- \
            standardfolders

        for user in users:
            skypeDB = skypefolder+'\\'+ \
            str(user)+'\\'+'main.db'
            printProfile(skypeDB)
            printContacts(skypeDB)
            printCallLog(skypeDB)

    except:
        print('Das Verzeichnis '+skypefolder+
            ' ist nicht vorhanden.')              
       
if __name__ == "__main__":
    main()