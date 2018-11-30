
from priorityqueue import *
from huffman import *
import unittest

class Asg4(unittest.TestCase):
   def test_priorityqueue_1(self):
      pq = PriorityQueue()
      pq.enqueue('a', 0)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('z', 100)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'z')  
         
   def test_priorityqueue_2(self):
      pq = PriorityQueue()
      pq.enqueue('a', 0)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('z', 100)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZZZ', -10)
      self.assertEqual(pq.front(), 'z')
         
   def test_priorityqueue_3(self):
      pq = PriorityQueue()
      pq.enqueue('a', 0)
      self.assertEqual(pq.front(), 'a')
      pq.enqueue('b', 5)
      self.assertEqual(pq.front(), 'b')
      pq.enqueue('z', 100)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'z')
      pq.enqueue('ZZZZ', 1000)

         
   def test_priorityqueue_4(self):
      pq = PriorityQueue()
      pq.enqueue('ZZ', -1)
      self.assertEqual(pq.front(), 'ZZ')
      pq.enqueue('ZZZZ', 1000)
      self.assertEqual(pq.dequeue(), 'ZZZZ')
         
   def test_priorityqueue_5(self):
      pq = PriorityQueue()
      pq.enqueue(list(), -1)
      self.assertEqual(pq.front(), [])
      pq.enqueue(tuple([1,2,3]), 1000); pq.enqueue('bbc', 1000)
      pq.enqueue(int('78'), 1000000)
      self.assertEqual(pq.dequeue(), 78)    
         
   def test_huffman_1(self):
      sent = 'aaaaggccttt'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  
         
      self.assertDictEqual(codes, {'a': '0', 'g': '111', 'c': '110', 't': '10'})
         
   def test_huffman_2(self):
      sent = 'asdf;k;lkjasdfk dasiirFFDg'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  
         
      self.assertDictEqual(codes, \
                                {'a': '001', 's': '100', 'd': '010', 'f': '1011', \
                                ';': '1101', 'k': '011', 'l': '11100', 'j': \
                                '11111', ' ': '11000', 'i': '000', 'r': '11101',\
                                'F': '1010', 'D': '11001', 'g': '11110'})
         
   def test_huffman_3(self):
      sent = 'asdf;k;lkjasdfk'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)  
         
      self.assertDictEqual(codes, {'a': '100', 's': '011', 'd': '101', \
                                        'f': '010', ';': '111', 'k': '00', \
                                        'l': '1101', 'j': '1100'})  
         
   def test_huffman_4(self):
      sent = 'testing this string'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)
         
      self.assertDictEqual(codes, {'t': '01', 'e': '10110', 's': '111', \
        'i': '110', 'n': '100', 'g': '001', ' ': '000', 'h': '10111', \
                'r': '1010'} )
                                 
   def test_huffman_5(self):
      sent = 'StringTeessttt'; codes = dict(); root = huffman(sent)
      for ch in sent:
         codes[ch] = get_huffman_code(ch, root)
         
      self.assertDictEqual(codes, {'S': '0100', 't': '11', 'r': \
        '1001', 'i': '1011', 'n': '1000', 'g': '1010', 'T': '0101', \
                'e': '011', 's': '00'})
   
if __name__ == '__main__':  
      unittest.main()
