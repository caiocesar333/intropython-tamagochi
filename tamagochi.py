class Tamagochi:
    def __init__(self, name, hunger = 5, health = 5, boredom = 5, exhaustion = 5, alive = True):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.boredom = boredom
        self.exhaustion = exhaustion
        self.alive = alive

    def decrease_att(self, value):
        if value - 1 < 0:
            return 0
        else: 
            return value - 1

    def increase_att(self, value):
        if value + 1 > 10:
            return 10
        else: 
            return value + 1

    def feed(self, hours):
        for _ in range(hours):
            self.hunger = self.decrease_att(self.hunger)

        print(f"You fed {self.name} for {hours}h. Its hunger is at {self.hunger}")

    def play(self, hours):
        for _ in range(hours):
            self.boredom = self.decrease_att(self.boredom)
            self.hunger = self.increase_att(self.hunger)
            self.exhaustion = self.increase_att(self.exhaustion)
            
        print(f"You played with {self.name} for {hours}h. Its boredom is at {self.boredom}. ")
        print(f"Its hunger and exhaustion increased. Hunger : {self.hunger}. Exhaustion: {self.exhaustion}")

    def sleep(self, hours):
        for _ in range(hours):
            self.exhaustion = self.decrease_att(self.exhaustion)

        print(f"{self.name} slept for {hours}h. Its exhaustion is at {self.exhaustion}")

    def heal(self, hours):
        for _ in range(hours):
            self.health = self.increase_att(self.health)

        print(f"You healed {self.name} for {hours}h. Its health is at {self.health}")

    def reduce_quality_of_life(self):
        self.hunger = self.increase_att(self.hunger)
        self.health = self.decrease_att(self.health) # its a positive att
        self.boredom = self.increase_att(self.boredom)
        self.exhaustion = self.increase_att(self.exhaustion)

    def random_event(self, id):
        if id == 1:
            self.reduce_quality_of_life()
            print(f"{self.name} is living a horrible life. Every attribute was decreased")
        elif id == 2:
            self.health = 0
            print(f"{self.name} got really sick. Its health is at {self.health}")
        elif id == 3:
            self.hunger = self.decrease_att(self.hunger)
            print(f"{self.name} found food. Its hunger is at {self.hunger}")
        elif id == 4:
            self.boredom = self.decrease_att(self.boredom)
            print(f"{self.name} played with its own shadow. But got tired by doing so")
            print(f" Its boredom is at {self.hunger}. Its exhaustion is at {self.exhaustion}")

        if self.health == 0 or self.hunger == 10 or self.boredom == 10 or self.exhaustion == 10:
            self.alive = False


    def is_alive(self):
        return self.alive
    
    def show_status(self):
        print(f" ---------- {self.name} Status ---------- ")
        print(f"Name : {self.name}") 
        print(f"Hunger : {self.hunger}") 
        print(f"Health : {self.health}") 
        print(f"Boredom : {self.boredom}") 
        print(f"Exhaustion : {self.exhaustion}")
        print(f"Is alive : {str(self.is_alive())}")

    def show_name(self):
        alive = "Alive"
        if not self.is_alive():
            alive = "Dead"
        print(f" - {self.name} | Status: {alive} \n")
        return self.name
    
    def return_statistics(self):
        return {"name": self.name, 
            "hunger": self.hunger, 
            "health": self.health, 
            "boredom": self.boredom, 
            "exhaustion": self.exhaustion, 
            "alive": self.alive }

    def return_statistics_as_list(self):
            return [ self.name, 
                self.hunger, 
                self.health, 
                self.boredom, 
                self.exhaustion, self.alive ]

    def load_tam(self, tam_json):
        print(tam_json)
        if type(tam_json) is list:
            self.hunger = int(tam_json[1])
            self.health = int(tam_json[2])
            self.boredom = int(tam_json[3])
            self.exhaustion = int(tam_json[4])
            self.alive = bool(tam_json[5])