
from  urllib.request import  urlopen,quote
from  urllib.error import  HTTPError,URLError
import json,time

img1 = '''

           amQQQQga
        _mQP?`  )?$Qg
       _QW'        "Q6
       mQ           )W6 amQQQQQQQQa
      _Qf            4QQP?       ?QQ/
      ]Q[            ]Q'           $Q.
      ]Q[             '            ]Qf
      -Qf                          ]Qf
       4Q                          yQ`
       )Q6                        jQf
        ]Qf                      yQf
         4Q/                   _QQ' 
          4Q/                _jQP
           QQ/             _yQD'
           "$Q,          aQQP'
             QQ/      ajQQ?
             -QQ/  ajQQ?'
               4QQQD?'
                ?!
         

           

'''



url_heads = {
    'english':'http://howtospeak.org:443/api/e2c?user_key=dfcacb6404295f9ed9e430f67b641a8e&notrans=0&text=',
    'japanese':'http://howtospeak.org:443/api/j2c?user_key=dfcacb6404295f9ed9e430f67b641a8e&notrans=0&text=',
    'korean':'http://howtospeak.org:443/api/k2c?user_key=dfcacb6404295f9ed9e430f67b641a8e&notrans=0&text='
}
def compile_url(url_head, word):
    url = url_head + quote(word)
    return url

def get_dict(url):
    try:
        req = urlopen(url,timeout=5)
    except (HTTPError, URLError) as e:
        return False
    jss = req.read().decode()
    js_dict = json.loads(jss)
    return js_dict

def play_str(string, delay=0.05):
    for c in string:
        print(c, end='')
        time.sleep(delay)
    print()

def print_3lang(word):
    for key in url_heads:
        for i in range(10):
            url = compile_url(url_heads[key], word)
            js_dict = get_dict(url)
            if js_dict:
                play_str('---> {0}, chinglish: {1}'.format(js_dict[key],js_dict['chinglish']))
                break
    
if __name__ == '__main__':   
    play_str(img, 0.03)
    play_str(str, 0.009)
    while True:
        word = input('输入: ').strip()
        if word == 'exit':
            break
        print_3lang(word)
    play_str('kk，(｡♥‿♥｡)，你喜欢卡卡这个名字吗！！！', 0.05)
    play_str(img1,0.001)
