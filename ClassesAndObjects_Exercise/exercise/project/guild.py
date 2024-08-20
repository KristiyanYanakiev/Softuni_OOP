from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        for p in self.players:
            if p.name == player_name:
                p.guild = "Unaffiliated"
                self.players.remove(p)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = f"Guild: {self.name}\n"
        for p in self.players:
            result += p.player_info()
        return result



