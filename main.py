import pygame as pg
import sys
import time
from globals import *
from game import *


# Keyboard keys checking
def check_pressed():
    keys = pg.key.get_pressed()

    if True in keys:
        pass


if __name__ == "__main__":
    # creating a pygame window
    screen = pg.display.set_mode(SIZE)
    clock = pg.time.Clock()
    title = "$~ FlappyBird Points: "

    env = Environment()

    Background = pg.transform.scale(pg.image.load("sprites/background-day.png").convert(), (WIDTH, HEIGHT))
    Ground = pg.transform.scale_by(pg.image.load("sprites/base.png").convert(), WIDTH / 336)
    Bird = [
        pg.transform.scale_by(pg.image.load("sprites/yellowbird-upflap.png").convert_alpha(), WIDTH // 15 / 17),
        pg.transform.scale_by(pg.image.load("sprites/yellowbird-midflap.png").convert_alpha(), WIDTH // 15 / 17),
        pg.transform.scale_by(pg.image.load("sprites/yellowbird-downflap.png").convert_alpha(), WIDTH // 15 / 17)
    ]
    Pipe = pg.transform.scale_by(pg.image.load("sprites/pipe-green.png").convert_alpha(), WIDTH // 4 / 52)
  
    vert_ticks, upd_time = pg.time.get_ticks(), time.perf_counter_ns()
    pause = True

    pg.display.set_icon(pg.image.load("icon.png"))

    for _ in range(2):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        pg.display.flip()

    # main cycle
    while True:
        # game environment updating (with vertical synchronization)
        if (N_DELTA_TIME <= time.perf_counter_ns() - upd_time) and not pause:
            upd_time = time.perf_counter_ns()

            # calling for game environment to update
            env.update(float(dt))

        # game Assets/UI/elements drawing
        if FPS_DT <= pg.time.get_ticks() - vert_ticks:
            # checking for keyboard, window, mouse inputs or events
            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    exit()

                if event.type == pg.KEYDOWN:
                    if event.key in (pg.K_SPACE, pg.K_UP):
                        pause = False
                        
                        if env.ground:
                            env = Environment()
                            pause = True
                        elif env.Bird.alive:
                            env.Bird.vel = -HEIGHT

            vert_ticks = pg.time.get_ticks()

            # drawing graphics

            screen.blit(Background, (0, 0))
            # Pipe 1
            screen.blit(Pipe, (env.Pipe1.x, env.Pipe1.height))
            screen.blit(pg.transform.rotate(Pipe, 180), (env.Pipe1.x, env.Pipe1.height - env.Pipe1.gap - HEIGHT // 140 * 124))
            # Pipe 2
            screen.blit(Pipe, (env.Pipe2.x, env.Pipe2.height))
            screen.blit(pg.transform.rotate(Pipe, 180), (env.Pipe2.x, env.Pipe2.height - env.Pipe2.gap - HEIGHT // 140 * 124))
            # Ground
            screen.blit(Ground, (0, HEIGHT - Ground.get_size()[1]))
            # Bird (Player)
            screen.blit(pg.transform.rotate(Bird[env.Bird.state], max(-env.Bird.vel / 25, -90)), (env.Bird.x - env.Bird.radius, env.Bird.height - env.Bird.radius))

            # cheking keys
            check_pressed()

            pg.display.set_caption(title + str(env.points) + " ~fps: " + str(round(clock.get_fps(), 2)))

            pg.display.flip()
            clock.tick()