class Pokemon():
  def __init__(self, name, level, types, maxhealth, currenthealth, knockedout):
    self.name = name
    self.level = level
    self.type = types
    self.max_health = maxhealth
    self.health = currenthealth
    self.knocked_out = knockedout


  def lost_health(self, numero):
    self.health -= numero
    if self.health <= 0:
      self.health = 0
      self.knocked_out = True
      print(self.name + " knocked out")
    else:
      print(f"{self.name} now has {self.health} health")
    return


  def gain_health(self, num):
    self.health += num
    if self.health > self.max_health:
      self.health = self.max_health

  def attack(self, other_pokemon):
    x = self.level
    if self.type == "Fire" and other_pokemon.type == "Grass":
      x = 2 * x
    elif self.type == "Grass" and other_pokemon.type == "Fire":
      x = x / 2
    other_pokemon.lost_health(x)
    print(f"{other_pokemon.name} has now {other_pokemon.health} health points") 
    return


class Trainer():
  def __init__(self, name, potions, pokes, active_pokes):
    self.name = name
    self.pokemons = pokes 
    self.potions = potions
    self.active_pokemons = active_pokes

  def use_potion(self):
    if self.potions > 0:
      active_poke = self.pokemons[self.active_pokemons]
      if active_poke.health < active_poke.max_health:
        active_poke.gain_health(20)
        self.potions -= 1
        print(f"potion used on {active_poke.name}. it now has {active_poke.health} health points") 
        print(f"{self.potions} potions left")   
      else:
        print("Active pokemon already has full health")

  def attack_trainer(self, potion, other_trainer):
    active_pokemon = self.pokemons[self.active_pokemons]
    other_active_pokes = other_trainer.pokemons[other_trainer.current_pokemons] 
    active_pokemon.attack(other_active_pokes)
    return None

  def switch_pokemon(self, new_poke):
    if new_poke >= len(self.pokemons):
      print("invalid pokemon")
      return 
    if self.pokemons[new_poke].knocked_out:
     print(f"{self.pokemons[new_poke].name} is knocked out, can't be activated")
     return
    else:
      self.active_pokemons = new_poke
      print(f"{self.name} switched to {self.pokemons[new_poke].name}")
