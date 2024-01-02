import math
from datetime import datetime


def distance_to_vector(point, vector_start, vector_end):
    vector_direction = (vector_end[0] - vector_start[0], vector_end[1] - vector_start[1])
    length_direction = math.sqrt(vector_direction[0] ** 2 + vector_direction[1] ** 2)
    distance = vector_direction[1] * (point[0] - vector_start[0]) - vector_direction[0] * (point[1] - vector_start[1])
    return abs(distance) / length_direction


def distance_to_line(point, line_start, line_end):
    # Project point C onto the line AB
    x, y = point
    x1, y1 = line_start
    x2, y2 = line_end

    dot_product = (x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)
    len_line_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2

    t = dot_product / len_line_squared

    # Find the nearest point on the line
    nearest_point_x = x1 + t * (x2 - x1)
    nearest_point_y = y1 + t * (y2 - y1)

    # Calculate haversine distance between C and the nearest point on the line
    distance = haversine_distance((x, y), (nearest_point_x, nearest_point_y))

    return distance
