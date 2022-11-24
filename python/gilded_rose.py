# -*- coding: utf-8 -*-

# My first attempt at the Gilded Rose.
# The problem appears to be perfect for OO design. 
# So I will try to go that way frirst, even though 
# it is perhaps not the most common among pythonistas.

MIN_QUANTITY = 0
MAX_QUANTITY = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _process_aged_brie(self, item):
        if item.quality > MIN_QUANTITY:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                self._process_aged_brie(item)
            else:
                if item.quality < MAX_QUANTITY:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < MAX_QUANTITY:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < MAX_QUANTITY:
                                item.quality = item.quality + 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > MIN_QUANTITY:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < MAX_QUANTITY:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
