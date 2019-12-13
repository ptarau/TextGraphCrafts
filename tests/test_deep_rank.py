import os
from text_graph_crafts.deepRank import maybeWord
from text_graph_crafts.params import *
from text_graph_crafts import GraphMaker

# shows wk summaries and sk keywords from file
# extracts highest ranked dk svo relations  and visualizes
# dk highest ranked filtered word to word edges as dot graph
# if svo optional arg is set to True, adns svo links to the graph


def runWithFilter(fileName, wk, sk, dk, vk, filter, show=pics == 'yes'):
    gm = GraphMaker()
    gm.load(fileName)
    dotName = os.path.splitext(fileName)[0]+".gv"
    gm.toDot(dk, filter, svo=True, fname=dotName, show=show)
    return gm


def test0():  # might talke 1-2 minutes
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
    showAllEdges(gm)
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
    showAllEdges(gm)
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
    gm = GraphMaker()
    gm.digest('The cat sits near the cats on the mat.')
    for g in gm.gs:
        for e in g.triples():
            print(e)
    for f, ft, r, t, tt in gm.edges():
        print(f, '->', r, '->', t)
    pr = gm.pagerank()
    for w in pr.items():
        print(w)
    showAllEdges(gm)
    return gm


