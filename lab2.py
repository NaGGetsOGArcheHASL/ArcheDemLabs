from flask import Blueprint, redirect, url_for
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example') 
def example():
   name = 'Артур Дементьев'
   numberlab = 2
   group = 'ФБИ-12'
   course = 3
   fruits = [
    {'name': 'Яблоки', 'price': 100},
    {'name': 'Груши', 'price': 120}, 
    {'name': 'Апельсины', 'price': 150}, 
    {'name': 'Мандарины', 'price': 180}, 
    {'name': 'Манго', 'price': 210}
    ]

   books = [
      {'name': '1984', 'autor': 'Джордж Оруэлл','page': 328, 'Genre': 'Научная фантастика', 'price': 613},

      {'name': 'Преступление и наказание', 'autor': 'Федор Достоевский','page': 672, 'Genre': 'Классика', 'price': 505},

      {'name': 'Гарри Поттер и философский камень', 'autor': 'Джоан Роулинг','page': 256, 'Genre': 'Фэнтези', 'price': 500},

      {'name': 'Три товарища', 'autor': 'Эрих Мария Ремарк','page': 480, 'Genre': 'Роман', 'price': 1035},

      {'name': 'Улисс', 'autor': 'Джеймс Джойс','page': 732, 'Genre': 'Современная классика', 'price': 1095},

      {'name': 'Война и мир', 'autor': 'Лев Толстой','page': 1225, 'Genre': 'Классика', 'price': 350},

      {'name': 'Гордость и предубеждение', 'autor': 'Джейн Остин','page': 432, 'Genre': 'Роман', 'price': 840},

      {'name': '451 градус по Фаренгейту', 'autor': 'Рэй Брэдбери','page': 256, 'Genre': 'Научная фантастика', 'price': 350},

      {'name': 'Гамлет', 'autor': 'Уильям Шекспир','page': 288, 'Genre': 'Драма', 'price': 380},

      {'name': 'Игра престолов', 'autor': 'Джордж Мартин','page': 694, 'Genre': 'Фэнтези', 'price': 505},
   ]
   
   return render_template('example.html', name=name, numberlab=numberlab, group=group, 
   course=course, fruits=fruits, books=books)


@lab2.route('/lab2/')
def lab():
   return render_template('lab2.html')


@lab2.route('/defence/')
def defence():
    return render_template('defence.html')


@lab2.route('/defence/for1')
def for1():
    k = 999
    n = 3
    result =  str(k) * n
    return (result)


@lab2.route('/defence/if16')
def if16():
    a = 3.3
    b = 3.7
    c = 4.4
    if (a > b) & (b > c) or (a < b) & (b < c):
        a *= 2
        b *= 2
        c *= 2
        result = str(a) + ', ' + str(b) + ', ' + str(c)
    else:
        result = str(-a) + ', ' + str(-b) + ', ' + str(-c)
    return (result)
