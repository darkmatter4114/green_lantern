class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {"E": "N",
                 "N": "W",
                 "W": "S",
                 "S": "E",
                 }
        self.direction = turns[self.direction]
        print(self.direction)

    def turn_right(self):
        turns = {"N": "E",
                 "E": "S",
                 "S": "W",
                 "W": "N",
                 }
        self.direction = turns[self.direction]

    def move_forward(self, steps):
        if self.direction == "E":
            if self.x + steps > self.asteroid.x:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.x = + steps
        elif self.direction == "N":
            if self.y + steps > self.asteroid.y:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.y += steps
        elif self.direction == "W":
            if (self.x - steps) < 0:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.x -= steps
        elif self.direction == "S":
            if self.y - steps < 0:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.y -= steps

    def move_backward(self, steps):
        if self.direction == "E":
            if self.x - steps < 0:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.x -= steps
        if self.direction == "N":
            if self.y - steps < 0:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.y -= steps
        if self.direction == "W":
            if self.y + steps > self.asteroid.y:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.y += steps
        if self.direction == "S":
            if self.x + steps > self.asteroid.x:
                raise ValueError("The Robot fell from the asteroid")
            else:
                self.x += steps


class MissAsteroidError(Exception):
    print("Miss asteroid")


class RobotFallFromAsteroid(Exception):
    pass


if __name__ == '__main__':
    asteroid = Asteroid(20, 30)
    robot = Robot(10, 13, asteroid, "E")
    robot.move_forward(20)

