import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep_time(seconds):
    time.sleep(seconds)