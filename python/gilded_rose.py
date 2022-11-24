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
        elif item.name == "Aged Brie":
            return AgedBrie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstageTicket(item)
        return ItemWrap(item)

    def update_quality(self):
        for item in self.items:
            item.next_day()
                   

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemWrap(Item):
    _item: Item = None 

    def __init__(self, item):
        self._item = item 

    def __repr__(self):
        return super().__repr__()

    def _adjust_sell_in(self):
        self._item.sell_in -= 1

    def _adjust_quality(self):
        self.decrease_quality()
        if self._item.sell_in < 0:
            self.decrease_quality()

    def next_day(self):
        self._adjust_sell_in()    
        self._adjust_quality()

    def decrease_quality(self):
        if self._item.quality > MIN_QUANTITY:
            self._item.quality -= 1

    def increase_quality(self):
        if self._item.quality < MAX_QUANTITY:
            self._item.quality += 1


class AgedBrie(ItemWrap):
    def __init__(self, item):
        super().__init__(item) 

    def _adjust_quality(self):
        self.increase_quality()
        if self._item.sell_in < 0:
            self.increase_quality()


class BackstageTicket(ItemWrap):
    def __init__(self, item):
        super().__init__(item) 

    def _adjust_quality(self):
        self.increase_quality()
        if self._item.sell_in < 10:
            self.increase_quality()
        if self._item.sell_in < 5:
            self.increase_quality()
        if self._item.sell_in < 0: 
            self._item.quality = 0


class Sulfuras(ItemWrap):
    def __init__(self, item):
        super().__init__(item) 

    def _adjust_sell_in(self):
        pass

    def _adjust_quality(self):
        pass 
    