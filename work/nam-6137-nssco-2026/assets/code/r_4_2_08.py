"""VIS-6137-4.2-08 -> ITEM-6137-4.2-030-APP: licensed horizontal photograph.

Wikimedia Commons, File:Karas (2006) 17.jpg, by LBM1948 (own work, 2006-04-11), described as a semi-desert plain north of Keetmanshoop, Karas, Namibia. CC BY-SA 4.0. Inspected on 30 Oct 2026:
a flat plain of stony, mostly bare ground with low cushion shrubs and pale grass tufts widely spaced, continuing to a flat horizon
under scattered cumulus. The colours appear strongly saturated in the original.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo42 import make, licence_record  # noqa: E402

RID = 'VIS-6137-4.2-08'
ITEM = 'ITEM-6137-4.2-030-APP'
LIC = licence_record({
    'source': 'Wikimedia Commons', 'title': 'Karas (2006) 17', 'creator': 'LBM1948',
    'source_url': 'https://commons.wikimedia.org/wiki/File:Karas_(2006)_17.jpg',
    'file_url': 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Karas_%282006%29_17.jpg',
    'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
    'date_taken': '2006-04-11', 'source_description': 'Semi-desert plain north of Keetmanshoop, Karas, Namibia',
    'commons_sha1': 'd21d29c628c312d8cb85927ec20d25a8072e7a89'})
MARKERS = [('1', (400, 440)), ('2', (620, 560)), ('3', (760, 300))]
ROWS = [('1', 'Low shrubs and pale grass tufts stand well apart from one another.'), ('2', 'Much stony bare ground shows between the plants: the cover is sparse, which is consistent with vegetation limited by water.'), ('3', 'The same sparse cover continues to the horizon. One photograph (April 2006) cannot establish annual rainfall or rule out season, grazing or other disturbance.')]


def main():
    return make(RID, ITEM, 'Horizontal photograph of a plain north of Keetmanshoop, Namibia', LIC, MARKERS, ROWS, 'A cautious interpretation',
                withholds=['interpretation', 'reason and limitation'],
                solution=['sparse, water-limited vegetation suggested (1)', 'widely spaced shrubs and tufts with bare stony ground (1)', 'one image/date: no rainfall total; season or grazing possible (1)'])


if __name__ == '__main__':
    main()
