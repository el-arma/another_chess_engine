

import unittest
from main import Piece_Col, Tower, Pawn, Game

# START:
g1 = Game(test_mode = True)

# BASIC MOVEMENTS:
# must be randomized

trgt_fld_1 = (0, 0)

g1.board[trgt_fld_1] = Tower(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)

g1.display_board()

g1.move('8a>8h')
g1.move('8h>8a')

g1.move('8a>8h')
g1.move('8h>1h')
g1.move('1h>1d')
g1.move('1d>1a')
g1.move('1a>8a')

# OBSTACLES:

print("New test", "*" * 100)

g2 = Game(test_mode = True)


trgt_fld_1 = (4, 4)
trgt_fld_2 = (4, 7)

g2.board[trgt_fld_1] = Tower(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)
g2.board[trgt_fld_2] = Pawn(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)

g2.display_board()
g2.move('4e>4g')
g2.display_board()

# Will error as expected:
# g2.move('4g>4h')

#######################################################################################################################
print("New test", "*" * 100)

g3 = Game(test_mode = True)


trgt_fld_1 = (4, 4)
trgt_fld_2 = (4, 7)
trgt_fld_3 = (0, 7)

g3.board[trgt_fld_1] = Tower(color = Piece_Col.BLACK.value, field_tup = trgt_fld_1)
g3.board[trgt_fld_2] = Pawn(color = Piece_Col.WHITE.value, field_tup = trgt_fld_1)

g3.board[trgt_fld_3] = Tower(color = Piece_Col.WHITE.value, field_tup = trgt_fld_1)

g3.display_board()
g3.move('4e>4h')
g3.move('4h>8h')
g3.move('8h>8a')


#######################################################################################################################
# g1.move('6e>6a')


# class NumbersTest(unittest.TestCase):

#     def __init__(self, methodName: str = "runTest") -> None:
#         super().__init__(methodName)

#         self.cases = load_pickle('scenarios')

#     def test_game(self):

#         for case in self.cases:

#             with self.subTest(case[0]):
#                 self.assertEqual(Main(test_mode = True, test_case = case[1:3]), case[3])



# if __name__ == '__main__':
#     unittest.main()