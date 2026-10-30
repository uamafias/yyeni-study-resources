"""VIS-6137-4.2-06 -> ITEM-6137-4.2-028-APP: licensed oblique aerial photograph.

Wikimedia Commons, File:Early Farming season.jpg, by Aminucrus (own work, 2025-02-05) (the source gives no location). CC BY-SA 4.0. Inspected on 30 Oct 2026:
many small plots bounded by low banks fill the foreground and middle distance; an unsealed track runs up through them from the
bottom centre; some plots hold water or green growth, most are bare; winding watercourses and a hazy plain lie beyond.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo42 import make, licence_record  # noqa: E402

RID = 'VIS-6137-4.2-06'
ITEM = 'ITEM-6137-4.2-028-APP'
LIC = licence_record({
    'source': 'Wikimedia Commons', 'title': 'Early Farming season', 'creator': 'Aminucrus',
    'source_url': 'https://commons.wikimedia.org/wiki/File:Early_Farming_season.jpg',
    'file_url': 'https://upload.wikimedia.org/wikipedia/commons/9/94/Early_Farming_season.jpg',
    'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
    'date_taken': '2025-02-05', 'source_description': 'Farmlands from above give a patterned and structured landscape with various shapes, sizes and colours.',
    'commons_sha1': '146e7c93d5768773a05e89b8bcfc0501c5f70f2b'})
MARKERS = [('1', (170, 560)), ('2', (548, 470)), ('3', (830, 450))]
ROWS = [('1', 'Many small plots separated by low banks fill the foreground and middle distance: evidence that the land is cultivated (agriculture).'), ('2', 'An unsealed track runs up through the plots from the bottom of the image, giving access to them.'), ('3', 'Some plots hold water or green growth. The image cannot show the crop, whether the water is irrigation or rain, or whether the farming is commercial.')]


def main():
    return make(RID, ITEM, 'Oblique aerial photograph', LIC, MARKERS, ROWS, 'Land use: evidence and limit',
                withholds=['land-use label', 'evidence and limit'],
                solution=['agriculture / cultivation (1)', 'bounded plots with growth or water, reached by a track (1)', 'crop, water source and purpose not established (1)'])


if __name__ == '__main__':
    main()
