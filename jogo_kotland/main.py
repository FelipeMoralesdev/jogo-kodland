import random
TITLE = "Yng - De volta para casa"

WIDTH = 800
HEIGHT = 600

game_state = "menu"  

music_on = True
sounds_on = True
music.play('music')


menu_options = ["Come\u00E7ar o jogo", "M\u00FAsica: Ligada",  "Sons: Ligados", "Sair"]
mouse_pos = (0, 0)
ufo = Actor('playership3_blue')

class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 1
        self.flip_x = False

        self.frames_walk = ['p3_walk01','p3_walk02','p3_walk03','p3_walk04','p3_walk05','p3_walk06','p3_walk07','p3_walk08','p3_walk09','p3_walk10','p3_walk11']
        self.frames_idle = ['p3_front', 'p3_stand','p3_front','p3_stand_02']

        self.actor = Actor('p3_front')
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 0.1

    def on_ground(self, platforms):
        for p in platforms:
            if (self.x + self.actor.width/2 > p.left and
                self.x - self.actor.width/2 < p.right and
                abs((self.y + self.actor.height/2) - p.top) <= 1):
                return True
        return False

    def update(self, keyboard, platforms, game_state):
        prev_y = self.y
        moving = False

        # Movimento horizontal
        if game_state == "jogo":
            if keyboard.right:
                self.x += 4
                moving = True
                self.flip_x = False
            elif keyboard.left:
                self.x -= 4
                moving = True
                self.flip_x = True

        # Pulo
        if game_state == "jogo" and keyboard.up and self.on_ground(platforms):
            self.velocity = -13

        # Gravidade
        self.y += self.velocity
        self.velocity += self.gravity

        # Colisão
        actor_rect = Rect((self.x - self.actor.width/2 + 20, self.y - self.actor.height/2),
                          (self.actor.width - 40, self.actor.height))
        for p in platforms:
            if actor_rect.colliderect(p):
                if prev_y + self.actor.height/2 <= p.top:
                    self.y = p.top - self.actor.height/2
                    self.velocity = 0
                elif prev_y - self.actor.height/2 >= p.bottom:
                    self.y = p.bottom + self.actor.height/2
                    self.velocity = 1
                else:
                    self.y = p.top - self.actor.height/2
                    self.velocity = 0
                actor_rect = Rect((self.x - self.actor.width/2, self.y - self.actor.height/2),
                                  (self.actor.width, self.actor.height))

        # Animação
        self.frame_timer += 1/60
        if moving:
            if self.frame_timer >= self.frame_delay:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames_walk)
                self.actor.image = self.frames_walk[self.frame_index]
        else:
            if self.frame_timer >= self.frame_delay * 4:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames_idle)
                self.actor.image = self.frames_idle[self.frame_index]

    def draw(self, camera_x):
        self.actor.pos = (self.x - camera_x, self.y)
        self.actor.flip_x = self.flip_x
        self.actor.draw()

class Bee:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frames = ['bee_fly', 'bee']
        self.actor = Actor(self.frames[0])
        self.frame_index = 0
        self.frame_counter = 0

    def update(self):
        # Animação
        self.frame_counter += 1
        if self.frame_counter >= 10:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.actor.image = self.frames[self.frame_index]

        # Movimento
        self.x -= 5
        if self.x < -50:
            self.x = random.randint(900, 2000)
            self.y = random.randint(250, 350)

    def draw(self):
        self.actor.pos = (self.x, self.y)
        self.actor.draw()

class Spikes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.actor = Actor('spikes') 

    def draw(self, camera_x):
        self.actor.pos = (self.x - camera_x, self.y)
        self.actor.draw()

alien = Alien(100, 454)
bee = Bee(600, 350)
camera_x = 0

platforms = [Rect((0, 500), (500, 100)), Rect((630, 450), (110, 16)), Rect((860, 400), (150, 16)), Rect((600, 250), (200, 16)), Rect((900, 150), (250, 16)), Rect((1100, 500), (150, 16)), Rect((1300, 300), (150, 16)), Rect((1500, 500), (1500, 100))]
spikes = [Spikes(1700, 500), Spikes(1900, 500),Spikes(2100, 500)]
spike_areas = [(1660, 1740, 430, 454), (1860, 1940, 430, 454), (2060, 2140, 430, 454)]

def draw():
    if game_state == "menu":
        draw_menu()
    elif game_state == "jogo":
        draw_game()
    elif game_state == "perdeu":
        draw_game()
        screen.draw.text("Voc\u00ea perdeu!", center=(WIDTH//2, HEIGHT//2),
                         fontsize=80, color="red")
        screen.draw.text("Clique para voltar ao menu",
                         center=(WIDTH//2, HEIGHT//2 + 80),
                         fontsize=40, color="white")
    elif game_state == "venceu":
        draw_game()
        screen.draw.text("Voc\u00ea venceu!", center=(WIDTH//2, HEIGHT//2),
                        fontsize=80, color="green")
        screen.draw.text("Clique para voltar ao menu",
                        center=(WIDTH//2, HEIGHT//2 + 80),
                        fontsize=40, color="white")

def draw_menu():
    draw_game()
    screen.draw.text("MENU PRINCIPAL", center=(WIDTH//2, 100), fontsize=60, color="white")
    for i, option in enumerate(menu_options):
        option_x = WIDTH // 2
        option_y = 200 + i*60
        option_width = 400
        option_height = 50
        rect = Rect((option_x - option_width//2, option_y - option_height//2),
                    (option_width, option_height))
        if rect.collidepoint(mouse_pos):
            fontsize = 50
            color = "yellow"
        else:
            fontsize = 40
            color = "white"
        screen.draw.text(option, center=(option_x, option_y), fontsize=fontsize, color=color)

def draw_game():
    screen.draw.filled_rect(Rect((0, 0), (800, 600)), (0, 191, 255))  # céu
    for p in platforms:
        p_com_camera = Rect((p.x - camera_x, p.y), (p.width, p.height))
        screen.draw.filled_rect(p_com_camera, (173, 255, 47))
    screen.draw.filled_circle((700, 80), 36, (255, 230, 80))  # sol
    alien.draw(camera_x)
    bee.draw()
    ufo.pos = (2500 - camera_x, 480)
    ufo.draw()
    for s in spikes:
        s.draw(camera_x)
    #screen.draw.text("x="+str(alien.x)+"y="+str(alien.y), (20,20), color=(0,0,0), fontsize=20)

def update():
    if game_state in ("menu", "jogo", "perdeu"):
        update_game()

def update_game():
    global camera_x, game_state

    if game_state == "jogo":
        alien.update(keyboard, platforms, game_state)
        bee.update()

        if alien.actor.colliderect(bee.actor):
            game_state = "perdeu"
            if sounds_on:
                sounds.gameover.play()

        if alien.y >700:
            game_state = "perdeu"
            if sounds_on:
                sounds.gameover.play()
        
        for x_min, x_max, y_min, y_max in spike_areas:
            if x_min <= alien.x <= x_max and y_min <= alien.y <= y_max:
                game_state = "perdeu"
                if sounds_on:
                    sounds.gameover.play()

        if alien.x >= 2450:
            game_state = "venceu"
            if sounds_on:
                sounds.victory.play()

        if alien.x > WIDTH // 2:
            camera_x = alien.x - WIDTH // 2
        else:
            camera_x = 0

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def on_mouse_down(pos):
    global game_state, music_on, sounds_on, menu_options
    if game_state == "perdeu":
        reset_game()
        game_state = "menu"
        return
    if game_state in ("perdeu", "venceu"):
        reset_game()
        game_state = "menu"
        return

    for i, option in enumerate(menu_options):
        option_x = WIDTH // 2
        option_y = 200 + i*60
        option_width = 400
        option_height = 50
        rect = Rect((option_x - option_width//2, option_y - option_height//2),
                    (option_width, option_height))
        if rect.collidepoint(pos):
            if option.startswith("Come\u00E7ar"):
                game_state = "jogo"
            elif option.startswith("M\u00FAsica"):
                music_on = not music_on
                menu_options[1] = f"M\u00FAsica: {'Ligada' if music_on else 'Desligada'}"
                if music_on:
                    music.play('music')
                else:
                    music.stop()  
            elif option.startswith("Sons"):
                sounds_on = not sounds_on
                menu_options[2] = f"Sons: {'Ligados' if sounds_on else 'Desligados'}"
            elif option.startswith("Sair"):
                exit()

def reset_game():
    global alien, bee, camera_x
    alien.x = 100
    alien.y = 454
    alien.velocity = 0
    alien.frame_index = 0
    alien.frame_timer = 0
    alien.actor.image = 'p3_front'
    alien.flip_x = False
    bee.x = 600
    bee.y = 350
    bee.frame_index = 0
    bee.frame_counter = 0
    bee.actor.image = bee.frames[0]
    camera_x = 0
