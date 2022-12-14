class Snake:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.length = 1
        self.body = [(self.x, self.y)]

    def move(self):
        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1

        self.body.insert(0, (self.x, self.y))
        self.body = self.body[:self.length]

    def check_collision(self, food):
        if self.x == food.x and self.y == food.y:
            self.length += 1
            food.move()

    def check_wall_collision(self):
        if self.x < 0 or self.x > 19 or self.y < 0 or self.y > 14:
            return True
        return False

    def check_self_collision(self):
        if (self.x, self.y) in self.body[1:]:
            return True
        return False

    def get_head_position(self):
        return self.x, self.y

    def get_length(self):
        return self.length
