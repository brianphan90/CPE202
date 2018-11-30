
from tictactoe import *
import unittest


class TestTicTacToe(unittest.TestCase):	 
   
 	 
   def test_board_eval(self):
      b = Board()
      b[0][0] = X(); b[0][1] = X(); b[0][2] = X()
      b[1][0] = O(); b[1][1] = O()
      b[2][0] = O()
 	 
      # Note: Computer plays X's
      self.assertEqual(b.eval(), 1, 'X wins.') 
   def test_board_eval_2(self):
      b = Board()
      b[0][0] = X(); b[0][1] = O(); b[0][2] = O()
      b[1][0] = X(); b[1][1] = O()
      b[2][0] = X()
 	 
      # Note: Computer plays X's
      self.assertEqual(b.eval(), 1, 'X wins.')  
   def test_board_eval_2(self):
      b = Board()
      b[0][0] = O(); b[0][1] = O(); b[0][2] = X()
      b[1][0] = O(); b[1][1] = X()
      b[2][0] = X()
 	 
      # Note: Computer plays X's
      self.assertEqual(b.eval(), 1, 'X wins.')     
 	 
   def test_board_full(self):
      b = Board()
      b[0][0] = O(); b[0][1] = X(); b[0][2] = O()
      b[1][0] = X(); b[1][1] = X(); b[1][2] = O()
      b[2][0] = O(); b[2][1] = O(); b[2][2] = X()
 	 
      self.assertTrue(b.full(), 'Full board.')
   def test_board_full_2(self):
      b = Board()
      b[0][0] = O(); b[0][1] = X(); b[0][2] = O()
      b[1][0] = O(); b[1][1] = X(); b[1][2] = O()
      b[2][0] = X(); b[2][1] = O(); b[2][2] = X()
 	 
      self.assertTrue(b.full(), 'Full board.')   
   def test_board_full_3(self):
      b = Board()
      b[0][0] = O(); b[0][1] = X(); b[0][2] = O()
      b[1][0] = O(); b[1][1] = O(); b[1][2] = X()
      b[2][0] = X(); b[2][1] = O(); b[2][2] = X()
 	 
      self.assertTrue(b.full(), 'Full board.')    
   
   def test_minimax(self):
      b = Board()
      b[0][0] = X(); b[0][1] = X()
      b[1][0] = O(); b[1][1] = O()
      b[2][0] = O()
          
      self.assertEqual(minimax(Computer, b), 1, 'Board contains a win for X')
   def test_minimax_2(self):
      b = Board()
      b[0][0] = O(); b[0][1] = O()
      b[1][0] = X(); b[1][1] = X()
      b[2][0] = O()
          
      self.assertEqual(minimax(Computer, b), 1, 'Board contains a win for X') 
   def test_minimax_2(self):
      b = Board()
      b[0][0] = O(); b[0][1] = O()
      b[1][0] = O(); b[1][1] = X()
      b[2][0] = X()
          
      self.assertEqual(minimax(Computer, b), 1, 'Board contains a win for X')  
 	 
if __name__ == '__main__':
   unittest.main()
