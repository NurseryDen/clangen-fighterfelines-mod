import random
import os
import ujson

class Traits():
    if os.path.exists('resources/dicts/traits/trait_ranges.json'):
        with open('resources/dicts/traits/trait_ranges.json') as read_file:
            trait_dict = ujson.loads(read_file.read())
