"""Space human repair-record prose without changing code/math/source records."""
import re

def format_prose(text):
 chunks=re.split(r'(```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|\$[^$\n]*\$)',text)
 for i in range(0,len(chunks),2):
  value=chunks[i]
  value=re.sub(r'(?<=\d)(?=[A-Za-z])',' ',value)
  value=re.sub(r'\b(all|with|after|before|exact|plus|from|and|or|exactly|the|to|coverage|objectives|motion|run|across|each|new|under|source|only|case|part|mark|grade|syllabus|rows|tuple|at|for|one|two|three|four|six|nine|twelve|twenty|now|neutral|Apply|Analyse|not|still|versus|retains|earns|given)(?=\d)',r'\1 ',value,flags=re.I)
  value=value.replace('visualparts','visual parts').replace('atx0','at x=0').replace('23November2026','23 November 2026').replace('December2020','December 2020').replace('November2026','November 2026')
  chunks[i]=value
 return ''.join(chunks)
