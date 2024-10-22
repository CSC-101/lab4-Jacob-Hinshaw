import data

# Write your functions for each part in the space below.

# Part 1
def first_element(nestedlist:list[list[int]]) -> list[int]:
    filtered_list = [list for list in nestedlist if list]
    first_elements = [list[0] for list in filtered_list]
    return first_elements

# Part 2
def x_coordinates(parameter:list[data.Point]) -> list[float]:
    return [Point.x for Point in parameter]

# Part 3
def are_in_positive_quadrant(parameter:list[data.Point]) -> list[data.Point]:
    return [Point for Point in parameter if Point.x > 0 and Point.y > 0]

# Part 4
def distance(point1:data.Point, point2:data.Point) -> float:
    x_distance = point1.x - point2.x
    y_distance = point1.y - point2.y
    return (x_distance ** 2 + y_distance ** 2) ** (1 / 2)

# Part 5
def manhattan_distance(point1:data.Point, point2:data.Point) -> float:
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)
# Part 6
def distance_all(points:list[data.Point]) -> list[float]:
    return [abs(point.x) + abs(point.y) for point in points]

