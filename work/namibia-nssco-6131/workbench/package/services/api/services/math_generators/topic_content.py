"""Remaining-topic presentation registry; no drawing or Recall grading changes."""
from . import (topic_text_content,topic_measures_content,topic_sets_graphs_content,
               topic_coordinate_content,topic_geometry_content,
               topic_vectors_matrices_content,topic_trigonometry_content,
               topic_statistics_content)

MODULES=(topic_text_content,topic_measures_content,topic_sets_graphs_content,
         topic_coordinate_content,topic_geometry_content,topic_vectors_matrices_content,
         topic_trigonometry_content,topic_statistics_content)
BUILDERS={gid:module.content for module in MODULES for gid in module.LABELS}
LEVEL_LABELS={gid:labels for module in MODULES for gid,labels in module.LABELS.items()}


def topic_content(problem):
    builder=BUILDERS.get(problem.generator_id)
    return builder(problem) if builder else None
