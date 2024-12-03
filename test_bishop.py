

import unittest
from main import Piece_Col, Bishop, Pawn, Game

class Bishop_moves(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.g1 = Game(test_mode = True)


    def test_same_fld(self):

        trgt_fld_1 = (0, 0)

        self.g1.board[trgt_fld_1] = Bishop(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)

        self.g1.display_board()

        with self.assertRaises(Exception):
            self.g1.move('8a>8a')

    def test_wrong_fld1(self):

        trgt_fld_1 = (0, 0)

        self.g1.board[trgt_fld_1] = Bishop(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)

        self.g1.display_board()

        with self.assertRaises(Exception):
            self.g1.move('8a>7a')

    def test_simple_move1(self):

        trgt_fld_1 = (0, 0)

        self.g1.board[trgt_fld_1] = Bishop(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)

        self.g1.display_board()

        self.g1.move('8a>1h')
        
        board_snap = self.g1.board_snapshot()

        self.assertEqual('BB', board_snap[7, 7])

    def test_simple_move2(self):

        trgt_fld_1 = (0, 7)

        self.g1.board[trgt_fld_1] = Bishop(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)

        self.g1.display_board()

        self.g1.move('8h>1a')
        
        board_snap = self.g1.board_snapshot()

        self.assertEqual('BB', board_snap[7, 0])

    def test_simple_move3(self):

        trgt_fld_1 = (7, 0)

        self.g1.board[trgt_fld_1] = Bishop(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)

        self.g1.display_board()

        self.g1.move('1a>8h')
        
        board_snap = self.g1.board_snapshot()

        self.assertEqual('BB', board_snap[0, 7])

if __name__ == '__main__':
    unittest.main()