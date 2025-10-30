class Hero:
    def __init__(self, name, health, attackPower, armorPower):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorPower =  armorPower

    def show(self):
        print ("Nama Hero: ", self.name,  
               "Health: ", self.health, 
               "Power: ", self.attackPower, 
               "Armor: ", self.armorPower)
        
    def serang (self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower)
    

    def diserang (self, lawan, attackPower_lawan):
        print(self.name + " telah diserang oleh " + lawan.name)
        attackReceived = attackPower_lawan/self.armorPower
        print("serangan diterima ", str(attackReceived))
        self.health -= attackReceived
        print("health tersisa dari " , self.name, "adalah ", self.health)
        

sniper = Hero ('sniper', 100, 10, 30)
zilong = Hero ('zilong', 90, 20, 20)

sniper.show()
zilong.show()
print("\n" *3)
sniper.serang(zilong)
print("\n" *1)
zilong.serang(sniper)

sniper.serang(zilong)
print("\n" *1)
zilong.serang(sniper)
sniper.serang(zilong)
print("\n" *1)
zilong.serang(sniper)
sniper.serang(zilong)
print("\n" *1)
zilong.serang(sniper)
