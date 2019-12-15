import os
from text_graph_crafts.deepRank import maybeWord, isAny, pdf2txt
from text_graph_crafts import GraphMaker
from text_graph_crafts.params import *

def go() :
  gm = GraphMaker(text='The cat sits on the mat.')
  print(gm.triples())
  print(gm.lemmas())
  print(gm.words())
  print(gm.tags())


# interactive read, parse, show labeled edges loop
def testx():
    gm= GraphMaker(text='The cat walks. The dog barks.')
    for g in gm.gs:
      print(g)
    for f, ft, r, t, tt in gm.edges():
      print(f, '->', r, '->', t)
    pr = gm.pagerank()
    for w in pr.items(): print(w)


def runWithFilter(fileName, wk, sk, dk, vk, filter, show=True):
    gm = GraphMaker(file_name=fileName)
    dotName = os.path.splitext(fileName)[0]+".gv"
    gm.toDot(dk, filter, svo=True, fname=dotName, show=show)
    return gm


def test0():  # might take 1-2 minutes
    gm = runWithFilter('../examples/tesla.txt', wk, sk, 30, 50, maybeWord)
    return gm


def test1():
    gm = runWithFilter('../examples/bfr.txt', wk, sk, 30, 50, maybeWord)
    return gm


def test2():
    wk, sk = 3, 3
    gm = runWithFilter('../examples/hindenburg.txt', wk, sk, 20, 50, maybeWord)
    return gm


def test3():
    gm = runWithFilter('../examples/const.txt', wk, sk, 20, 50, maybeWord)
    return gm


def test4():
    gm = gm = runWithFilter('../examples/summary.txt', 12, 3, 30, 50, maybeWord)
    return gm


def test5():
    gm = runWithFilter('../examples/heaven.txt', wk, sk, 30, 50, maybeWord)
    return gm


def test6():
    gm = runWithFilter('../examples/einstein.txt', wk, sk, 30, 50, maybeWord)
    return gm


def test7():
    gm = runWithFilter('../examples/kafka.txt', wk, sk, 20, 50, maybeWord)
    return gm


def test8():
    gm = runWithFilter('../examples/test.txt', wk,
                       sk, 20, 50, isAny, show=False)
    return gm


def test9():
    gm = runWithFilter('../examples/relativity.txt', wk, sk, 20, 50, maybeWord)
    return gm


def test10():
    gm = runWithFilter('../examples/cats.txt', wk, sk, 20, 50, maybeWord)
    return gm


def test11():
    gm = runWithFilter('../examples/wasteland.txt', wk, sk, 20, 50, maybeWord)
    return gm


def test12():
    fname = "../pdfs/textrank"
    pdf2txt(fname+".pdf")
    gm = runWithFilter(fname+".txt", wk, sk, 20, 50, maybeWord)
    return gm


def testx():
    gm = GraphMaker(text='The cat sits. The dog barks.')
    for e in gm.triples():
            print(e)
    for f, ft, r, t, tt in gm.edges():
        print(f, '->', r, '->', t)
    pr = gm.pagerank()
    for w in pr.items():
        print(w)
    return gm
