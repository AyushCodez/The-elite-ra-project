import pygame
import constants as consts
from utils import colors
from utils import widgets
from levels import mine


def level_chooser_screen():

    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    # Render font
    levels_title = consts.TITLE_FONT.render("LEVELS", True, colors.WHITE_COLOR)
    consts.MAIN_DISPLAY.blit(levels_title, (40, 10))

    pygame.draw.line(consts.MAIN_DISPLAY, colors.WHITE_COLOR, (5, 10 + levels_title.get_height()),
                     (consts.SCREEN_WIDTH-10, 10 + levels_title.get_height()), 3)

    # TODO: blit buttons for levels 1 thru 6
    lvl1_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(10, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='1')
    lvl2_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(70, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='2')
    lvl3_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(130, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='3')
    lvl4_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(190, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='4')
    lvl5_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(250, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='5')
    lvl6_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(310, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='6')

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

        # TODO: add button handlers
        if lvl1_button.hovered:
            lvl1_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                lvl1_button.toggle_bg(colors.THEME_ALT)
                print("NO")
        else:
            lvl1_button.toggle_bg(colors.THEME_ALT)

        if lvl2_button.hovered:
            lvl2_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                lvl2_button.toggle_bg(colors.THEME_ALT)
                print("NO")
        else:
            lvl2_button.toggle_bg(colors.THEME_ALT)

        if lvl3_button.hovered:
            lvl3_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                lvl3_button.toggle_bg(colors.THEME_ALT)
                return mine.mine_level()
        else:
            lvl3_button.toggle_bg(colors.THEME_ALT)

        if lvl4_button.hovered:
            lvl4_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                lvl4_button.toggle_bg(colors.THEME_ALT)
                print("NO")
        else:
            lvl4_button.toggle_bg(colors.THEME_ALT)

        if lvl5_button.hovered:
            lvl5_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                lvl5_button.toggle_bg(colors.THEME_ALT)
                print("NO")
        else:
            lvl5_button.toggle_bg(colors.THEME_ALT)

        if lvl6_button.hovered:
            lvl6_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                lvl6_button.toggle_bg(colors.THEME_ALT)
                print("NO")
        else:
            lvl6_button.toggle_bg(colors.THEME_ALT)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
