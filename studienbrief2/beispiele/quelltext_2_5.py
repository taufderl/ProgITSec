# I. A. a. Violent Python S. 111
def printCookies(cookiesDB):
    try:
        conn = sqlite3.connect(cookiesDB)
        c = conn.cursor()
        c.execute('SELECT host, name, value FROM \
        moz_cookies')
        print('\n[*] -- Gefundene Cookies --')
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])
            print('[+] Host: ' + host + ', Cookie: ' + \
            name + ', Wert: ' + value)
    except Exception as e:
        if 'encrypted' in str(e):
            print('\n[*] Fehler beim Lesen der DB')