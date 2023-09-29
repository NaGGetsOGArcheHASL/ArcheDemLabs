from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Web-программирование, часть 2. Список лабораторных
        </header>
            
            <h1>web-сервер на flask</h1>

        <footer>
            &copy; Дементьев Артур Русланович, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Дементьев Артур Русланович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        
        
        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые 
            базовые возможности.
        </div>
        
        
        <footer>
            &copy; Артур Дементьев, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
