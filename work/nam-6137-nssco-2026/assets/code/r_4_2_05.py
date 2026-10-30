"""VIS-6137-4.2-05 -> ITEM-6137-4.2-027-INTERP: licensed horizontal photograph of a coast.

Wikimedia Commons, File:Pebble Beach with Rock Cliff.jpg, by Daredeep33 (own work, 2019-03-22), described
as a pebble beach and sedimentary rock formations near Fins, Oman. CC BY-SA 4.0. Inspected on 30 Oct 2026:
a pebble beach fills the foreground; a steep, jointed, layered rock outcrop (a low cliff) with fallen blocks
rises on the left; calm sea fills the right and middle distance, with a detached rock just offshore.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo42 import make, licence_record  # noqa: E402

RID = 'VIS-6137-4.2-05'
ITEM = 'ITEM-6137-4.2-027-INTERP'
LIC = licence_record({
    'source': 'Wikimedia Commons', 'title': 'Pebble Beach with Rock Cliff', 'creator': 'Daredeep33',
    'source_url': 'https://commons.wikimedia.org/wiki/File:Pebble_Beach_with_Rock_Cliff.jpg',
    'file_url': 'https://upload.wikimedia.org/wikipedia/commons/7/77/Pebble_Beach_with_Rock_Cliff.jpg',
    'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
    'date_taken': '2019-03-22', 'source_description': 'Pebble beach and sedimentary rock formations near Fins, Oman.',
    'commons_sha1': '4ca5217191670b44c08fbca896e4977c17c9d855'})
MARKERS = [('1', (500, 690)), ('2', (180, 400)), ('3', (760, 560))]
ROWS = [('1', 'Foreground (bottom of the image): a beach of small rounded pebbles (shingle).'),
        ('2', 'Left, middle distance: a steep outcrop of jointed, layered rock (a low cliff), with fallen blocks at its foot.'),
        ('3', 'Right and middle distance: calm sea, with a detached rock just offshore; the horizon lies behind.')]


def main():
    return make(RID, ITEM, 'Horizontal photograph of a coast', LIC, MARKERS, ROWS, 'Visible physical features',
                withholds=['feature names and positions'],
                solution=['pebble beach in the foreground (1)', 'rock outcrop / low cliff on the left (1)', 'sea on the right with a detached rock offshore (1)'])


if __name__ == '__main__':
    main()
