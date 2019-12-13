from text_graph_crafts import *

def go() :
  gm=deepRank.GraphMaker(text='The cat sits on the mat.')
  print(gm.triples())
  print(gm.lemmas())
  print(gm.words())
  print(gm.tags())

# interactive read, parse, show labeled edges loop
def test1():
    gm= deepRank.GraphMaker(text='The cat walks. The dog barks.')
    for g in gm.gs:
      print(g)
    for f, ft, r, t, tt in gm.edges():
      # ppp('!!!!!!',f,ft,r,t,tt)
      print(f, '->', r, '->', t)
    pr = gm.pagerank()
    for w in pr.items(): print(w)
    #showAllEdges(gm)

test1()
