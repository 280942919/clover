
from  urllib.request import  urlopen,quote
from  urllib.error import  HTTPError,URLError
import json,time
img = '''
         

               树间朝阳      漫山绿草

             是你一席白裙    向着孩子微笑

           山区校园的红旗下有了你甜美歌声

           颗颗感动的小灵心听着你尊尊教导

             你走遍了乡县把孩子的家寻找

               递上积蓄助他们迈入学校

                 山花编成感激的金环

                   戴上它泪光闪耀

                     你点燃希望

                       向着爱                 

                        拥抱

                         ！


'''
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

str = '''

天上掉钞票我不会弯腰，因为天上馅饼都不会掉，更别说掉钞票了！！！哈哈哈....



        暗梅幽闻花，                        俺没有文化，

         卧枝伤恨底，                    我智商很低，

           遥闻卧似水，                要问我是谁，

             易透达春绿。              头大蠢驴。

               岸似绿,                 俺是驴，

                 岸似透绿,         俺是头驴，

                    岸似透黛绿.俺是头呆驴。
                       。。。。。。。
                         。。。。。
                          。。。。
                           。。。
                            。。
                             。


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
