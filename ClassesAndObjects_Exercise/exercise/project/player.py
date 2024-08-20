
class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cos: int) -> str:
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cos
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        info = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n" + '\n'.join(f"==={s} - {c}\n" for s, c in self.skills.items())

        return info


