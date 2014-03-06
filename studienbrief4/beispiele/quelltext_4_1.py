#I. A. a. Violent Python
from winreg import *

def printMACs():
    net = r'SOFTWARE\Microsoft\Windows NT\Current'+\
        r'Version\NetworkList\Signatures\Unmanaged'
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print('\n[*] Networks You have joined.')
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, name, t) = EnumValue(netKey, 4)
            (n, addr, t) = EnumValue(netKey, 5)
            print('\n'+name)
            print(':'.join(['%x' % x for x in addr]))
            CloseKey(netKey)
        except:
            pass
def main():
    printMACs()

if __name__ == "__main__":
    main()