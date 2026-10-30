"""VIS-6137-4.2-09 -> ITEM-6137-4.2-031-INTERP: licensed oblique aerial photograph.

Wikimedia Commons, File:Kreuzung der Hauptstraßen C18 und C15 bei Gochas, Namibia (2017).jpg, by Olga Ernst & Hp.Baumeler (own work, 2017-04-20), described as main roads C18 and C15 crossing at Gochas, Namibia. CC BY-SA 4.0. Inspected on 30 Oct 2026:
buildings are grouped closely along a grid of unsealed streets in the lower left, beside a tarred main road; the town street meets
the tarred road at a junction (lower right); beyond a belt of trees the main road crosses a gravel road; a smaller group of buildings
lies further away; most surrounding land is open bush; the town continues beyond the left edge.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo42 import make, licence_record  # noqa: E402

RID = 'VIS-6137-4.2-09'
ITEM = 'ITEM-6137-4.2-031-INTERP'
LIC = licence_record({
    'source': 'Wikimedia Commons', 'title': 'Kreuzung der Hauptstraßen C18 und C15 bei Gochas, Namibia (2017)', 'creator': 'Olga Ernst & Hp.Baumeler',
    'source_url': 'https://commons.wikimedia.org/wiki/File:Kreuzung_der_Hauptstra%C3%9Fen_C18_und_C15_bei_Gochas,_Namibia_(2017).jpg',
    'file_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c0/Kreuzung_der_Hauptstra%C3%9Fen_C18_und_C15_bei_Gochas%2C_Namibia_%282017%29.jpg',
    'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
    'date_taken': '2017-04-20', 'source_description': 'Main roads C18 and C15 crossing at Gochas in Namibia (2017)',
    'commons_sha1': '35331c277fc1975e0f2755ec78b575034740efd3'})
MARKERS = [('1', (220, 520)), ('2', (800, 470)), ('2', (660, 290)), ('3', (900, 389)), ('4', (60, 620))]
ROWS = [('1', 'Buildings are grouped closely along a grid of streets in the lower left: a nucleated cluster within this frame.'), ('2', 'The cluster lies beside the tarred main road, where the town street joins it; farther back, beyond the belt of trees, the main road crosses another road.'), ('3', 'Open bush surrounds the cluster, with a smaller group of buildings further away.'), ('4', 'The settlement continues past the left edge, so this is part of one place, not the pattern of a whole region.')]


def main():
    return make(RID, ITEM, 'Oblique aerial photograph: Gochas, Namibia (2017)', LIC, MARKERS, ROWS, 'Settlement arrangement and routes',
                withholds=['pattern label', 'route relationship'],
                solution=['buildings clustered (nucleated) in the frame (1)', 'cluster beside the main road where the town street joins it, near a road crossing (1)', 'partial frame: local, not regional pattern (1)'])


if __name__ == '__main__':
    main()
