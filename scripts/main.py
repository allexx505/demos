# -*- coding: utf-8 -*-
# @Create Time : 2018/8/11 19:58
# @Author  : Alex-tan
# @FileName: main.py

import random


class Creature():
    def __init__(self, name, hp):
        self.hp = hp
        self.name = name

    def attack(self):
        attack_value = random.randint(0, 10)
        return attack_value

    def is_not_dead(self):
        if self.hp <= 0:
            self.hp = 0
            return False
        else:
            return True

    def be_attack(self,value):
        self.hp -= value

    def show_info(self):
        print('{}\'s hp is {}'.format(self.name, self.hp))


def attack_with_enemy():
    player = Creature('player', 100)
    enemy = Creature('enemy', 80)
    a = True
    while player.is_not_dead() and enemy.is_not_dead():
        player.show_info()
        enemy.show_info()
        user_input = input("Attack or Defence(A/D)?")
        if user_input == 'A':
            patt_value = player.attack()
            eatt_value = enemy.attack()
            enemy.be_attack(patt_value)
            player.be_attack(eatt_value)
        elif user_input == 'D':
            eatt_value = enemy.attack()*0.1
            player.be_attack(eatt_value)
    if player.is_not_dead():
        print('You have won, {} hp left'.format(player.hp))
    else:
        print('You lose')


if __name__ == "__main__":
    attack_with_enemy()