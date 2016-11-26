from bottle import route,run
@route('/get/<file_content>')
def get_cintent(file_content):
    print(file_content)
    return 'nice'
run(host='0.0.0.0',port=8080)
