from pathlib import Path
import sys
import time

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename, filereadlines):
    # write file
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def convertMoonReadermrexpt(filename):
    # readfile
    filereadlines = readfile(filename)
    # bookname,author style
    eachcontent = []
    eachcontent.append('# ' + filereadlines[5])
    eachcontent.append('\n\n---')
    for i in range(4, len(filereadlines), 17):
        eachcontent.append('\n\n> ' + filereadlines[i + 12] + '\n\n')
        if filereadlines[i + 11] != '':
            eachcontent.append('**' + filereadlines[i + 11] + '**\n\n')
        # time
        clippingTime = float(filereadlines[i + 9]) / 1000
        clippingTimeTransfered = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clippingTime))
        eachcontent.append('*' + clippingTimeTransfered + '*\n\n')
        eachcontent.append('---')
    eachcontent.append('\n')
    # write file
    writefile(filename, eachcontent)

def main():
    current_dir = Path(__file__).parent
    for file in current_dir.glob('*.mrexpt'):
        convertMoonReadermrexpt(file)

if __name__ == '__main__':
    main()