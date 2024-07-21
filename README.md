# Geometry Library

## Описание

Эта библиотека позволяет вычислять площадь различных геометрических фигур, таких как круги и треугольники. Также она может проверять, является ли треугольник прямоугольным.

## Добавление фигур

Чтобы добавить новую фигуру, например, прямоугольник, нужно создать новый класс, наследующийся от Shape, и реализовать метод area:

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
