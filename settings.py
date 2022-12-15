class Settings:
    ''' A class to store all settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game's settings'''
        #Screen Settings
        self.screen_width = 960
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 3
        #Fleet direction of 1 represent right; -1 represents lef
        self.fleet_direction = -1

        #Inisialize speed of the game
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.Initialize_dynamic_settings()
    
    def Initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = -1

        #scoring
        self.alien_points = 20

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)