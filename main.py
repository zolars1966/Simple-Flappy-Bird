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
    title = "$~ FlappyBird"

    env = Environment()
  
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
                    	elif env.Bird.alive: env.Bird.vel = -HEIGHT

            vert_ticks = pg.time.get_ticks()

            # drawing graphics

            screen.fill((135, 206, 235))

            # Pipe 1
            pg.draw.rect(screen, env.Pipe1.color, (env.Pipe1.x, env.Pipe1.height, env.Pipe1.width, HEIGHT - env.Pipe1.height))
            pg.draw.rect(screen, env.Pipe1.color, (env.Pipe1.x, 0, env.Pipe1.width, env.Pipe1.height - env.Pipe1.gap))

            # Pipe 2
            pg.draw.rect(screen, env.Pipe2.color, (env.Pipe2.x, env.Pipe2.height, env.Pipe2.width, HEIGHT - env.Pipe2.height))
            pg.draw.rect(screen, env.Pipe2.color, (env.Pipe2.x, 0, env.Pipe2.width, env.Pipe2.height - env.Pipe2.gap))

            # Ground
            pg.draw.rect(screen, env.ground_color, (0, env.ground_height, WIDTH, HEIGHT - env.ground_height))

            # Bird (Player)
            pg.draw.circle(screen, env.Bird.color, (env.Bird.x, env.Bird.height), env.Bird.radius)

            # cheking keys
            check_pressed()

            pg.display.set_caption(title + " Points: " + str(env.points) + " ~fps: " + str(round(clock.get_fps(), 2)))

            pg.display.flip()
            clock.tick()