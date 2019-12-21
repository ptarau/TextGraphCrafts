###### parameters #######
import math

# Graph building, parsing ranking

abstractive='no'
pics='no'

corenlp=True

# for LINKS, RANKING, SUMMARIES AND KEYPHRASES

# sets link addition parameters
all_recs  = True  # sentence recommendatations
giant_comp = False # only extract from giant comp
noun_defs = True
noun_self = False

# formula for adjusting rank of long or short sentences
def adjust_rank(rank,length,avg) :
   #adjust = 1 + math.sqrt(1 + abs(length - avg))
   adjust = 1 + math.log(1+abs(length-avg))
   newr=rank/adjust
   #print('ADJUST',adjust,length,avg)
   return newr
