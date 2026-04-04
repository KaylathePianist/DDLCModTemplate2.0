image menu_logo:
    "mod_assets/DDLCModTemplateLogo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

init python:
    
    ## ParticleBurst
    # This class declares the code used for the ParticleBurst effect.
    class ParticleBurst(object):
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 5):
            self.sm = SpriteManager(update=self.update)

            self.stars = [ ]
            self.displayable = theDisplayable
            self.explodeTime = explodeTime
            self.numParticles = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.gravity = 240
            self.timePassed = 0
            
            for i in range(self.numParticles):
                self.add(self.displayable, 1)
        
        def add(self, d, speed):
            s = self.sm.create(d)
            speed = random.random()
            angle = random.random() * 3.14159 * 2
            xSpeed = speed * math.cos(angle) * self.particleXSpeed
            ySpeed = speed * math.sin(angle) * self.particleYSpeed - 1
            s.x = xSpeed * 24
            s.y = ySpeed * 24
            pTime = self.particleTime
            self.stars.append((s, ySpeed, xSpeed, pTime))
        
        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x = xSpeed * 120 * (st + .20)
                    s.y = (ySpeed * 120 * (st + .20) + (self.gravity * st * st))
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            return 0