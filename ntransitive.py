#!/Users/oleks/anaconda3/bin/python

import sys
import getopt
from timer import timeit

import solutions.simple as simple
import solutions.partial_order as partord

@timeit
def print_ntransitive(size, method):
   ntransitive = method.number_of_transitive_relations(size)
   print('Number of transitive relations on {}-element set: {}'\
      .format(size, ntransitive))

def main(argv):
   try:
      opts, args = getopt.getopt(argv, "s:", ["size="])

      if len(opts) != 1:
         raise getopt.GetoptError(None)

      for opt, arg in opts:
         if opt in ['-s', '--size']:
            size = int(arg)
            print_ntransitive(size, method=partord)

         else:
            raise getopt.GetoptError(None)

   except getopt.GetoptError:
      print('usage: ntransitive.py -s <size>')
      print('usage: ntransitive.py --size <size>')
      sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])