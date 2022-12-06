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


    def _copy_item_with(self, item: Item, sell_in: int = None, quality: int = None): 
        copied = copy.copy(item)
        copied.sell_in = sell_in or item.sell_in
        copied.quality = quality or item.quality
        return copied

    def _unchaged_quality(self, item: Item) -> int:
        return item.quality 

    def _reduced_quality_with_age(self, item: Item) -> int:
        return max(MIN_QUALITY, item.quality-1)

    def _increase_quality_with_age(self, item: Item) -> int:
        return min(MAX_QUALITY, item.quality+1)

    def _increase_concert_quality_with_age(self, item: Item) -> int:
        quality = item.quality + 1
        if item.sell_in < 11:
            quality += 1
        if item.sell_in < 6:
            quality += 1
        return min(MAX_QUALITY, quality)

    def _age_an_item(self, item: Item):
        quality_function = {
            'Aged Brie': self._increase_quality_with_age,
            'Backstage passes to a TAFKAL80ETC concert': self._increase_concert_quality_with_age,
            'Sulfuras, Hand of Ragnaros': self._unchaged_quality,
        }.get(item.name, self._reduced_quality_with_age)

        return self._copy_item_with(item, item.sell_in, quality_function(item))

    def update_quality(self):
        self.items = [self._age_an_item(i) for i in self.items]
        for item in self.items:
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

