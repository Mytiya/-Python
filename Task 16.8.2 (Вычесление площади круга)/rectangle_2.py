from rectangle import Rectangle, Square, Circle
# Создаем два прямоугольника
rec_1 = Rectangle(3, 4)
rec_2 = Rectangle(12, 5)
# Вывод площади двух прямоугольников
print(rec_1.get_area())
print(rec_2.get_area())
# Создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)
# Вывод площади квадратов
print(square_1.get_area_square(),
      square_2.get_area_square())
# Создаем два круга
circle_1 = Circle(10)
circle_2 = Circle(60)
# Выводим площадь кругов
print(circle_1.get_area_circle(),
      circle_2.get_area_circle())

figures = [rec_1, rec_2, square_1,
           square_2, circle_1, circle_2]
# функция isinstance, проверяет, является ли аргумент объекта экземпляром класса или экземпляром класса из кортежа
for figure in figures:
      if isinstance(figure, Square):
            print(figure.get_area_square())
      elif isinstance(figure, Circle):
            print(figure.get_area_circle())
      else:
            print(figure.get_area())
