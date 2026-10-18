import pygame as pg
from loading import Loading

pg.init()

window = pg.display.set_mode((800, 800))

clock = pg.time.Clock()

loading1 = Loading(100, 100, 400, 50, 3, (255, 0, 0))
loading2 = Loading(200, 300, 500, 25, 5, (255, 255, 0))
loading3 = Loading(500, 400, 250, 30, 2, (0, 255, 0))
loading4 = Loading(50, 600, 200, 90, 1.5, (255, 0, 255))

running = True
while running:
    dt = clock.tick() / 1000
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    window.fill((32, 32, 32))

    loading1.draw(dt, window)
    loading2.draw(dt, window)
    loading3.draw(dt, window)
    loading4.draw(dt, window)

    pg.display.flip()
