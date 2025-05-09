import numpy as np

# Value Sanitizers
def _san_location(location):
    if not isinstance(location, tuple):
        raise TypeError(f"Value for \'location\' must be tuple, received {type(location)}")
    if len(location) != 2:
        raise ValueError(f"Length of \'location\' tuple must be 2, received {len(location)}")
    if (not isinstance(location[0], float)) and (not isinstance(location[0], int)):
        raise TypeError(f"Location tuple \'values\' must contain float, received {type(location[0])}")
    if (not isinstance(location[1], float)) and (not isinstance(location[0], int)):
        raise TypeError(f"Location tuple \'values\' must contain float, received {type(location[1])}")
    return tuple((float(location[0]), float(location[1])))

def _san_rotation(rotation):
    if (not isinstance(rotation, float)) and (not isinstance(rotation, int)):
        raise TypeError(f"Value for \'rotation\' must be float, received {type(rotation)}")
    if rotation >= 360:
        rotation %= 360
    if rotation < 0:
        rotation = 360 - (abs(rotation) % 360)
    return float(rotation)

def _san_team(team):
    if not isinstance(team, int):
        raise TypeError(f"Value for \'team\' must be int, received {type(team)}")
    return team

def _san_score(score):
    if not isinstance(score, int):
        raise TypeError(f"Value for \'score\' must be int, received {type(score)}")
    if score < 0:
        raise ValueError(f"Value for \'score\' must be 0 or greater, received {score}")
    return score

def _san_velocity(velocity):
    if not isinstance(velocity, tuple):
        raise TypeError(f"Value for \'velocity\' must be tuple, received {type(velocity)}")
    if len(velocity) != 2:
        raise ValueError(f"Length of \'velocity\' tuple must be 2, received {len(velocity)}")
    if (not isinstance(velocity[0], float)) and (not isinstance(velocity[0], int)):
        raise TypeError(f"velocity tuple \'values\' must contain float, received {type(velocity[0])}")
    if (not isinstance(velocity[1], float)) and (not isinstance(velocity[0], int)):
        raise TypeError(f"velocity tuple \'values\' must contain float, received {type(velocity[1])}")
    return tuple((float(velocity[0]), float(velocity[1])))

def _san_acceleration(acceleration):
    if not isinstance(acceleration, tuple):
        raise TypeError(f"Value for \'acceleration\' must be tuple, received {type(acceleration)}")
    if len(acceleration) != 2:
        raise ValueError(f"Length of \'acceleration\' tuple must be 2, received {len(acceleration)}")
    if (not isinstance(acceleration[0], float)) and (not isinstance(acceleration[0], int)):
        raise TypeError(f"acceleration tuple \'values\' must contain float, received {type(acceleration[0])}")
    if (not isinstance(acceleration[1], float)) and (not isinstance(acceleration[0], int)):
        raise TypeError(f"acceleration tuple \'values\' must contain float, received {type(acceleration[1])}")
    return tuple((float(acceleration[0]), float(acceleration[1])))

def _san_health(health):
    if (not isinstance(health, int)) and (not isinstance(health, float)):
        raise TypeError(f"Value for \'health\' must be float, received {type(health)}")
    if 0 > health > 1:
        raise ValueError(f"Value for \'health\' must be between 0 and 1, received {health}")
    return float(health)

def _san_max_health(max_health):
    if not isinstance(max_health, int):
        raise TypeError(f"Value for \'max_health\' must be int, received {type(max_health)}")
    if max_health < 1:
        raise ValueError(f"Value for \'max_health\' must be 1 or greater, received {max_health}")
    return max_health

def _san_path(path):
    if not isinstance(path, int):
        raise TypeError(f"Value for \'path\' must be int, received {type(path)}")
    if path < 0:
        raise ValueError(f"Value for \'path\' must be 0 or greater, received {path}")
    return path

def _san_ordinance(ordinance):
    if not isinstance(ordinance, np.ndarray):
        raise TypeError(f"Value for \'ordinance\' must be np.ndarray, received {type(ordinance)}")
    if len(ordinance) == 0:
        return ordinance
    else:
        for entry in range(len(ordinance)):
            if not isinstance(ordinance[entry], Ordinance):
                raise TypeError(f"Values listed in \'ordinance\' must be Ordinance, received {type(ordinance[entry])} at index {entry}")
    return ordinance

def _san_stats(stats):
    if not isinstance(stats, np.ndarray):
        raise TypeError(f"Value for \'stats\' must be np.ndarray, received {type(stats)}")
    for entry in range(len(stats)):
        if not isinstance(stats[entry], int):
            raise TypeError(f"Values listed in \'stats\' must be int, received {type(stats[entry])} at index {entry}")
        if stats[entry] < 0:
            raise ValueError(f"Values listed \'stats\' must be positive, received {stats[entry]} at index {entry}")
    return stats


class Ordinance:
    def __init__(self, location, velocity, acceleration, rotation, parent, size, health, damage):
        pass


class Tank:
    def __init__(self, location, rotation, team, score, velocity=(0, 0), acceleration=(0, 0), health=1, max_health=100, path=0, ordinance=np.array([]), stats=None, allow_san_bypass=False):
        self.__location = None
        self.set_location(location)

        self.__rotation = None
        self.set_rotation(rotation)

        self.__team = None
        self.set_team(team)

        self.__score = None
        self.set_score(score)

        if velocity == (0, 0):
            self.__velocity = (0, 0)
        else:
            self.__velocity = None
            self.set_velocity(velocity)

        if acceleration == (0, 0):
            self.__acceleration = (0, 0)
        else:
            self.__acceleration = None
            self.set_acceleration(acceleration)

        if health == 1:
            self.__health = float(health)
        else:
            self.__health = None
            self.set_health(health)

        if max_health == 100:
            self.__max_health = 100
        else:
            self.__max_health = None
            self.set_max_health(max_health)

        if path == 0:
            self.__path = 0
        else:
            self.__path = None
            self.set_path(path)

        self.__ordinance = None
        self.set_ordinance(ordinance)

        if stats is None:
            stats = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        else:
            self.__stats = None
            self.set_stats(stats)

        self.__allow_san_bypass = allow_san_bypass


    # Property Getters
    @property
    def location(self):
        return self.__location

    @property
    def rotation(self):
        return self.__rotation

    @property
    def team(self):
        return self.__team

    @property
    def score(self):
        return self.__score

    @property
    def velocity(self):
        return self.__velocity

    @property
    def acceleration(self):
        return self.__acceleration

    @property
    def health(self):
        return self.__health

    @property
    def max_health(self):
        return self.__max_health

    @property
    def path(self):
        return self.__path

    @property
    def ordinance(self):
        return self.__ordinance

    @property
    def stats(self):
        return self.__stats


    # Property Setters
    def set_location(self, location, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__location = location
        sanitized = _san_location(location)
        self.__location = sanitized

    def set_rotation(self, rotation, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__rotation = rotation
        sanitized = _san_rotation(rotation)
        self.__rotation = sanitized

    def set_team(self, team, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__team = team
        sanitized = _san_team(team)
        self.__team = sanitized

    def set_score(self, score, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__score = score
        sanitized = _san_score(score)
        self.__score = sanitized

    def set_velocity(self, velocity, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__velocity = velocity
        sanitized = _san_velocity(velocity)
        self.set_velocity(sanitized)

    def set_acceleration(self, acceleration, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__acceleration = acceleration
        sanitized = _san_acceleration(acceleration)
        self.__acceleration = sanitized

    def set_health(self, health, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__health = health
        sanitized = _san_health(health)
        self.__health = sanitized

    def set_max_health(self, max_health, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__max_health = max_health
        sanitized = _san_max_health(max_health)
        self.__max_health = sanitized

    def set_path(self, path, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__path = path
        sanitized = _san_path(path)
        self.__path = sanitized

    def set_ordinance(self, ordinance, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__ordinance = ordinance
        sanitized = _san_ordinance(ordinance)
        self.__ordinance = sanitized

    def set_stats(self, stats, __bypass_san=False):
        if __bypass_san and self.__allow_san_bypass: self.__stats = stats
        sanitized = _san_stats(stats)
        self.__stats = sanitized


    # Property Incrementers
    # Ordinance list
    # YOu don't want to go through all of those objects, so just make tack a new one on
    def launch_ordinance(self):
        pass

    def stat_increase(self):
        pass

    def stat_refund(self, stat):
        pass

    def move(self, time_increment, __bypass_san=False):
        # Time increment input sanitizing
        if (not __bypass_san) or (not self.__allow_san_bypass):
            if (not isinstance(time_increment, float)) and (not isinstance(time_increment, int)):
                raise TypeError(f"Value for \'time_increment\' must be float, received {type(time_increment)}")
            if time_increment <=0:
                raise ValueError(f"Value for \'time_increment\' must be greater than 0, received {time_increment}")

        new_velocity = (self.__velocity[0] + (self.__acceleration[0] * time_increment),
                        self.__velocity[1] + (self.__acceleration[1] * time_increment))

        new_location = (self.__location[0] + (self.__velocity[0] * time_increment),
                        self.__location[1] + (self.__velocity[1] * time_increment))

        # NOT SANITIZED
        self.__velocity = new_velocity
        self.__location = new_location
