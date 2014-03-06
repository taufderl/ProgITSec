#I. A. a. Violent Python
import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', '')
        print('\n[*] ' + str(hostname) +\
            ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except:
        print('\n[-] ' + str(hostname) +\
        ' FTP Anonymous Logon Failed.')
        return False
host = '127.0.0.1'
anonLogin(host)