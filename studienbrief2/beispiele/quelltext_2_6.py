# I. A. a. Violent Python S. 111
def printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/\
            1000000, 'unixepoch') from moz_places,\
            moz_historyvisits where visit_count >\
            0 and moz_places.id==moz_historyvisits.\
            place_id;")
        print('\n[*] -- Browser History --')
        for row in c:
            url = str(row[0])
            date = str(row[1])
            print('[+] ' + date + ' - Visited: ' + url)
    except Exception as e:
        if 'encrypted' in str(e):
            print('\n[*] Fehler beim Lesen der DB')
        exit(0)