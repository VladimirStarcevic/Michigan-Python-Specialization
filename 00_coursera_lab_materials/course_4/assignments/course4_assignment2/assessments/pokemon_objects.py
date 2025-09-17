class Pokemon(object):
    attack = 12  # The "baseline" attack,...
    defense = 10  # defense, and...
    health = 15  # health scores for new Pokemon instances
    p_type = "Normal"
    strong_vs = [] # The "type" (like 'Normal', 'Water', 'Fire', etc.) helps determine how effective certain moves will be

    attack_boost = 3  # When we "train", this is how much we increment our attack,...
    defense_boost = 2  # defense, and...
    health_boost = 5  # health

    evolution_threshold = 10  # How many times we need to train before we "evolve"

    def __init__(self, name, level=5):
        self.name = name  # The name for this *instance*
        self._level = level  # The starting level for this instance (the initial underscore signals that it is a private variable)

    @property
    def level(self):  # *GETTER* for the 'level' property
        return self._level

    @level.setter
    def level(self, value):  # *SETTER* for the 'level' property, ensuring that it is at least 1
        if value < 1:
            raise ValueError("Level must be greater than or equal to 1")
        self._level = value

    def train(self):
        # Increment attack, defense, and health levels
        self.attack_up()
        self.defense_up()
        self.health_up()

        self.level = self.level + 1

        evolved = (self.level % self.evolution_threshold == 0)  # Did we "evolve" on this step?

        return self.level, evolved  # Return a tuple with the current level and whether we evolved

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def is_strong_vs(self, opponent):
        opponent_type = opponent.p_type
        return opponent_type in self.strong_vs

    def is_weak_vs(self, opponent):
        return opponent.is_strong_vs(self)

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class GrassPokemon(Pokemon):
    attack = 15  # base levels for grass pokemon
    defense = 14
    health = 12
    p_type = "Grass"
    strong_vs = ["Water"]

    attack_boost = 2  # when we "train", how much to increment by
    defense_boost = 3
    health_boost = 6

    evolution_threshold = 12  # How many times we need to train before we "evolve"

    def train(self):
        current_level_before_train = self.level

        self.defense_up()
        self.health_up()

        if current_level_before_train >= 10:
            self.attack_up()

        self.level += 1

        evolved = (self.level % self.evolution_threshold == 0)
        return self.level, evolved

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return f"{self.name} knows a lot of different moves!"


class FirePokemon(Pokemon):
    p_type = "Fire"
    strong_vs = ["Grass", "Normal"]
class WaterPokemon(Pokemon):
    p_type = "Water"
    strong_vs = ["Fire"]