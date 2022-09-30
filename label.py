import pygame


class Label(pygame.sprite.Sprite):
    def __init__(self, text, x, y, font, color):
        super().__init__()
        self.text = text
        self.pos = x, y
        self.font = font
        self.color = color

        t_surf = self.font.render(self.text, True, self.color)
        self.image = pygame.Surface((t_surf.get_width() + 10, t_surf.get_height() + 10), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.image.blit(t_surf, (5, 5))

    def upd(self, c_dir: str) -> None:
        import os
        if c_dir != "":
            self.text = f"Fichier correction : {os.path.basename(c_dir)}"
            t_surf = self.font.render(self.text, True, self.color)
            self.image = pygame.Surface((t_surf.get_width() + 10, t_surf.get_height() + 10), pygame.SRCALPHA)
            self.rect = self.image.get_rect(topleft=self.pos)
            self.image.blit(t_surf, (5, 5))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
