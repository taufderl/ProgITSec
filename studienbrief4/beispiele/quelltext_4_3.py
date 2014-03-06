def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
        "SOFTWARE\Microsoft\Windows NT\CurrentVersion"+\
        "\ProfileList" + '\\' + sid)
        (value, type) = QueryValueEx(key,\
            'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid