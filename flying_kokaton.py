import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img=pg.image.load("fig/3.png")
    kk_img=pg.transform.flip(kk_img, True,False)
    kk_rct=kk_img.get_rect()
    kk_rct.center=300,200
    tmr = 0
    tobu=0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst=pg.key.get_pressed()
        dx=-1
        dy=0

        if key_lst[pg.K_UP]:
            dx=-1
            dy=-1

        if key_lst[pg.K_DOWN]:
            dx=-1
            dy=1

        if key_lst[pg.K_RIGHT]:
            dx=1
            dy=0

        if key_lst[pg.K_LEFT]:
            dx=-1
            dy=0
        
        kk_rct.move_ip(dx,dy)

        screen.blit(bg_img, [tobu, 0])
        screen.blit(bg_img2, [tobu+1600, 0])
        screen.blit(bg_img, [tobu+3200, 0])
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        print(tobu)
        if tobu<=-3199:
            tobu=0
        tmr += 1  
        tobu -=5   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()