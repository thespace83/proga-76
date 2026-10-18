import pygame as pg
from math import sin


class Loading:
    """
    Класс элемента загрузки.

    Это работает как бесконечная анимация. Когда ты вызываешь draw, загрузка смотрит на _k и как будто
    ставит эту анимацию на _k-ой секунде. А дельта в draw нужно для того, чтобы увеличивать _k и
    двигать анимацию дальше.
    """

    def __init__(self, x: int, y: int, wight: int, height: int, speed: float, color: tuple[int, int, int]):
        """
        Конструктор объекта загрузки.

        :param x: Координата x левого верхнего угла.
        :param y: Координата y левого верхнего угла.
        :param wight: Ширина загрузки.
        :param height: Высота загрузки.
        :param speed: Скорость загрузки.
        :param color: Цвет загрузки.
        """
        self.x: int = x
        self.y: int = y
        self.wight: int = wight
        self.height: int = height
        self.speed: float = speed
        self.color: tuple[int, int, int] = color
        self._k = 0  # Количество миллисекунд с начала работы программы. Нижнее подчёркивание значит, что трогать переменную все класса нельзя.

    def draw(self, delta: float, surface: pg.Surface):
        """
        Отрисовать загрузку.

        :param delta: Дельта.
        :param surface: Поверхность, на который ты рисуешь, например window.
        :return:
        """
        self._k += delta
        pg.draw.line(surface, self.color,
                     (self.x + self.wight / 2 + sin(self._k * self.speed) * self.wight / 2,
                      self.y + self.height / 2),
                     (self.x + self.wight / 2 + sin(self._k * self.speed + 1.57) * self.wight / 2,
                      self.y + self.height / 2),
                     self.height - 1)
        pg.draw.rect(surface, (128, 128, 128), (self.x, self.y, self.wight, self.height), 3)
