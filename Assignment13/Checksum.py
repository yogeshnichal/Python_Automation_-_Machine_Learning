import os
import hashlib


def hashfile(Dir_Path,blocksize =1024):
    File = open(Dir_Path, "rb")
    hasher = hashlib.md5()
    buf = File.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = File.read(blocksize)

    File.close()

    return hasher.hexdigest()


def DirectoryDuplicateFiles(Dir_Name):
    if not os.path.isabs(Dir_Name):
        Dir_Name = os.path.abspath(Dir_Name)

    if os.path.isdir(Dir_Name):

        DuplicateFiles = {}
        FilesCount = 0

        for foldername, subfolder, filename in os.walk(Dir_Name):
            for subf in subfolder:
                pass
            for fname in filename:
                print("File inside " + foldername + " is " + fname)
                print(" ")
                fname = os.path.join(foldername, fname)
                checksum = hashfile(fname)
                FilesCount += 1

                if checksum in DuplicateFiles:
                    DuplicateFiles[checksum].append(fname)
                else:
                    DuplicateFiles[checksum] = [fname]

        return DuplicateFiles, FilesCount

def DuplicateFiles(Dir_Name):
    data, filecount = DirectoryDuplicateFiles(Dir_Name)
    return DuplicateFilesList(data), filecount


def DuplicateFilesList(Dir_Name):
    result = list(filter(lambda x: len(x) > 1, Dir_Name.values()))
    lst = []
    filecount = 0

    for outer in result:
        icnt = 0
        for inner in outer:
            icnt += 1
            if icnt >= 2:
                filecount += 1
                lst.append(inner)
        filecount = 0
    return lst

def DeleteDuplicateFiles(Dir_Name):
    lst, filecount = DuplicateFiles(Dir_Name)

    for file in lst:
        os.remove(file)
    return lst, filecount, len(lst)

def ChkFileExists(filename, Cnt=0):

    if not os.path.exists(filename):
        return filename

    elif "_Copy" not in filename:

        Fd1 = filename[0:filename.rfind('.')]
        Fd2 = filename[filename.rfind('.'):]
        newfname = Fd1 + "_Copy" + Fd2
        filename = newfname

    else:
        Fd1 = filename[0:filename.rfind('_Copy')]
        Fd2 = filename[filename.rfind('.'):]
        newfname = Fd1 + "_Copy_" + str(Cnt) + Fd2
        filename = newfname
    Cnt += 1
    return ChkFileExists(filename, Cnt)
