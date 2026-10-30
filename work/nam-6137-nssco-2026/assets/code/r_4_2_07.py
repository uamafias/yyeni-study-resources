"""VIS-6137-4.2-07 -> ITEM-6137-4.2-029-INTERP: licensed horizontal photograph.

Wikimedia Commons, File:Fish-River-Namibia-anagoria.JPG, by Anagoria (own work, 2011-02-07), described as the Fish River, Namibia. CC BY 3.0. Inspected on 30 Oct 2026:
a wide, muddy channel with sandbars and bushy islands fills the foreground; a belt of green trees and shrubs lines the
banks in the middle distance; a steep slope of layered red rock rises behind on the right, with lower flat-topped land on the left.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo42 import make, licence_record  # noqa: E402

RID = 'VIS-6137-4.2-07'
ITEM = 'ITEM-6137-4.2-029-INTERP'
LIC = licence_record({
    'source': 'Wikimedia Commons', 'title': 'Fish River, Namibia', 'creator': 'Anagoria',
    'source_url': 'https://commons.wikimedia.org/wiki/File:Fish-River-Namibia-anagoria.JPG',
    'file_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c6/Fish-River-Namibia-anagoria.JPG',
    'licence': 'CC BY 3.0', 'licence_url': 'https://creativecommons.org/licenses/by/3.0/',
    'date_taken': '2011-02-07', 'source_description': 'Fish River, Namibia',
    'commons_sha1': '12c72b63e2a76482d68af4792b4ee89208a67aac'})
MARKERS = [('1', (470, 420)), ('2', (480, 200)), ('3', (760, 140))]
ROWS = [('1', 'Foreground: a wide channel of muddy water with sandbars and bushy islands.'), ('2', 'Middle distance: a belt of green trees and shrubs along the banks.'), ('3', 'Background: a steep valley side of layered red rock rising on the right, with lower flat-topped land on the left.')]


def main():
    return make(RID, ITEM, 'Horizontal photograph of a river valley (Fish River, Namibia)', LIC, MARKERS, ROWS, 'Visible valley features',
                withholds=['feature names and positions'],
                solution=['channel with water and sandbars in the foreground (1)', 'bank vegetation in the middle distance (1)', 'steep layered valley side in the background (1)'])


if __name__ == '__main__':
    main()
