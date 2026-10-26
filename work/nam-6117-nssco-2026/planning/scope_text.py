"""Ignore syllabus exclusion parentheticals only when embedded in known objective titles."""
import re

def clean_objective_title(text):
 return re.sub(r'\([^()]*(?:not required|will not be set|will not be assessed|no need)[^()]*\)', '', text, flags=re.I)

def scope_view(text,objectives):
 for o in objectives:
  for key in ['syllabus_text','learner_objective']:
   title=o.get(key,'');clean=clean_objective_title(title)
   if title and title!=clean:text=text.replace(title,clean)
 return text
