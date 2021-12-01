# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:23:22 2021

@author: Menings
"""

import random
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
# %% sequence functions

def make_sound_slow():
    sound = SoundLoader.load('Relax.wav')
    sound.play()

def make_sound_fast():
    sound = SoundLoader.load('Sprint.wav')
    sound.play()

def start_sequence():
    pass

def finish_sequence():
    pass

def actual_sequence(intervall):
    for count, value in enumerate(intervall):
        if count%2 == 0:
            make_sound_slow()
            time.sleep(value)
        else:
            make_sound_fast()
            time.sleep(value)
    return

  # %%
class FirstWindow(Screen):
    pass


class TimeWindow(Screen):

    mu_rest_t = ObjectProperty(None)
    sigma_rest_t = ObjectProperty(None)
    mu_sprint_t = ObjectProperty(None)
    sigma_sprint_t = ObjectProperty(None)
    totaltime = ObjectProperty(None)

    def start(self):
        interval = []
        while sum(interval) < float(self.totaltime.text):
            interval.append(abs(random.gauss(float(self.mu_rest_t.text),
                                         float(self.sigma_rest_t.text))))
            interval.append(abs(random.gauss(float(self.mu_sprint_t.text),
                                         float(self.sigma_sprint_t.text))))
        print(interval)
        start_sequence()
        actual_sequence(interval)
        finish_sequence()


class CountWindow(Screen):

    mu_rest_c = ObjectProperty(None)
    sigma_rest_c = ObjectProperty(None)
    mu_sprint_c = ObjectProperty(None)
    sigma_sprint_c = ObjectProperty(None)
    count = ObjectProperty(None)

    def start(self):
        interval = []
        for i in range(int(self.count.text)):
            interval.append(abs(random.gauss(float(self.mu_rest_c.text),
                                         float(self.sigma_rest_c.text))))
            interval.append(abs(random.gauss(float(self.mu_sprint_c.text),
                                         float(self.sigma_sprint_c.text))))

        start_sequence()
        actual_sequence(interval)
        finish_sequence()

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()


