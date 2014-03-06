# I. A. a. Violent Python (S. 109)
import sqlite3
import os
def printForm(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute('SELECT value, timesUsed, datetime(\
    firstUsed/1000000,\'unixepoch\'), datetime(\
    firstUsed/1000000\,\'unixepoch\') FROM\
    moz_formhistory;')
    print('\n--- Formulardaten --- ')
    for row in c:
        print('Eingabe: ' + str(row[0]) + ' Anzahl: '\
            + str(row[1]) + ' erste Nutzung: ' +\
            str(row[2]) + ' letzte Nutzung: ' +\
            str(row[3]))

def main():
    firefoxfolder = os.environ['appdata']+ \
        '\\Mozilla\\Firefox\\Profiles'

    try:
        firefoxprofiles = os.listdir(firefoxfolder)

        for firefoxprofile in firefoxprofiles:
            printForm(firefoxfolder+'\\'\
            +firefoxprofile+'\\formhistory.sqlite')

    except:
        print('Das Verzeichnis '+firefoxfolder+ \
            ' ist nicht vorhanden.')      

if __name__ == "__main__":
    main()