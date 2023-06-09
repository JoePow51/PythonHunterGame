import random

class Settings:
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game's settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # screen color changed from grey to yellow for semester project; set b back to 230 to revert changes
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = random.randint(3, 4)
        self.fleet_drop_speed = 30.0
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1