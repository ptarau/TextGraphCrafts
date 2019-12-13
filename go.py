from text_graph_crafts import *

def go() :
  gm=deepRank.GraphMaker(text='The cat sits on the mat.')
  print(gm.triples())
  print(gm.lemmas())
  print(gm.words())
  print(gm.tags())


# interactive read, parse, show labeled edges loop
def testx():
    gm= deepRank.GraphMaker(text='The cat walks. The dog barks.')
    for g in gm.gs:
      print(g)
    for f, ft, r, t, tt in gm.edges():
      # ppp('!!!!!!',f,ft,r,t,tt)
      print(f, '->', r, '->', t)
    pr = gm.pagerank()
    for w in pr.items(): print(w)
    #showAllEdges(gm)

wk,sk=6,6

def test1() :
  deepRank.runWithFilter('examples/bfr.txt',wk,sk,30,50,deepRank.maybeWord)


def test0():  # might talke 1-2 minutes
  deepRank.runWithFilter('examples/tesla.txt', wk, sk, 30, 50, deepRank.maybeWord)


def test1():
  deepRank.runWithFilter('examples/bfr.txt', wk, sk, 30, 50, deepRank.maybeWord)


def test2():
  wk, sk = 3, 3
  deepRank.runWithFilter('examples/hindenburg.txt', wk, sk, 20, 50, deepRank.maybeWord)


def test3():
  deepRank.runWithFilter('examples/const.txt', wk, sk, 20, 50, deepRank.maybeWord)


def test4():
  gm = deepRank.runWithFilter('examples/summary.txt', 12, 3, 30, 50, deepRank.maybeWord)



def test5():
  deepRank.runWithFilter('examples/heaven.txt', wk, sk, 30, 50, deepRank.maybeWord)


def test6():
  deepRank.runWithFilter('examples/einstein.txt', wk, sk, 30, 50, deepRank.maybeWord)


def test7():
  deepRank.runWithFilter('examples/kafka.txt', wk, sk, 20, 50, deepRank.maybeWord)


def test8():
  gm = deepRank.runWithFilter('examples/test.txt', wk, sk, 20, 50, deepRank.isAny, show=False)


def test9():
  deepRank.runWithFilter('examples/relativity.txt', wk, sk, 20, 50, deepRank.maybeWord)


def test10():
  deepRank.runWithFilter('examples/cats.txt', wk, sk, 20, 50, deepRank.maybeWord)


def test11():
  deepRank.runWithFilter('examples/wasteland.txt', wk, sk, 20, 50, deepRank.maybeWord)


def test12():
  fname = "pdfs/textrank"
  deepRank.pdf2txt(fname + ".pdf")
  deepRank.runWithFilter(fname + ".txt", wk, sk, 20, 50, deepRank.maybeWord)

def go() :
  #test0()
  test1()
  test2()
  test3()
  test4()
  test5()
  test6()
  test7()
  test8()
  #test9()
  test10()
  test11()
  test12()

if __name__ == '__main__'  :
  go()
  #test10()
