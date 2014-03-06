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