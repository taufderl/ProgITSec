# I. A. a. Violent Python (S.103) 
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