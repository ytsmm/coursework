import webbrowser

"""
Функция запускает веб-страницу с результатами кластеризации в браузере
"""
def Vizualize():
    try:
        webbrowser.open_new_tab('http://127.0.0.1:8080')
    except:
        return 'Please, start up the http-server'
