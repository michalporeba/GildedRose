# -*- coding: utf-8 -*-

# My first attempt at the Gilded Rose.
# The problem appears to be perfect for OO design. 
# So I will try to go that way frirst, even though 
# it is perhaps not the most common among pythonistas.

MIN_QUANTITY = 0
MAX_QUANTITY = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = [self._decorate_item(item) for item in items]

    def _decorate_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
        return ItemWrap(item)

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > MIN_QUANTITY:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
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

            item.next_day()

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

# Since I cannot change the Item class I will try to use the decorator pattern

class ItemWrap(Item):
    _item: Item = None 

    def __init__(self, item):
        self._item = item 

    def __repr__(self):
        return super().__repr__()

    def _adjust_sell_in(self):
        self._item.sell_in -= 1

    def _adjust_quality(self):
        pass 

    def next_day(self):
        self._adjust_sell_in()    
        self._adjust_quality()

    @property
    def name(self):
        return self._item.name

    @property 
    def sell_in(self):
        return self._item.sell_in 

    @property 
    def quality(self):
        return self._item.quality 

    @quality.setter 
    def quality(self, value):
        self._item.quality = value 

class Sulfuras(ItemWrap):
    def __init__(self, item):
        super().__init__(item) 

    def next_day(self):
        pass