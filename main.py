import os        

path = input("enter file path to rename : ")
checkPath = os.path.exists(path)

if checkPath:
    os.chdir(path)
    files = os.listdir()
    print('files:' + ';'.join(files))

    prefix = input("enter file prefix : ")

    ok = input('are you sure?(y/n)')
    if ok == 'y':
        for i in range(len(files)):
            os.rename(files[i], prefix + str(i) + os.path.splitext(files[i])[1])
        print('success')
    else:
        print('cancel')

else:
    print('path error')

