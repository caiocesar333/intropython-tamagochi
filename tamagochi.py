class Tamagochi:
    def __init__(self, name, hunger = 5, health = 5, boredom = 5, exhaustion = 5, alive = True):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.boredom = boredom
        self.exhaustion = exhaustion
        self.alive = alive

    def reduce_att(self, value):
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
            self.hunger = self.reduce_att(self.hunger)

        print(f"You fed {self.name} for {hours}h. Its hunger is at {self.hunger}")

    def play(self, hours):
        for _ in range(hours):
            self.boredom = self.reduce_att(self.boredom)

        print(f"You played with {self.name} for {hours}h. Its boredom is at {self.boredom}")

    def sleep(self, hours):
        for _ in range(hours):
            self.exhaustion = self.reduce_att(self.exhaustion)

        print(f"{self.name} slept for {hours}h. Its exhaustion is at {self.exhaustion}")

    def heal(self, hours):
        for _ in range(hours):
            self.health = self.increase_att(self.health)

        print(f"You healed {self.name} for {hours}h. Its health is at {self.health}")

    def show_status(self):
        print(f" ---------- {self.name} Status ---------- ")
        print(f"Name : {self.name}") 
        print(f"Hunger : {self.hunger}") 
        print(f"Health : {self.health}") 
        print(f"Boredom : {self.boredom}") 
        print(f"Exhaustion : {self.exhaustion}")

    def reduce_quality_of_life(self):
        self.hunger = self.reduce_att(self.hunger)
        self.health = self.increase_att(self.health) # its a positive att
        self.boredom = self.reduce_att(self.boredom)
        self.exhaustion = self.reduce_att(self.exhaustion)

    def random_event(self, id):
        if id == 1:
            self.reduce_quality_of_life(self)
        if id == 2:
            self.health = 1
            print(f"{self.name} got really sick. Its health is at {self.health}")
        if id == 3:
            self.hunger = self.reduce_att(self.hunger)
            print(f"{self.name} found food. Its hunger is at {self.hunger}")
            
        if id == 4:
            self.boredom = self.reduce_att(self.boredom)
            print(f"{self.name} played with his own shadow. But it got tired doing so")
            print(f" Its boredom is at {self.hunger}. Its exhaustion is at {self.exhaustion}")

        
    def show_name(self):
        print(f" - {self.name} ")
        return self.name
        
