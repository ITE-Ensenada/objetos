class weapon:
    def __init__(self, type, rng, acc, dmg):
        self.type   = type  #Type of weapon: sword, dagger, bow, spear, axe
        self.rng    = rng   #Hit distance
        self.acc    = acc   #Accuracy
        self.dmg    = dmg   #Damage modifier
