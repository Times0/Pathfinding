import pygame

"""
Font : basicfont = pygame.font.SysFont('comicsans', 30)
Create button instance : Button()
Add sprite group : self.btns_group = pygame.sprite.Group()
Update state in the while loop: self.btns_group.update(eves)
"""

BLACK = 0, 0, 0
GRAY = (185, 224, 226)

TEXTCOLORDEFAULT = 255, 255, 255
TEXTCOLORONHOVER = GRAY


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, text, back_color, text_color, font, outline, onclick, hover_backcolor=None,
                 hover_textcolor=None):
        super().__init__()
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.width = w
        self.text = text
        self.font = font

        self.back_color_default = back_color
        self.back_color = back_color

        self.textcolor_default = text_color
        self.textcolor = text_color

        self.hover_backcolor = hover_backcolor
        self.hover_textcolor = hover_textcolor
        self.onclick = onclick

        self.outline = outline
        self.draw()

    def draw(self):
        t_surf = self.font.render(self.text, True, self.textcolor, self.back_color)
        self.image = pygame.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10),
                                    pygame.SRCALPHA)
        self.image.fill(self.back_color)
        self.image.blit(t_surf, (5, 5))

        if self.outline:
            pygame.draw.rect(self.image, BLACK, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.isMouseOnIt(event.pos):
                    self.hover()
                else:
                    self.default()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if self.isMouseOnIt(event.pos):
                    self.onclick()

    def isMouseOnIt(self, pos):
        return self.rect.collidepoint(*pos)

    def hover(self):
        if self.hover_backcolor:
            self.back_color = self.hover_backcolor
        if self.hover_textcolor:
            self.textcolor = self.hover_textcolor

    def default(self):
        self.back_color = BLACK
        self.textcolor = BLACK


class ButtonImg(pygame.sprite.Sprite):
    def __init__(self, img, x, y, onclick):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(center=(x, y))
        self.x, self.y = x, y
        self.pos = x, y
        self.onclick = onclick

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.isMouseOn(event.pos):
                    self.onclick()

    def isMouseOn(self, pos):
        return self.rect.collidepoint(*pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
