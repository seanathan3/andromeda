from django.db import models

# Create your models here.

class Player(models.Model):
    username = models.CharField(max_length=30)

    MAX_INTERNAL_HEALTH = 10
    MAX_NUM_DEFENSE_UNITS = 2
    MAX_NUM_OFFENSE_UNITS = 4

    cur_internal_health = 10
    cur_num_defense_units = 0
    cur_num_offense_units = 0
    
    energy = models.IntegerField()
    tower_type = models.IntegerField()
    d_bench = [] #defense bench (max 2 units)
    o_bench = [] #offense bench (max 4 units)

    def __str__(self):
        return self.username


class BaseTower(models.Model):    
    MAX_HEALTH = 20
    cur_health = 20

    def take_damage(self, damage_amount):
        self.cur_health -= damage_amount

        if self.cur_health <= 0:
            self.destroy_tower()

    def heal_self(self, heal_amount):
        self.cur_health += heal_amount

        if self.cur_health > 20:
            self.cur_health = 20

class MoatTower(BaseTower):
    def use_ability(enemy_units):
        for unit in enemy_units:
            unit.take_damage(1)


class Card(models.Model):
    name = models.CharField(max_length=30, default='name')
    cost = models.IntegerField()
    def __str__(self):
        return self.name

class Unit(Card):
    max_health = models.IntegerField()
    health = models.IntegerField()
    power = models.IntegerField()
    ranged = models.BooleanField()

    def get_power(self):
        return self.power
    
    def get_health(self):
        return self.health

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.kill_self()
    
    def heal_self(self, amount):
        self.heal_self += amount

        if self.health > self.max_health:
            self.health = self.max_health
    
    def attack(self, target, damage):
        target.take_damage(damage)
        if self.ranged == False:
            self.take_damage(target.get_power())

    #def kill_self(self):
    

    #def obliderate_self():
    



