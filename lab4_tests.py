import data
import lab4
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        # write a second test here
        input = [[],[],[],[1,2,3,"hey",5]]
        result = lab4.first_element(input)
        expected = [1]
        self.assertEqual(expected, result)


    # Part 2
    def test_x_coordinates_1(self):
        input = [data.Point(2,3), data.Point(5,6)]
        result = lab4.x_coordinates(input)
        expected = [2,5]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [data.Point(5,7)]
        result = lab4.x_coordinates(input)
        expected = [5]
        self.assertEqual(expected, result)


    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(5,7), data.Point(-2,9)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(5,7)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input = [data.Point(-5,-7), data.Point(-2,9)]
        result = lab4.are_in_positive_quadrant(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        result = lab4.distance(data.Point(0,0), data.Point(3,4))
        expected = 5
        self.assertEqual(expected, result)

    def test_distance_2(self):
        result = lab4.distance(data.Point(4,3), data.Point(0,0))
        expected = 5
        self.assertEqual(expected, result)

    # Part 5
    def test_manhattan_1(self):
        result = lab4.manhattan_distance((data.Point(1,1)), data.Point(0,0))
        expected = 2
        self.assertEqual(expected, result)

    def test_manhattan_2(self):
        result = lab4.manhattan_distance(data.Point(-2, -3), data.Point(0,0))
        expected = 5
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all_1(self):
        result = lab4.distance_all([data.Point(1,1), data.Point(2,2)])
        expected = [2, 4]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        result = lab4.distance_all([data.Point(-1,-1), data.Point(-2,2)])
        expected = [2, 4]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
