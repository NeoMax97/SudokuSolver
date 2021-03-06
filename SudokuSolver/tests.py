import unittest
from main import Sudoku as S


class SudokuTester(unittest.TestCase):

    # Set up variables for tests
    def setUp(self):
        # Single Sudoku Boards
        self.board0 = S.parse(S, "....8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3")
        self.solved = S.parse(S, "417895632328764951569213784782349516145628397936157428891436275254971863673582149")
        self.almost_1 = S.parse(S, ".17895632328764951569213784782349516145628397936157428891436275254971863673582149")
        self.almost_2 = S.parse(S, ".1789563232876495156921378478234951614562839793615742889143627525497186367358214.")
        self.hardest = S.parse(S, "...8.5.3..28.6..5.5.9.13..4..23.951.145.2.3.79.6..74..8.14...7.2.49.1.6..735..1.9")
        # list of random Sudoku Boards
        self.easyBoardStringList = [
              "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..",
              "2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3",
              ".3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....98..1.2.6...8..6..2.",
              ".2.81.74.7....31...9...28.5..9.4..874..2.8..316..3.2..3.27...6...56....8.76.51.9.",
              ".43.8.25.6.............1.949....4.7....6.8....1.2....382.5.............5.34.9.71.",
              "48...69.2..2..8..19..37..6.84..1.2....37.41....1.6..49.2..85..77..9..6..6.92...18",
              "...1254....84.....42.8......3.....95.6.9.2.1.51.....6......3.49.....72....1298...",
              ".6234.75.1....56..57.....4.....948..4.......6..583.....3.....91..64....7.59.8326.",
              "3..........5..9...2..5.4....2....7..16.....587.431.6.....89.1......67.8......5437",
              "....2..4...8.35.......7.6.2.31.4697.2...........5.12.3.49...73........1.8....4...",
              "361.259...8.96..1.4......57..8...471...6.3...259...8..74......5.2..18.6...547.329",
              ".5.8.7.2.6...1..9.7.254...6.7..2.3.15.4...9.81.3.8..7.9...762.5.6..9...3.8.1.3.4.",
              ".8...5........3457....7.8.9.6.4..9.3..7.1.5..4.8..7.2.9.1.2....8423........1...8.",
              "..35.29......4....1.6...3.59..251..8.7.4.8.3.8..763..13.8...1.4....2......51.48..",
              "...........98.51...519.742.29.4.1.65.........14.5.8.93.267.958...51.36...........",
              ".2..3..9....9.7...9..2.8..5..48.65..6.7...2.8..31.29..8..6.5..7...3.9....3..2..5.",
              "..5.....6.7...9.2....5..1.78.415.......8.3.......928.59.7..6....3.4...1.2.....6..",
              ".4.....5...19436....9...3..6...5...21.3...5.68...2...7..5...2....24367...3.....4.",
              "..4..........3...239.7...8.4....9..12.98.13.76..2....8.1...8.539...4..........8..",
              "..72564..4.......5.1..3..6....5.8.....8.6.2.....1.7....3..7..9.2.......4..63127..",
              "..........79.5.18.8.......7..73.68..45.7.8.96..35.27..7.......5.16.3.42..........",
              ".3.....8...9...5....75.92..7..1.5..8.2..9..3.9..4.2..1..42.71....2...8...7.....9.",
              "2..17.6.3.5....1.......6.79....4.7.....8.1.....9.5....31.4.......5....6.9.6.37..2",
              ".......8.8..7.1.4..4..2..3.374...9......3......5...321.1..6..5..5.8.2..6.8.......",
              "6.8.7.5.2.5.6.8.7...2...3..5...9...6.4.3.2.5.8...5...3..5...2...1.7.4.9.4.9.6.7.1",
              ".5..1..4.1.7...6.2...9.5...2.8.3.5.1.4..7..2.9.1.8.4.6...4.1...3.4...7.9.2..6..1.",
              ".53...79...97534..1.......2.9..8..1....9.7....8..3..7.5.......3..76412...61...94.",
              "..6.8.3...49.7.25....4.5...6..317..4..7...8..1..826..9...7.2....75.4.19...3.9.6..",
              "..5.8.7..7..2.4..532.....84.6.1.5.4...8...5...7.8.3.1.45.....916..5.8..7..3.1.6..",
              "...9..8..128..64...7.8...6.8..43...75.......96...79..8.9...4.1...36..284..1..7...",
              "....8....27.....54.95...81...98.64...2.4.3.6...69.51...17...62.46.....38....9....",
              "...6.2...4...5...1.85.1.62..382.671...........194.735..26.4.53.9...2...7...8.9...",
              "38..........4..785..9.2.3...6..9....8..3.2..9....4..7...1.7.5..495..6..........92",
              "...158.....2.6.8...3.....4..27.3.51...........46.8.79..5.....8...4.7.1.....325..."
              ]

    # Peers tests
    def test_peers(self):
        # Top Right
        self.assertEqual(S.peers(S, 0, 0), [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                                            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                                            (1, 1), (1, 2), (2, 1), (2, 2)
                                            ])
        # Middle
        self.assertEqual(S.peers(S, 4, 4), [(0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                                            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
                                            (3, 3), (3, 5), (5, 3), (5, 5)
                                            ])
        # Bottom Right
        self.assertEqual(S.peers(S, 8, 8), [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8),
                                            (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7),
                                            (6, 6), (6, 7), (7, 6), (7, 7)
                                            ])

    # valueAt Tests
    def test_valueAt(self):
        self.assertEqual(self.board0.valueAt(0, 4), 8)
        self.assertEqual(self.board0.valueAt(0, 0), 0)  # No value assigned yet

    # isSolved tests
    def test_isSolved(self):
        self.assertTrue(self.solved.isSolved())
        self.assertFalse(self.board0.isSolved())

    # place tests
    def test_place(self):
        after = S.parse(S, "1...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3")
        self.assertEqual(self.board0.place(0, 0, 1).avail, after.avail)

    # nextStates tests
    def test_nextStates(self):
        after_1 = self.almost_1.place(0, 0, 4).avail
        self.assertEqual(self.almost_1.nextStates()[0].avail, after_1)
        # If there is only one value left, that value is also added, since there is no other move possible
        # Therefore, the two nextStates will return the final board
        after_2 = self.almost_2.place(0, 0, 4).place(8, 8, 9).avail
        self.assertEqual(self.almost_2.nextStates()[0].avail, after_2)

    # solve Tests
    def test_solve(self):
        self.assertTrue(self.board0.solve().isSolved())
        self.assertTrue(self.almost_1.solve().isSolved())
        self.assertTrue(self.almost_2.solve().isSolved())
        # solve every board in easyBoardStringList
        self.assertTrue(self.hardest.solve().isSolved())
        for board in self.makeBoards():
            self.assertTrue(board.solve().isSolved())

    # Helper Function: Makes boards from a list of strings
    def makeBoards(self):
        res = list()
        for s in self.easyBoardStringList:
            res.append(S.parse(S, s))
        return res


if __name__ == '__main__':
    unittest.main()
