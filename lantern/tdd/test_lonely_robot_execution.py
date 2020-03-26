import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, 'W')


class TestTurns:
    def setup(self):
        x, y = 10, 15
        self.asteroid = Asteroid(x * 2, y * 2)

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N"),
        )

    )
    def test_turn_left(self, current_direction, expected_direction):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        (
                ("N", "E"),
                ("E", "S"),
                ("S", "W"),
                ("W", "N"),
        )

    )
    def test_turn_right(self, current_direction, expected_direction):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    # class TurnON:
    @pytest.mark.parametrize(
        "current_direction, steps, expec_loc",
        (
                ("N", 3, (10, 18)),
                ("W", 7, (10, 8)),
                ("S", 5, (5, 15)),
                ("E", 9, (25, 15)),
        )

    )
    def test_move_forward(self, current_direction, steps, expec_loc):
        x, y = 10, 15
        asteroid = Asteroid(x * 2, y * 2)
        robot = Robot(x, y, asteroid, current_direction)
        robot.move_forward(steps)
        assert robot.x, robot.y == expec_loc

    @pytest.mark.parametrize(
        "current_direction, steps, expec_loc",
        ([
            ("E", 2, (8, 15)),
            ("N", 3, (10, 18)),
            ("W", 7, (10, 8)),
            ("S", 5, (5, 15)),

        ])

    )
    def test_move_backward(self, current_direction, steps, expec_loc):
        x, y = 10, 15
        asteroid = Asteroid(x * 2 , y * 2 )
        robot = Robot(x, y, asteroid, current_direction)
        robot.move_backward(steps)
        assert robot.x, robot.y == expec_loc

    def test_fall_robot(self):
        x, y = 10, 15
        asteroid = Asteroid(x * 2 + 1, y * 2 + 1)
        robot = Robot(x, y, asteroid, "E")
        with pytest.raises(ValueError):
            robot.move_forward(100)
        with pytest.raises(ValueError):
            robot.move_backward(100)