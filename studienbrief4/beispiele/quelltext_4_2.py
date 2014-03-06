def returnDir():
    dirs=['C:\\Recycler\\','C:\\Recycled\\',\
        'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None