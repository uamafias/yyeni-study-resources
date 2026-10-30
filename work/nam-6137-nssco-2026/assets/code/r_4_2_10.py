"""VIS-6137-4.2-10 -> ITEM-6137-4.2-032-APP: licensed oblique photograph.

Wikimedia Commons, File:C26 at Gamsberg Pass, Namibia (2014).jpg, by Olga Ernst (own work, 2014-10-18), described as road C26 at Gamsberg Pass, Namibia. CC BY-SA 4.0. Inspected on 30 Oct 2026:
looking down a valley, an unsealed road crosses the foreground and then follows the lower part of the left-hand slope (above a
small gully) through the middle distance towards the valley head; steep, rocky, bush-covered slopes rise on both sides; hills
behind; a few animals are on the road.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo42 import make, licence_record  # noqa: E402

RID = 'VIS-6137-4.2-10'
ITEM = 'ITEM-6137-4.2-032-APP'
LIC = licence_record({
    'source': 'Wikimedia Commons', 'title': 'C26 at Gamsberg Pass, Namibia (2014)', 'creator': 'Olga Ernst',
    'source_url': 'https://commons.wikimedia.org/wiki/File:C26_at_Gamsberg_Pass,_Namibia_(2014).jpg',
    'file_url': 'https://upload.wikimedia.org/wikipedia/commons/2/2c/C26_at_Gamsberg_Pass%2C_Namibia_%282014%29.jpg',
    'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
    'date_taken': '2014-10-18', 'source_description': 'C26 at Gamsberg Pass in Namibia (2014)',
    'commons_sha1': 'a6bbbce24efadbc76d87f36778e253e9a9404877'})
MARKERS = [('1', (480, 358)), ('1', (500, 622)), ('2', (140, 180)), ('2', (870, 330))]
ROWS = [('1', 'The unsealed road winds through the valley: across the foreground, then along the lower part of the left-hand slope, bending with the valley.'), ('2', 'Steep, rocky slopes rise above it on both sides; the road keeps to the lower, gentler parts instead of climbing straight over them.'), ('3', 'The photograph cannot show the exact gradient, the building cost or the full reason the road was placed here.')]


def main():
    return make(RID, ITEM, 'Oblique photograph: road C26 at Gamsberg Pass, Namibia (2014)', LIC, MARKERS, ROWS, 'Relief and the route',
                withholds=['relief-route suggestion', 'limit'],
                solution=['route follows the valley floor / lower slopes (1)', 'steep rocky sides avoided (visible) (1)', 'no exact gradient, cost or full cause (1)'])


if __name__ == '__main__':
    main()
