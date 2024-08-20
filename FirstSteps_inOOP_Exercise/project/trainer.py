from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        for p in self.pokemons:
            if pokemon.name == p.name:
                return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"


    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if pokemon_name == p.name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = ""

        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            result += f"- {p.name} with health {p.health}"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
