import math
from datetime import datetime


def distance_to_vector(point, vector_start, vector_end):
    vector_direction = (vector_end[0] - vector_start[0], vector_end[1] - vector_start[1])
    length_direction = math.sqrt(vector_direction[0] ** 2 + vector_direction[1] ** 2)
    distance = vector_direction[1] * (point[0] - vector_start[0]) - vector_direction[0] * (point[1] - vector_start[1])
    return abs(distance) / length_direction
