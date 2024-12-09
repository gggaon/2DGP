import pygame

pygame.mixer.init()
pygame.init()

menu_music = "main.mp3"
stage1_music = "stage_1.mp3"
stage2_music = "stage_2.mp3"
stage3_music = "stage_3.mp3"
bounce_sound = pygame.mixer.Sound("bounce.mp3")
bounce_sound.set_volume(0.1)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TinoVenture")

stage1_background_image = pygame.image.load('map.png').convert()
stage1_background_image = pygame.transform.scale(stage1_background_image, (800, 600))

stage2_background_image = pygame.image.load('map2.png').convert()
stage2_background_image = pygame.transform.scale(stage2_background_image, (800, 600))

stage3_background_image = pygame.image.load('map3.png').convert()
stage3_background_image = pygame.transform.scale(stage3_background_image, (800, 600))

lobby_background_image = pygame.image.load('lobby.png').convert()
lobby_background_image = pygame.transform.scale(lobby_background_image, (800, 600))

tino_image = pygame.image.load('mario.png').convert()
tino_image.set_colorkey((0, 0, 0))
tino_image = pygame.transform.scale(tino_image, (50, 50))

stand_image = pygame.image.load('stand.png').convert()
stand_image.set_colorkey((0, 0, 0))
stand_image = pygame.transform.scale(stand_image, (50, 50))

tinoface_image = pygame.image.load('tinoface.png').convert()
tinoface_image.set_colorkey((0, 0, 0))
tinoface_image = pygame.transform.scale(tinoface_image, (30, 30))

finish_image = pygame.image.load('finish.png').convert()
finish_image.set_colorkey((0, 0, 0))
finish_image = pygame.transform.scale(finish_image, (150, 150))

stage_background_image = pygame.image.load('stage.png').convert()
stage_background_image = pygame.transform.scale(stage_background_image, (800, 600))

tino_image_flipped = pygame.transform.flip(tino_image, True, False)
stand_image_flipped = pygame.transform.flip(stand_image, True, False)

ground_image = pygame.image.load('ground.png').convert_alpha()
ground_width, ground_height = ground_image.get_size()

original_block_image = pygame.image.load('ground.png').convert_alpha()

scene_8_block1_image = original_block_image.subsurface(pygame.Rect(0, 0, 50, ground_height))
scene_8_block1_image = pygame.transform.scale(scene_8_block1_image, (50, ground_height))

monster_image = pygame.image.load('mush.png').convert()
monster_image.set_colorkey((0, 0, 0))  
monster_image = pygame.transform.scale(monster_image, (50, 50))

slider_knob_image = pygame.image.load("mario.png").convert()
slider_knob_image.set_colorkey((0, 0, 0)) 
slider_knob_image = pygame.transform.scale(slider_knob_image, (40, 40))
slider_knob_image_flipped = pygame.transform.flip(slider_knob_image, True, False)

ground_y_position = 500

scene_1_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width) if not (500 <= x < 700)
]

scene_2_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width) if not (400 <= x < 600)
]

scene_3_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width)
]

scene_4_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width)
]

scene_5_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width) if not (50 <= x < 500)
]

scene_6_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width) if not (150 <= x < 500)
]

scene_7_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width) if not (400 <= x < 500)
]

scene_8_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width) if not (50 <= x < 550)
]

scene_9_ground_blocks = [
    pygame.Rect(x, ground_y_position, ground_width, ground_height)
    for x in range(0, 800, ground_width) 
]

continue_button_rect = pygame.Rect(300, 200, 200, 50)
volume_slider_rect = pygame.Rect(300, 300, 200, 10)

scene_1_block1_rect = pygame.Rect(200, ground_y_position - ground_height - 70, ground_width, ground_height)
scene_1_block2_rect = pygame.Rect(500, ground_y_position - ground_height - 70, ground_width, ground_height)

scene_2_block1_rect = pygame.Rect(300, ground_y_position - ground_height - 70, ground_width, ground_height)
scene_2_block2_rect = pygame.Rect(600, ground_y_position - ground_height - 70, ground_width, ground_height)

scene_2_block1_falling = False
scene_2_block1_velocity_y = 0.5

transparent_block_rect = pygame.Rect(700, 350, ground_width, ground_height)
transparent_block_visible = False 

scene_3_finish_rect = finish_image.get_rect()
scene_3_finish_rect.topleft = (500, ground_y_position - 150)

scene_4_finish_rect = finish_image.get_rect()
scene_4_finish_rect.topleft = (430, ground_y_position - ground_height - 220)

scene_6_finish_rect = finish_image.get_rect()
scene_6_finish_rect.topleft = (600, ground_y_position - 150)

scene_4_block1_rect = pygame.Rect(400, ground_y_position - ground_height - 70, ground_width, ground_height)

scene_5_block1_rect = pygame.Rect(300, ground_y_position - ground_height - 70, ground_width, ground_height)

scene_8_block1_rect = pygame.Rect(100, ground_y_position - ground_height - 70, 50, ground_height)
scene_8_block2_rect = pygame.Rect(250, ground_y_position - ground_height - 70, 50, ground_height)
scene_8_block3_rect = pygame.Rect(400, ground_y_position - ground_height - 70, 50, ground_height)

stage_buttons = [
    {"label": "1", "rect": pygame.Rect(250, 200, 100, 50), "enabled": True, "clear": False},
    {"label": "2", "rect": pygame.Rect(350, 200, 100, 50), "enabled": False, "clear": False},
    {"label": "3", "rect": pygame.Rect(450, 200, 100, 50), "enabled": False, "clear": False},
]
button_font = pygame.font.SysFont("Arial", 24)
stage_message_active = False

scene = "main_menu"
running = True
tino_x, tino_y = 50, ground_y_position - 50
tino_velocity_y = 0
gravity = 0.001
jump_strength = -0.5
on_ground = True
move_speed = 0.1
facing_left = False
moving = False
message_active = False
triangle_falling = False
triangle_x = 0
triangle_y = -50
triangle_speed = 0.3
player_lives = 4
current_music = None
monster_x = 200
monster_y = ground_y_position - 50
monster_speed = 0.1
monster_direction = 1
paused = False
volume_level = 0.5
font = pygame.font.SysFont("Arial", 24) 

def play_music(file, loop=-1):
    pygame.mixer.music.stop()  
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loop)

    if file == "stage_1.mp3":
        pygame.mixer.music.set_volume(0.4)  
    elif file == "stage_2.mp3":
        pygame.mixer.music.set_volume(0.4)  
    elif file == "stage_3.mp3":
        pygame.mixer.music.set_volume(0.2) 
    elif file == "main.mp3":
        pygame.mixer.music.set_volume(1.0)

def draw_stage():
    screen.blit(stage_background_image, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    
    for button in stage_buttons:
        label = button["label"]
        rect = button["rect"]
        enabled = button["enabled"]
        
        if rect.collidepoint(mouse_pos):
            color = (0, 200, 0) if enabled else (100, 100, 100)
        else:
            color = (0, 255, 0) if enabled else (150, 150, 150)

        pygame.draw.rect(screen, color, rect, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), rect, 3, border_radius=10)

        label_text = button_font.render(label, True, (0, 0, 0))
        screen.blit(label_text, (
            rect.x + (rect.width - label_text.get_width()) // 2, 
            rect.y + (rect.height - label_text.get_height()) // 2)
        )

        if button["clear"]:
            clear_text = button_font.render("CLEAR", True, (0, 0, 0))
            screen.blit(clear_text, (rect.x + 15, rect.y + 60))

    if stage_message_active:
        draw_message_box("This stage is locked!")

def draw_settings():
    screen.fill((50, 50, 50))
    
    title_font = pygame.font.SysFont("Arial", 48)
    title_text = title_font.render("SETTING", True, (255, 255, 255))
    screen.blit(title_text, ((800 - title_text.get_width()) // 2, 100))

    pygame.draw.rect(screen, (0, 255, 0), continue_button_rect, border_radius=10)
    continue_text = button_font.render("CONTINUE", True, (0, 0, 0))
    screen.blit(continue_text, (continue_button_rect.x + 55, continue_button_rect.y + 10))

    pygame.draw.rect(screen, (200, 200, 200), volume_slider_rect)

    slider_knob_x = volume_slider_rect.x + int(volume_level * volume_slider_rect.width)
    slider_knob_y = volume_slider_rect.y - 30

    screen.blit(slider_knob_image_flipped, (slider_knob_x - 20, slider_knob_y))

    volume_label = button_font.render(f"VOLUME: {int(volume_level * 100)}%", True, (255, 255, 255))
    screen.blit(volume_label, (345, 350))

def handle_stage_click(pos):
    global scene, stage_message_active
    for button in stage_buttons:
        if button["rect"].collidepoint(pos):
            if button["enabled"]:
                if button["label"] == "1":
                    scene = "scene_1"
                    if stage_buttons[0]["clear"] == True:
                        reset_outstage1()
                    elif stage_buttons[0]["clear"] == False:
                        reset_instage1()
                elif button["label"] == "2":
                    scene = "scene_4"
                    if stage_buttons[1]["clear"] == True:
                        reset_outstage2()
                    elif stage_buttons[1]["clear"] == False:
                        reset_instage2()
                elif button["label"] == "3":
                    scene = "scene_7"
                    if stage_buttons[2]["clear"] == True:
                        reset_outstage3()
                    elif stage_buttons[2]["clear"] == False:
                        reset_instage3()
            else:
                stage_message_active = True

def reset_instage1():
    global tino_x, tino_y, tino_velocity_y, triangle_falling, triangle_x, triangle_y,scene_2_block1_falling, scene_2_block1_rect, transparent_block_visible, player_lives, on_ground, facing_left, player_lives
    tino_x, tino_y = 50, ground_y_position - 50  
    tino_velocity_y = 0
    triangle_falling = False
    triangle_x = 0
    triangle_y = -50
    scene_2_block1_falling = False
    scene_2_block1_rect = pygame.Rect(300, ground_y_position - ground_height - 70, ground_width, ground_height)
    transparent_block_visible = False
    on_ground = True  
    facing_left = False
    player_lives -= 1
    scene = "scene_1"

def reset_outstage1():
    global tino_x, tino_y, tino_velocity_y, triangle_falling, triangle_x, triangle_y,scene_2_block1_falling, scene_2_block1_rect, transparent_block_visible, player_lives, on_ground, facing_left, player_lives
    tino_x, tino_y = 50, ground_y_position - 50  
    tino_velocity_y = 0
    triangle_falling = False
    triangle_x = 0
    triangle_y = -50
    scene_2_block1_falling = False
    scene_2_block1_rect = pygame.Rect(300, ground_y_position - ground_height - 70, ground_width, ground_height)
    transparent_block_visible = False
    on_ground = True  
    facing_left = False
    player_lives = 3
    scene = "scene_1"

def reset_instage2():
    global tino_x, tino_y, tino_velocity_y, player_lives, on_ground, facing_left, player_lives
    tino_x, tino_y = 50, ground_y_position - 50  
    tino_velocity_y = 0
    on_ground = True  
    facing_left = False
    player_lives -= 1
    scene = "scene_4"

def reset_outstage2():
    global tino_x, tino_y, tino_velocity_y, player_lives, on_ground, facing_left, player_lives
    tino_x, tino_y = 50, ground_y_position - 50  
    tino_velocity_y = 0
    on_ground = True  
    facing_left = False
    player_lives = 3
    scene = "scene_4"

def reset_instage3():
    global tino_x, tino_y, tino_velocity_y, player_lives, on_ground, facing_left, player_lives
    tino_x, tino_y = 50, ground_y_position - 50  
    tino_velocity_y = 0
    on_ground = True  
    facing_left = False
    player_lives -= 1
    scene = "scene_7"

def reset_outstage3():
    global tino_x, tino_y, tino_velocity_y, player_lives, on_ground, facing_left, player_lives
    tino_x, tino_y = 50, ground_y_position - 50  
    tino_velocity_y = 0
    on_ground = True  
    facing_left = False
    player_lives = 3
    scene = "scene_7"

def check_falling_into_hole():
    global player_lives, scene
    tino_rect = pygame.Rect(tino_x, tino_y, 50, 50)
    is_in_hole = True

    if scene == "scene_1":
        for block in scene_1_ground_blocks:
            if tino_rect.colliderect(block):
                is_in_hole = False
                break
        if tino_rect.colliderect(scene_1_block1_rect) or tino_rect.colliderect(scene_1_block2_rect):
            is_in_hole = False
    elif scene == "scene_2":
        for block in scene_2_ground_blocks:
            if tino_rect.colliderect(block):
                is_in_hole = False
                break
        if tino_rect.colliderect(scene_2_block1_rect) or tino_rect.colliderect(scene_2_block2_rect):
            is_in_hole = False
    elif scene == "scene_3":
        for block in scene_3_ground_blocks:
            if tino_rect.colliderect(block):
                is_in_hole = False
                break
    elif scene == "scene_5":
        for block in scene_5_ground_blocks:
            if tino_rect.colliderect(block):
                is_in_hole = False
                break
        if tino_rect.colliderect(scene_5_block1_rect):
            is_in_hole = False
    elif scene == "scene_7":
        for block in scene_7_ground_blocks:
            if tino_rect.colliderect(block):
                is_in_hole = False
                break
    elif scene == "scene_8":
        for block in scene_8_ground_blocks:
            if tino_rect.colliderect(block):
                is_in_hole = False
                break
        if tino_rect.colliderect(scene_8_block1_rect) or tino_rect.colliderect(scene_8_block2_rect) or tino_rect.colliderect(scene_8_block3_rect):
            is_in_hole = False

    if is_in_hole and tino_y > ground_y_position:
        if scene in ["scene_1", "scene_2", "scene_3"]:
            scene = "scene_1"
            reset_instage1()
        if scene in ["scene_4", "scene_5"]:
            scene = "scene_4"
            reset_instage2()
        if scene in ["scene_7", "scene_8"]:
            scene = "scene_7"
            reset_instage3()

def draw_lobby():
    screen.blit(lobby_background_image, (0, 0))

    large_font = pygame.font.SysFont("Comic Sans MS", 48)
    if pygame.time.get_ticks() % 1000 < 500:  
        press_enter_text = large_font.render("Press Enter", True, (255, 255, 255))
        screen.blit(press_enter_text, ((800 - press_enter_text.get_width()) // 2, 500))

def draw_message_box(message):
    box_width, box_height = 500, 250
    box_x = (800 - box_width) // 2
    box_y = (600 - box_height) // 2

    pygame.draw.rect(screen, (0, 0, 0), (box_x, box_y, box_width, box_height))
    pygame.draw.rect(screen, (255, 255, 255), (box_x+5, box_y+5, box_width-10, box_height-10), 5)

    message_lines = message.split('\n')
    message_font = pygame.font.SysFont("Arial", 28, bold=True)
    for i, line in enumerate(message_lines):
        text_surface = message_font.render(line, True, (255, 255, 255))
        text_x = box_x + (box_width - text_surface.get_width()) // 2
        text_y = box_y + 60 + i * 40
        screen.blit(text_surface, (text_x, text_y))

    continue_text = message_font.render("Press Enter to continue", True, (200, 200, 200))
    continue_x = box_x + (box_width - continue_text.get_width()) // 2
    continue_y = box_y + box_height - 60
    screen.blit(continue_text, (continue_x, continue_y))

def draw_tino_position():
    position_text = font.render(f"X: {int(tino_x)}, Y: {int(tino_y)}", True, (0, 0, 0))  
    screen.blit(position_text, (600, 10)) 

def draw_game_scene():
    if scene in ["scene_1", "scene_2", "scene_3"]:
        screen.blit(stage1_background_image, (0, 0))
    elif scene in ["scene_4", "scene_5", "scene_6"]:
        screen.blit(stage2_background_image, (0, 0))
    elif scene in ["scene_7", "scene_8", "scene_9"]:
        screen.blit(stage3_background_image, (0, 0))

    if moving:
        current_tino_image = tino_image if facing_left else tino_image_flipped
    else:
        current_tino_image = stand_image if facing_left else stand_image_flipped
    screen.blit(current_tino_image, (tino_x, tino_y))

    if scene == "scene_1":
        for block in scene_1_ground_blocks:
            screen.blit(ground_image, block.topleft)
        screen.blit(ground_image, scene_1_block1_rect.topleft)
        screen.blit(ground_image, scene_1_block2_rect.topleft)
    elif scene == "scene_2":
        for block in scene_2_ground_blocks:
            screen.blit(ground_image, block.topleft)
        screen.blit(ground_image, scene_2_block1_rect.topleft)
        screen.blit(ground_image, scene_2_block2_rect.topleft)
        draw_monster()
    elif scene == "scene_3":
        for block in scene_3_ground_blocks:
            screen.blit(ground_image, block.topleft)
        if transparent_block_visible:
            screen.blit(ground_image, transparent_block_rect.topleft)
        scene_3_finish_rect.y = max(100, min(ground_y_position - 150, ground_y_position - 150 - tino_x // 2))
        screen.blit(finish_image, scene_3_finish_rect.topleft)
    elif scene == "scene_4":
        for block in scene_4_ground_blocks:
            screen.blit(ground_image, block.topleft)
        screen.blit(ground_image, scene_4_block1_rect.topleft)

        scene_4_finish_rect.x = 330 + tino_x
        if scene_4_finish_rect.x >= 560 :
            scene_4_finish_rect.y = ground_y_position - 150
        screen.blit(finish_image, scene_4_finish_rect.topleft)
    elif scene == "scene_5":
        for block in scene_5_ground_blocks:
            screen.blit(ground_image, block.topleft)
        screen.blit(ground_image, scene_5_block1_rect.topleft)
    elif scene == "scene_6":
        for block in scene_6_ground_blocks:
            screen.blit(ground_image, block.topleft)
            screen.blit(finish_image, scene_6_finish_rect.topleft)
    elif scene == "scene_7":
        for block in scene_7_ground_blocks:
            screen.blit(ground_image, block.topleft)
    elif scene == "scene_8":
        for block in scene_8_ground_blocks:
            screen.blit(ground_image, block.topleft)

        screen.blit(scene_8_block1_image, scene_8_block1_rect.topleft)
        screen.blit(scene_8_block1_image, scene_8_block2_rect.topleft)
        screen.blit(scene_8_block1_image, scene_8_block3_rect.topleft)
    elif scene == "scene_9":
        for block in scene_9_ground_blocks:
            screen.blit(ground_image, block.topleft)

    if triangle_falling:
        triangle_points = [
            (triangle_x, triangle_y + 50),
            (triangle_x - 20, triangle_y),
            (triangle_x + 20, triangle_y)
        ]
        pygame.draw.polygon(screen, (255, 0, 0), triangle_points)

    screen.blit(tinoface_image, (10, 10))
    lives_text = font.render(f"x {player_lives}", True, (0, 0, 0))
    screen.blit(lives_text, (50, 10))

    if message_active:
        draw_message_box(f"Wow, I arrived safely!\nBut is this the only life I have left?\n{player_lives}?!")

    draw_tino_position()

def draw_monster():
    screen.blit(monster_image, (monster_x, monster_y))

def update_monster():
    global monster_x, monster_direction, tino_x, tino_y, scene

    monster_x += monster_speed * monster_direction
    if monster_x <= 150 or monster_x >= 500:  
        monster_direction *= -1

    tino_rect = pygame.Rect(tino_x, tino_y, 50, 50)
    monster_rect = pygame.Rect(monster_x, monster_y, 50, 50)
    if tino_rect.colliderect(monster_rect):
        scene = "scene_1"
        reset_instage1()

def check_finish():
    global scene, message_active, stage_buttons, player_lives
    tino_rect = pygame.Rect(tino_x, tino_y, 50, 50)

    if scene == "scene_3" and tino_rect.colliderect(scene_3_finish_rect):
        message_active = True

    if scene == "scene_6" and tino_rect.colliderect(scene_6_finish_rect):
        message_active = True

    #if scene == "scene_9" and tino_rect.colliderect(scene_9_finish_rect):
    #    message_active = True

    keys = pygame.key.get_pressed()
    if message_active and keys[pygame.K_RETURN]:
        if scene == "scene_3":
            stage_buttons[0]["clear"] = True  
            stage_buttons[1]["enabled"] = True 

        if scene == "scene_6":
            stage_buttons[1]["clear"] = True  
            stage_buttons[2]["enabled"] = True  

        if scene == "scene_9":
            stage_buttons[2]["clear"] = True  

        scene = "stage"  
        message_active = False
        player_lives = 4

def handle_keys():
    global tino_x, tino_y, tino_velocity_y, on_ground, facing_left, moving
    if message_active:  
        return

    keys = pygame.key.get_pressed()
    moving = False
    if keys[pygame.K_a]:
        tino_x -= move_speed
        tino_x = max(tino_x, 0)  
        facing_left = True
        moving = True
    if keys[pygame.K_d]:
        tino_x += move_speed
        facing_left = False
        moving = True
    if keys[pygame.K_w] and on_ground:
        tino_velocity_y = jump_strength
        on_ground = False
        moving = True
        
        bounce_sound.play()

def handle_collisions():
    global tino_y, tino_velocity_y, on_ground, scene, tino_x, transparent_block_visible
    tino_rect = pygame.Rect(tino_x, tino_y, 50, 50)

    if scene == "scene_1":
        blocks = scene_1_ground_blocks + [scene_1_block1_rect, scene_1_block2_rect]
    elif scene == "scene_2":
        blocks = scene_2_ground_blocks + [scene_2_block2_rect]
        if not scene_2_block1_falling:
         blocks.append(scene_2_block1_rect)

    elif scene == "scene_3":
        blocks = scene_3_ground_blocks
        if tino_rect.colliderect(transparent_block_rect):
            if tino_velocity_y > 0:  
                tino_y = transparent_block_rect.top - 50
                tino_velocity_y = 0
                on_ground = True
                transparent_block_visible = True  
                return
    elif scene == "scene_4":
        blocks = scene_4_ground_blocks + [scene_4_block1_rect]
    elif scene == "scene_5":
        blocks = scene_5_ground_blocks + [scene_5_block1_rect]
    elif scene == "scene_6":
        blocks = scene_6_ground_blocks
    elif scene == "scene_7":
        blocks = scene_7_ground_blocks
    elif scene == "scene_8":
        blocks = scene_8_ground_blocks + [scene_8_block1_rect] + [scene_8_block2_rect] + [scene_8_block3_rect]
    elif scene == "scene_9":
        blocks = scene_9_ground_blocks

    for block in blocks:
        if tino_rect.colliderect(block) and tino_velocity_y > 0:
            tino_y = block.top - 50
            tino_velocity_y = 0
            on_ground = True
            return

    if scene in ["scene_3", "scene_6", "scene_9"]:
        tino_x = min(tino_x, 800 - 50)
    if tino_x > 800:
        if scene == "scene_1":
            scene = "scene_2"
        elif scene == "scene_2":
            scene = "scene_3"
        elif scene == "scene_4":
            scene = "scene_5"
        elif scene == "scene_5":
            scene = "scene_6"
        elif scene == "scene_7":
            scene = "scene_8"
        elif scene == "scene_8":
            scene = "scene_9"
        tino_x = 0

def handle_triangle():
    global triangle_falling, triangle_y, triangle_x
    if scene != "scene_1":
        return
    tino_rect = pygame.Rect(tino_x, tino_y, 50, 50)
    if triangle_falling:
        triangle_y += triangle_speed
        triangle_rect = pygame.Rect(triangle_x - 20, triangle_y, 40, 50)
        if triangle_rect.colliderect(tino_rect):
            reset_instage1()
    elif tino_x >= 300 and not triangle_falling:
        triangle_falling = True
        triangle_x = tino_x + 140

def update_scene_2_block1():
    global scene_2_block1_rect, scene_2_block1_falling, tino_y, tino_velocity_y, on_ground

    tino_rect = pygame.Rect(tino_x, tino_y, 50, 50)

    if tino_rect.bottom == scene_2_block1_rect.top and not scene_2_block1_falling:
        scene_2_block1_falling = True 

    if scene_2_block1_falling:
        scene_2_block1_rect.y += scene_2_block1_velocity_y

        if tino_rect.colliderect(scene_2_block1_rect):
            tino_y += scene_2_block1_velocity_y
            on_ground = False

        if scene_2_block1_rect.top > 600:
            scene_2_block1_falling = False  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        
        if paused:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if continue_button_rect.collidepoint(mouse_pos):
                    paused = False

            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  
                    if volume_slider_rect.collidepoint(event.pos):
                        volume_level = (event.pos[0] - volume_slider_rect.x) / volume_slider_rect.width
                        volume_level = max(0, min(1, volume_level))
                        pygame.mixer.music.set_volume(volume_level)
                        bounce_sound.set_volume(volume_level)

        if not paused:
            if scene == "main_menu" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                scene = "stage"
            elif scene == "stage" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_stage_click(event.pos)
            elif scene == "stage" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                handle_stage_click(event.pos)
            elif stage_message_active and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                stage_message_active = False

    if not paused:
        if scene in ["main_menu", "stage"]:
            if current_music != menu_music:
                play_music(menu_music)
                current_music = menu_music
        elif scene in ["scene_1", "scene_2", "scene_3"]:
            if current_music != stage1_music:
                play_music(stage1_music)
                current_music = stage1_music
        elif scene in ["scene_4", "scene_5", "scene_6"]:
            if current_music != stage2_music:
                play_music(stage2_music)
                current_music = stage2_music
        elif scene in ["scene_7", "scene_8", "scene_9"]:
            if current_music != stage3_music:
                play_music(stage3_music)
                current_music = stage3_music

    if paused:
        draw_settings()
    else:
        if scene == "main_menu":
            draw_lobby()
        elif scene == "stage":
            draw_stage()
        elif scene in ["scene_1", "scene_2", "scene_3"]:
            if not message_active:  
                handle_keys()
                tino_velocity_y += gravity
                tino_y += tino_velocity_y
                handle_collisions()
                check_falling_into_hole()
                handle_triangle()

                if scene == "scene_2":  
                    update_scene_2_block1()
                    update_monster()
            check_finish()  
            draw_game_scene()
        elif scene in ["scene_4", "scene_5"]:
            handle_keys()
            tino_velocity_y += gravity
            tino_y += tino_velocity_y
            handle_collisions()
            check_falling_into_hole()
            draw_game_scene()
        elif scene == "scene_6":
            handle_keys()
            tino_velocity_y += gravity
            tino_y += tino_velocity_y
            handle_collisions()
            if tino_y > 1000:  
                tino_y = -100 
                tino_velocity_y = 0
            draw_game_scene()
            check_finish()
        elif scene in ["scene_7", "scene_8", "scene_9"]:
            if not message_active:  
                handle_keys()
                tino_velocity_y += gravity
                tino_y += tino_velocity_y
                handle_collisions()
                check_falling_into_hole()
                check_finish()  
                draw_game_scene()

    pygame.display.flip()

pygame.quit()
