"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.

"""
__author__ = "Jayson Morgado"
__version__ = 2
######################################################################
Field_Text = """You are in a field in your kingdom.
In the west there is a brutally cold mountain.
To the east behind you there is a spooky, ominous cave
The north there is a white sandy beach. And to the south the castle.
Where do you want to travel?"""
Cave_without_knowledge_of_key_Text = """The cave is scary and nearly pitch black.
Not many people travel here as there isn’t much here. You can only return to the field.
Where do you want to travel?"""
Beach_Text = """To the left you see a village filled with life.
Down the shore to the right you see something in the distance out at sea, but you are not sure what it is.
You can go to the village, shore, or to the field.
Where do you want to travel to? """
Mountain_Text = """The Mountain is freezing.
To the left there is a dangerous path too cold to travel. It leads to the home of the Evil Knight.
To the right there is a blacksmith shop, the forge.
You can go to the forge, the peak, or the field.
Where do you want to travel"""
Castle_Text = """Up ahead is the your father's room, The King.
You can either enter the kings room or go back to the field.
Where do you want to travel?"""
Kings_room_first_Text = """Your Father is sick and needs help.
He has been poisoned and needs the cure from the mountain.
It is your destiny to get it. Get the sword from the blacksmith
and tell him what happened. You can only go to the castle.
Good luck. Where do you want to travel?"""
Village_first_Text = """A villager proposes an offer to you.
If you can find his lost key, he will reward you with an object that can control time.
Perhaps you should look for it. Nothing else in the village catches your eye.
You can only return to the beach."""
Village_get_watch_Text = """The villager thanks you. You now have the magic watch which can move time forward.
Where do you want to go?"""
Cave_found_key_Text = """You found the key! Give this back to the villager to
earn your reward. You can only go to the field"""
Shore_without_watch = """You see an island out to the sea.
The water is deep, and the currents move fast. Perhaps you could swim.
Do you want to want to go to the island or the beach?"""
Shore_with_watch = """The tide is too high maybe you can use the magic watch
too change that. What do you want to do?"""
Shore_low_tide_Text = """It is now low tide. You can reach the island.
Where do you want to go?"""
Peak_before_fight =  """The evil knight is at the top of the mountain. He currently has the potion to cure your Father.
He draws his sword to defend it. Use your sword to kill him and save your father. """
Peak_killed_Text = """You were defensely as the evil knight killed you"""
Killed_villian = """You defeated the evil knight in a sword fight.
You took the potion from his pocket. Go save your Father. You can only go to the Mountain"""
Cave_with_key = "Nothing else to do here. You can only go to the field"
Village_with_watch = """Maybe you can use the new magic watch somewhere else.
You can only travel to the beach."""
Villager_needs_key = """'Please I need the key!' The villager begs.
You can only travel to the beach"""
Low_tide = "The tide is now low. You can walk to the island"
Island_with_jacket = """You now have a jacket, which can help you through the cold. 
You can only go the the shore"""
Peak_fight = """Quickly use your sword to killed the Evil Knight!"""
Peak_done = "Go save your father! You can only travel to the mountain"
Forge_done = """You now have your sword, good luck on your quest. 
You can only travel back to the mountain from here"""
Forge_welcome = """'Welcome to The Forge. My family has owned this place for generations. I now run it.' The blacksmith is hard at work. Where do you want to go?"""
Forge_waiting = """'I can make the sword for you, but it may take a while'. The blacksmith said. Perhaps you can use something to speed the process up. What do you want to do?""" 
#######################################################################
locations_that_modify_world = ["kings room","village", "island","peak","forge"]
locations = ["cave", "mountain", "field", "castle", "beach", "kings room","village", "shore", "island","peak","forge"]
locations_from_field = ["cave", "mountain", "beach", "castle"]
locations_from_castle = ["field", "kings room"]
locations_from_beach = ["field","village", "shore"]
locations_from_mountain = ["field","peak","forge"]
locations_from_shore = ["island", "beach"]
locations_from_island = ["shore"]
locations_from_peak = ["mountain"]
commands = ["use magic watch","use sword"]
command_valid_locations = ["shore","peak","forge"]
##########################################################################

class King:
    '''
    Attributes:
        healthy (bool): whether or not the king is healthy
        time_left (number): how many days (moves) left before the king dies
        start_time (bool): whether or not the time has start for the timer 
    '''
    def __init__(self):
        self.healthy = False
        self.time_left = 50
        self.start_time = False
    def change_health(self):
        '''
        Consumes nothing and sets the healthy attribute to True
        Args:
            none
        Return:
            none
        '''
        self.healthy = True
class Player:
    '''
    Attributes:
        location (str): the current location of the player
                        within the world
        inventory (list of strings): the list of the players
                          inventory
        knowledge_of_key  (bool): whether or not the player
                                 knows about the key
        knowledge_of_sword  (bool): whether or not the blacksmith will
                                   the make the sword
    '''
    def __init__(self, given_location, given_inventory):
        self.location = given_location
        self.inventory = given_inventory
        self.knowledge_of_key = False
        self.knowledge_of_sword = False
        self.sword_done = False
    def change_knowledgeofsword(self):
        '''
        Consumes nothing and changes the knowledge of sword attribute to true
        Args:
            None
        Return:
            None
        '''
        self.knowledge_of_sword = True
    def set_location(self, string):
        '''
        Consumes a string and changes the location attribute to the string
        Args:
            String (string): location
        Return:
            None
        '''
        self.location = string
    def change_sworddone(self):
        '''
        Consumes nothing and sets the sword_done attribute to true
        Args:
            None
        Return:
            None
        '''
        self.sword_done = True
king = King()       
player = Player("field", [])
class World:
    '''
    Attributes:
        game_status (str):Whether the game is in
                          progress or has ended. Either "playing",
                          "won", or "lost".
        player (Player): The player character's info.
        high_tide  (bool): whether or not the player can
                           reach the island
        king  (King): contains the information related to the king
        villager_has_key  (bool): if true the player recieves the
                                  hourglass
        villian_killed  (bool): if true player receives potion
    '''
    def __init__(self):
        self.game_status = "playing"
        self.player = player
        self.high_tide  = True 
        self.king = king
        self.villager_has_key = False 
        self.villian_killed = False
    def change_hightide(self):
        '''
        Consumes nothing and sets the current hightide state to the opposite
        Args:
            none
        Return:
            none
        '''
        self.high_tide = False
    def is_done(self):
        '''
        consumes a world state, checks too see if the game should end
        Args:
            self (world): current world state
        Return: a boolean
        '''
        if self.game_status in ("won", "lost", "quit") or self.king.healthy == True:
            return True
        else:
            return False
    def is_good(self):
        '''
        Consumes a world state checks to see if it is valid
        Args:
            self (world): current world state
        Returns: a boolean
        '''
        if self.game_status in ("playing", "won", "lost"):
            return True
        else:
            return False
    def render(self):
        '''
        Consumes a world state, returns a string
        Args:
            self (world): current world state
        Returns: string to be displayed based on the world state
        '''
        if self.player.location == "field":
            return Field_Text
        elif self.player.location == "cave":
            return Cave_textFun(self)
        elif self.player.location == "beach":
            return Beach_Text
        elif self.player.location == "mountain":
            return Mountain_Text
        elif self.player.location == "castle":
            return Castle_Text
        elif self.player.location == "kings room":
            return Kings_room_first_Text
        elif self.player.location == "village":
            return Village_Text(self)
        elif self.player.location == "shore":
            return Shore_Text(self)
        elif self.player.location == "island":
            return Island_Text(self)
        elif self.player.location == "peak":
            return Peak_Text(self)
        elif self.player.location == "forge":
            return Forge_Text(self)
    def is_input_good(self, string):
        '''
        Consumes a world state and a user command to test if the command is valid
        Args:
            self (world): current world state
            string (string): what the user wants to do
        Return:
            boolean, true if the command is valid for the current world state
        '''
        if string[10:] in locations:
            return location_command_valid(string[10:], self.player.location)
        elif string in commands:
            return self.player.location in command_valid_locations
        elif string == "quit":
            return True
        else:
            return False
    def process(self, string):
        '''
        Consumes a world state and a string, modifies the world state based on the string
        Args:
            self (world): current world state
            string (string): command user enters
        Returns: None
        '''
        if string[10:] in locations_that_modify_world:
            modify(self, string[10:])
        elif string.startswith("go to the"):
            self.player.set_location(string[10:])
        elif string[:3] == "use":
            using_invent(self, string)
        elif string == "quit":
            self.game_status = "quit"
    def tick(self):
        '''
        Consumes a world state and consistently updates the game
        Args:
            self (world): current world state
        Returns: None
        '''
        if self.king.start_time == True:
            self.king.time_left -= 1
            if self.king.time_left == 0:
                self.game_status = "lost"
                
    def render_ending(self):
        '''
        Consumes a world state and produces a string to print at the end of the game
        Args:
            self(world): current world state
        Return: String showing result of the game
        '''
        if self.game_status == "lost" and self.king.time_left == 0:
            return "Your Father died Game Over"
        elif self.player.location == "island":
            return "You drowned!"
        elif self.player.location == "peak" and "jacket" not in self.player.inventory:
            return "You froze while climbing the mountain"
        elif self.player.location == "peak" and "sword" not in self.player.inventory:
            return "You made it up the mountain. But the Evil Knight was prepared and you were defenseless"
        elif self.game_status == "lost":
            return "You Died, Game Over"
        elif self.king.healthy == True:
            return "You saved your Father from untimely death. Your legacy is immortalized"
        elif self.game_status == "quit":
            return "thanks for playing"
    def render_start(self):
        '''
        consumes a world state and produces a string
        Args:
            self (world): beginning world state
        Returns a string
        '''
        return """QUEST
By: Jayson Morgado
To travel to a location, type "go to the ..."
To use an item, type "use ..."
type in all lowercase
----------------------------------------"""
##############################################################################################3

def Cave_textFun(self):
    '''
    Consumes a world state to see what to print
    Args:
        self (world): current world state
    '''
    if "key" in self.player.inventory:
        return Cave_with_key 
    elif self.player.knowledge_of_key == True:
        self.player.inventory.append("key")
        return Cave_found_key_Text
    else:
        return Cave_without_knowledge_of_key_Text
#assert Cave_textFun(worldTest) == Cave_without_knowledge_of_key_Text
############################################################################
def Village_process(self):
    '''
    Consumes a command and a world state
    Args:
        self (world): current world state
        command (string): user input
    Returns: none
    '''
    self.player.set_location("village")
    if self.player.knowledge_of_key == True and "key" in self.player.inventory:
        self.player.inventory.append("magic watch")
        self.villager_has_key == True
#assert Village_process(worldTest) == None
def Village_Text(self):
    '''
    Consumes a command and a world state
    Args:
        self (world): current world state
        command (string): user input
    Returns: none
    '''
    if self.villager_has_key == True:
        return Village_with_watch
    elif self.player.knowledge_of_key == True and "key" in self.player.inventory:
        return Village_get_watch_Text
    elif self.player.knowledge_of_key == False:
        self.player.knowledge_of_key = True
        return Village_first_Text
    else:
        return Villager_needs_key
#assert Village_Text(worldTest) == Village_first_Text 
################################################################################
def Shore_Text(self):
    '''
    Consumes a world state
    Args:
        self (world): current world state
        command (string): user input
    Returns: string to be displayed
    '''
    if self.high_tide == False and "jacket" not in self.player.inventory:
        return Low_tide
    elif self.high_tide == False:
        return Shore_low_tide_Text
    elif "magic watch" in self.player.inventory:
        return Shore_with_watch
    else:
        return Shore_without_watch
def Shore_Process(self, command):
    '''
    Consumes a command and a world state and updates the world state based on the command
    Args:
        self (world): current world state
        command (string): user input
    Returns: none
    '''
    if command == "use magic watch":
        self.change_hightide()
################################################################################
def Island_Text(self):
    '''
    Consumes a world state and produces a string
    Args:
        self (world): current world state
    Returns: string to display based on the world
    '''
    self.player.set_location("island")
    if self.high_tide == False and "jacket" in self.player.inventory:
        return Island_with_jacket
def Island_process(self):
    '''
    Consumes a command and a world state and updates the world state based on the command
    Args:
        self (world): current world state
        command (string): user input
    Returns: none
    '''
    self.player.location = "island"
    if self.high_tide == False:
        self.player.inventory.append("jacket")
    elif self.high_tide == True:
        self.game_status = "lost"
################################################################################
def Kings_Room_process(self):
    '''
    Consumes world state and updates the world state based on the current world
    Args:
        self (world): current world state
    Returns: none
    '''
    self.player.set_location("kings room")
    if "potion" in self.player.inventory:
        self.king.change_health()
    else:
        self.king.start_time = True
        self.player.change_knowledgeofsword()
################################################################################
def Peak_Process(self, command):
    '''
    Consumes a world state and updates the world state based on the current one
    Args:
        self (world): current world state
    Return: none
    '''
    self.player.set_location("peak")
    if command == "use sword" and "sword" in self.player.inventory and self.villian_killed == False:
        self.player.inventory.append("potion")
        self.villian_killed = True
    elif "jacket" not in self.player.inventory or "sword" not in self.player.inventory:
        self.game_status = "lost"
def Peak_Text(self):
    '''
    Consumes a world state and returns the apporitate text
    Args:
        self (world): current world state
    Return: None
    '''
    if self.villian_killed == False:
        return Peak_fight
    elif self.villian_killed == True: 
        return Killed_villian
###################################################################
def Forge_Text(self):
    '''
    Consumes a world state and returns the apporitate text
    Args:
        self (world): current world state
    Return: None
    '''
    if "sword" in self.player.inventory:
        return Forge_done
    elif self.player.knowledge_of_sword == False:
        return Forge_welcome 
    elif self.player.knowledge_of_sword == True:
        return """'I can make the sword for you, but it may take a while'. Perhaps you can use something to speed the process up
What do you want to do"""
def Forge_Process(self, command):
    '''
    Consumes a world state and updates the world state based on the current one
    Args:
        self (world): current world state
    Return: none
    '''
    self.player.set_location("forge")
    if self.player.sword_done == True:
        pass
    elif command == "use magic watch" and "magic watch" in self.player.inventory and self.player.knowledge_of_sword == True:
        self.player.change_sworddone() 
        self.player.inventory.append("sword")
########################################################################################
        
def location_command_valid(command, current):
    '''
    Consumes two strings and returns a boolean
    Args:
        command (string): where the user wants to travel too
        current (string): where the user currently is
    Returns:
        a boolean based in wheter the user can travel there
    '''
    if current == "field":
        return command in locations_from_field
    elif current == "castle":
        return command in locations_from_castle
    elif current == "beach":
        return command in locations_from_beach
    elif current == "mountain":
        return command in locations_from_mountain
    elif current == "cave":
        return command == "field"
    elif current == "kings room":
        return command == "castle"
    elif current == "village":
        return command == "beach"
    elif current == "shore":
        return command in locations_from_shore
    elif current == "island":
        return command == "shore"
    elif current == "forge":
        return command == "mountain"
    elif current == "peak":
        return command == "mountain"
assert location_command_valid("field", "cave") == True
assert location_command_valid("castle", "field") == True
assert location_command_valid("beach","shore") == True
assert location_command_valid("mountain","forge") == True
assert location_command_valid("cave","field") == True
assert location_command_valid("kings room", "castle") == True
assert location_command_valid("village","beach") == True
assert location_command_valid("shore","island") == True
assert location_command_valid("island","shore") == True
assert location_command_valid("forge", "mountain") == True
assert location_command_valid("peak","mountain") == True
assert location_command_valid("mountain","peak") == True
assert location_command_valid("beach","village") == True
assert location_command_valid("castle", "kings room") == True
def modify(self, command):
    '''
    Consumes a world state and a command
    Args:
        self (world): current world state
        command (string): command user entered
    Return:
        modified world state
    '''
    if command == "kings room":
        Kings_Room_process(self)
    elif command == "village":
        Village_process(self)
    elif command == "island":
        Island_process(self)
    elif command == "peak":
        Peak_Process(self, command)
    elif command == "forge":
        Forge_Process(self, command)

def using_invent(self, string):
    '''
    Consumes a world state and modifies it
    Args:
        self (world): a world state
    Return: None
    '''
    if self.player.location == "shore":
        Shore_Process(self, string)
    elif self.player.location == "peak":
        Peak_Process(self, string)
    elif self.player.location == "forge":
        Forge_Process(self, string)
###########################################################################

    

    
# Command Paths to give to the unit tester
LOSE_PATH = ["go to the beach", "go to the shore", "go to the island"]
WIN_PATH = ["go to the castle", "go to the kings room", "go to the castle", "go to the field","go to the beach","go to the village","go to the beach", "go to the field", "go to the cave", "go to the field", "go to the beach", "go to the village", "go to the beach","go to the shore", "use magic watch", "go to the island", "go to the shore", "go to the beach","go to the field","go to the mountain", "go to the forge","use magic watch","go to the mountain","go to the peak","use sword", "go to the mountain", "go to the field", "go to the castle", "go to the kings room"]



#####################################
#############CODE COVERAGE####################
#####################################
worldt = World()
worldt.render_start()
worldt.process("go to the mountain")
assert worldt.is_done() == False
assert worldt.render() == Mountain_Text
worldt.process("go to the peak")
worldt.game_status = "playing"
worldt.process("go to the forge")
assert worldt.render() == Forge_welcome
worldt.process("go to the field")
assert worldt.render() == Field_Text
worldt.process("go to the castle")
assert worldt.render() == Castle_Text
worldt.process("go to the kings room")
assert worldt.render() == Kings_room_first_Text   
worldt.process("go to the cave")
assert worldt.render() == Cave_without_knowledge_of_key_Text
worldt.process("go to the beach")
assert worldt.render() == Beach_Text
worldt.process("go to the shore")
assert worldt.render() == Shore_without_watch
worldt.process("go to the island")
worldt.game_status = "playing"
worldt.process("go to the village")
assert worldt.render() == Village_first_Text
worldt.process("go to the beach")
worldt.process("go to the village")
assert worldt.render() == Villager_needs_key
worldt.process("go to the cave")
assert worldt.render() == Cave_found_key_Text
worldt.process("go to the field")
worldt.process("go to the cave")
assert worldt.render() == Cave_with_key
worldt.process("go to the village")
assert worldt.render() == Village_get_watch_Text
worldt.process("go to the beach")
worldt.process("go to the village")
assert worldt.render() == Village_get_watch_Text
worldt.process("go to the shore")
worldt.process("use magic watch")
assert worldt.render() == Low_tide
worldt.process("go to the island")
assert worldt.render() == Island_with_jacket
worldt.process("quit")
worldt.game_status = "playing"
assert worldt.is_input_good("quit") == True 
assert worldt.is_input_good("a") == False
worldt.process("go to the shore")
assert worldt.render() == Shore_low_tide_Text
assert worldt.is_input_good("go to the field") == False
worldt.process("go to the forge")
worldt.render() 
assert worldt.is_input_good("use magic watch") == True
worldt.process("use magic watch")
assert worldt.render() == Forge_done
worldt.process("go to the peak")
assert worldt.render() == Peak_fight
worldt.game_status = "F"
assert worldt.is_good() == False
worldt.game_status = "playing"
worldt.process("use sword")
assert worldt.render() == Killed_villian
worldt.process("go to the forge") 
worldt.process("go to the mountain")
worldt.process("go to the peak")
worldt.render() 
worldt.tick()
worldt.king.time_left = 0
worldt.tick()
assert worldt.is_good() == True
worldt.process("go to the kings room")
worldt.render()
worldt.is_done()
worldt.game_status = "lost"
assert worldt.render_ending() == "You Died, Game Over"
worldt.king.time_left = 0
assert worldt.render_ending() == "Your Father died Game Over"
worldt.game_status = "playing"
worldt.player.location = "island"
assert worldt.render_ending() == "You drowned!"
worldt.player.location = "peak"
worldt.player.inventory = []
assert worldt.render_ending() == "You froze while climbing the mountain"
worldt.player.inventory = ["jacket"]
assert worldt.render_ending() == "You made it up the mountain. But the Evil Knight was prepared and you were defenseless"
worldt.player.location = "kings room"
worldt.king.healthy = True
assert worldt.render_ending() == "You saved your Father from untimely death. Your legacy is immortalized"
worldt.king.healthy = False
worldt.game_status = "quit"
assert worldt.render_ending() == "thanks for playing"

player.location = "field"
player.inventory = []
player.knowledge_of_key = False
player.knowledge_of_sword = False
king.healthy = False
king.start_timer = False
player.sword_done = False
##################################
###################################

def main():
    '''
    This is the Main game function. When executed, it begins a run of the game.
    Read over it to understand the engine that you are using and the order
    that the methods are executed in.
    '''
    world = World()
    print(world.render_start())
    while not world.is_done():
        if not world.is_good():
            raise ValueError("The world is in an invalid state.", world)
        print(world.render())
        is_input_good = False
        while not is_input_good:
            user_input = input("")
            is_input_good = world.is_input_good(user_input)
        world.process(user_input)
        world.tick()
    print(world.render_ending())

# Executes the main function only if this file is being run directly.
# This prevents the autograder from being confused. Never call main outside
# of this IF statement!
if __name__ == "__main__":
    ## You might comment out the main function and call each function
    ## one at a time below to try them out yourself
    main()
    ## e.g., comment out main() and uncomment the line(s) below
#world = World()
#world.render_start()
#world.process("go to the castle")
#world.process("go to the kings room")
#world.process("go to the castle")

    
    
    




