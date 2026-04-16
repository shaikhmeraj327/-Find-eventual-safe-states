import unittest

from safe_nodes import Solution, eventual_safe_nodes, eventualSafeNodes


class SafeNodesTests(unittest.TestCase):
    def test_problem_example(self):
        vertices = 5
        edges = [[1, 0], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
        expected = [0, 1, 2, 3, 4]

        self.assertEqual(eventual_safe_nodes(vertices, edges), expected)
        self.assertEqual(eventualSafeNodes(vertices, len(edges), edges), expected)
        self.assertEqual(Solution().eventualSafeNodes(vertices, len(edges), edges), expected)

    def test_cycle_nodes_not_safe(self):
        vertices = 4
        edges = [[0, 1], [1, 2], [2, 1], [2, 3]]
        self.assertEqual(eventual_safe_nodes(vertices, edges), [3])


if __name__ == "__main__":
    unittest.main()
