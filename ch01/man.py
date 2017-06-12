#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#Created 2017-06-12
#
class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("Mike")
m.hello()
m.goodbye()
