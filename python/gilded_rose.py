# -*- coding: utf-8 -*-

# This will be an attempt to solve the Gilded Rose problem 
# using principles of functional programming

import copy

MAX_QUALITY = 50
MIN_QUALITY = 0
MIN_SELL_IN = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _age_an_item(self, item: Item): 
        return copy.copy(item)

    def update_quality(self):
        self.items = [self._age_an_item(i) for i in self.items]
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > MIN_QUALITY:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality -= 1
            else:
                if item.quality < MAX_QUALITY:
                    item.quality += + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < MAX_QUALITY:
                                item.quality += 1
                        if item.sell_in < 6:
                            if item.quality < MAX_QUALITY:
                                item.quality += 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            if item.sell_in < MIN_SELL_IN:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > MIN_QUALITY:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality -= 1
                    else:
                        item.quality = MIN_QUALITY
                else:
                    if item.quality < MAX_QUALITY:
                        item.quality += 1

