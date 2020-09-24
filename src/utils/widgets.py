"""
Widgets for the mastermind game
"""
import pygame


class TextButton:
    """PyGame text button class."""

    def __init__(self, surface, pos, width, height, fg_color, bg_color, font, text):

        self.surface = surface
        self.width = width
        self.height = height
        self.pos = pos
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.font = font
        self.text = text

        self.top_border = pos[1]  # Y of top left of rect
        self.right_border = pos[0] + width  # X of top left of rect plus width
        self.bottom_border = pos[1] + height  # Y of top left of rect plus height
        self.left_border = pos[0]  # X of top left of rect

        # Render font
        text_surface = font.render(text, True, fg_color)
        text_rect = text_surface.get_rect()
        # Center text on button
        text_rect.center = (self.left_border + (self.right_border - self.left_border) / 2,
                            self.top_border + (self.bottom_border - self.top_border) / 2)
        # render text and button
        if bg_color:
            pygame.draw.rect(surface, bg_color, (pos[0], pos[1], width, height))
        surface.blit(text_surface, text_rect)

    @property
    def hovered(self):
        """Return a boolean representing if mouse is hovering over button."""
        row, col = pygame.mouse.get_pos()
        if self.left_border <= row <= self.right_border and self.top_border <= col <= self.bottom_border:
            return True
        else:
            return False

    # @property
    # def clicked(self):
    #     """Return a boolean representing if any mouse button has clicked (but not released) the button."""
    #     if not all(val == 0 for val in pygame.mouse.get_pressed()):
    #         if self.hovered:
    #             return True
    #     return False

    def toggle_bg(self, bg_new_color):
        """Change a button's background color."""
        # Save change to bg
        self.bg_color = bg_new_color
        # Render font
        text_surface = self.font.render(self.text, True, self.fg_color)
        text_rect = text_surface.get_rect()
        # Center text on button
        text_rect.center = (self.left_border + (self.right_border - self.left_border) / 2,
                            self.top_border + (self.bottom_border - self.top_border) / 2)
        # Render text and button
        pygame.draw.rect(self.surface, bg_new_color, (self.pos[0], self.pos[1], self.width, self.height))
        self.surface.blit(text_surface, text_rect)


# def draw_text(surface, fg, bg, font, text, rect):
#     """Draw text and automatically wrap words to fit into rect. Return text that didn't fit."""
#     rect = pygame.Rect(rect)
#     rect_top = rect.top
#     line_spacing = -2
#
#     # get the height of the font
#     font_height = font.size("Tg")[1]  # using Tg as Tg gives limits
#
#     while text:
#         i = 1
#
#         # determine if the row of text will be outside our area
#         if rect_top + font_height > rect.bottom:
#             break
#
#         # determine maximum width of line
#         while font.size(text[:i])[0] < rect.width and i < len(text):
#             i += 1
#
#         # if we've wrapped the text, then adjust the wrap to the last word
#         if i < len(text):
#             i = text.rfind(" ", 0, i) + 1
#
#         # render the line and blit it to the surface
#         image = font.render(text[:i], 1, fg, bg)
#         image.set_colorkey(bg)
#
#         surface.blit(image, (rect.left, rect_top))
#         rect_top += font_height + line_spacing
#
#         # remove the text we just blitted
#         text = text[i:]
#
#     return text
