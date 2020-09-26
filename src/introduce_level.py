import pygame
from levels import mine
from levels import maze
from levels import quiz
import constants as consts
from utils import widgets, colors


def introduce(level):
    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])

    text = ""
    controls = ""
    if level == 1:
        text = "Solve the maze to get the crystal!"
        controls = "WASD to move through the maze"
    if level == 2:
        text = "Solve the alien's riddles to get the crystal!"
        controls = "Hover over the white bar and type the answer!"
    if level == 3:
        text = "The last crystal has buried itself! Dig for it!"
        controls = "Use A or Left Arrow Key to move Left and D or Right Arrow Key to move right"

    rendered_text = consts.TITLE_FONT.render(text, True, colors.WHITE_COLOR)
    rendered_controls = consts.BUTTON_FONT.render(controls, True, colors.WHITE_COLOR)

    consts.MAIN_DISPLAY.blit(rendered_text, (consts.SCREEN_WIDTH/2 - rendered_text.get_width()/2, 150))

    consts.MAIN_DISPLAY.blit(rendered_controls, (consts.SCREEN_WIDTH/2 - rendered_controls.get_width()/2, 200))

    play_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                       consts.SCREEN_HEIGHT / 2 + 20),
                                     width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='Start Level')

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:
        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        # button interaction
        if play_button.hovered:
            play_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                play_button.toggle_bg(colors.THEME_ALT)
                if level == 1:
                    return maze.maze_level()
                elif level == 2:
                    return quiz.Main()
                elif level == 3:
                    return mine.mine_level()
        else:
            play_button.toggle_bg(colors.THEME_ALT)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
