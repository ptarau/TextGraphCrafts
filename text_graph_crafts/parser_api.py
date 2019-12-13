from nltk.parse.corenlp import CoreNLPDependencyParser
import stanfordnlp
import os
import sys
from abc import ABC, abstractmethod
from timeit import timeit as tm


# nlp toolkit plugin - abstract class

class NLP_API(ABC):
    def __init__(self, text):
        self.text = text
        self.triples = None
        self.lemmas = None
        self.words = None
        self.tags=None

    @abstractmethod
    def get_triples(self):
        pass

    @abstractmethod
    def get_lemmas(self):
        pass

    @abstractmethod
    def get_words(self):
        pass

    @abstractmethod
    def get_tags(self):
      pass

    def get_all(self):
        return self.get_triples(), self.get_lemmas(), self.get_words(), self.get_tags()

# subclass using Stanford coreNLP

class CoreNLP_API(NLP_API):
    def __init__(self, text):
        super().__init__(text)

        dparser = CoreNLPDependencyParser(url='http://localhost:9000')

        def parse(text) :
          return dparser.parse_text(text)

        # gss is a list of graph generators with
        # number of elements equal to the number of sentences

        chop = 2 ** 16
        gens = []

        while len(text) > chop:
          head = text[:chop]
          text = text[chop:]
          # ppp((head))
          if head:
            hs = list(parse(head))
            # ppp('PARSED')
            gens.append(hs)
        if gens:
          self.gss = [x for xs in gens for x in xs]
        else:
          self.gss = list(parse(text))


        #self.gss = list(dparser.parse_text(self.text))

        self.get_triples()
        self.get_lemmas()
        self.get_words()
        self.get_tags()

    def get_triples(self):
        if not self.triples:
            self.triples = []
            for gs in self.gss:
                self.triples.append(list(gs.triples()))
        return self.triples

    def _extract_key(gss, key):
        wss = []
        for gs in gss:
            ns = list(gs.nodes.items())
            ws = [None]*(len(ns)-1)
            for k, v in ns:
                #print("WORDDICT",v)
                ws[k-1] = v[key]
            wss.append(ws)
        return wss

    def get_lemmas(self):
        if not self.lemmas:
            self.lemmas = CoreNLP_API._extract_key(self.gss, 'lemma')
        return self.lemmas

    def get_words(self):
        if not self.words:
            self.words = CoreNLP_API._extract_key(self.gss, 'word')
        return self.words

    def get_tags(self):
      if not self.tags:
        self.tags = CoreNLP_API._extract_key(self.gss, 'tag')
      return self.tags

# subclass using  torch-based  stanfordnlp - Apache licensed
class StanTorch_API(NLP_API):

    def start_pipeline():
        mfile = os.getenv("HOME") + \
            '/stanfordnlp_resources/en_ewt_models'
        sout = sys.stdout
        serr = sys.stderr
        f = open(os.devnull, 'w')
        sys.stdout = f
        sys.stderr = f
        # turn output off - too noisy
        if not os.path.exists(mfile):
            stanfordnlp.download('en', confirm_if_exists=True)
        nlp = stanfordnlp.Pipeline()
        sys.stdout = sout
        sys.stderr = serr
        # turn output on again
        return nlp

    nlp = start_pipeline()

    def __init__(self, text):
        super().__init__(text)
        self.doc = self.start_parser(text)

    def get_triples(self):
        if not self.triples:
            tss = []
            for s in self.doc.sentences:
                ts = []
                for dep_edge in s.dependencies:
                    if dep_edge[1]=='root' :
                      continue # compatibility with coreNLP
                    source = (dep_edge[0].text, dep_edge[0].pos)
                    target = (dep_edge[2].text, dep_edge[2].pos)
                    t = (source,  dep_edge[1], target)
                    #print('DEPEDGE', len(dep_edge),t)
                    ts.append(t)
                tss.append(ts)
                self.tuples = tss
        return self.tuples

    def get_words_lemmas_tags(self):
        if not self.lemmas or not self.words:
            wss = []
            lss = []
            pss = []
            for s in self.doc.sentences:
                ws = []
                ls = []
                ps = []
                for w in s.words:
                    ws.append(w.text)
                    ls.append(w.lemma)
                    ps.append(w.xpos)
                wss.append(ws)
                lss.append(ls)
                pss.append(ps)
            self.words = wss
            self.lemmas = lss
            self.tags=pss

    def get_words(self):
        self.get_words_lemmas_tags()
        return self.words

    def get_lemmas(self):
        self.get_words_lemmas_tags()
        return self.lemmas

    def get_tags(self):
        self.get_words_lemmas_tags()
        return self.tags

    def start_parser(self, text):
        sout = sys.stdout
        serr = sys.stderr
        f = open(os.devnull, 'w')
        sys.stdout = f
        sys.stderr = f
        # turn output off - too noisy
        self.dparser = StanTorch_API.nlp(text)
        sys.stdout = sout
        sys.stderr = serr
        # turn output on again
        return self.dparser

def apply_api(api, fname):
    with open(fname, 'r') as f:
        ls = f.readlines()
        text = "".join(ls)
        return api(text).get_all()


def t1():
    print('with coreNLP')
    print('')
    text = 'The happy cat sleeps. The dog just barks today.'
    p = CoreNLP_API(text)
    print(p.get_triples())
    print('')
    print(p.get_lemmas())
    print('')
    print(p.get_words())
    print('')
    print(p.get_triples())
    print('-'*50)
    print('')


def t2():
    print('with stanfordnlp - torch based')
    print('')
    text = 'The happy cat sleeps. The dog just barks today.'
    p = StanTorch_API(text)
    print(p.get_triples())
    print('')
    print(p.get_lemmas())
    print('')
    print(p.get_words())
    print('')
    print(p.get_tags())
    print('')

# benchmark


def bm1(fname):
    api = CoreNLP_API
    (ds, ls, ws) = apply_api(api, fname)
    print('coreNLP', 'sents=', len(ws))


def bm2(fname):
    api = StanTorch_API
    (ds, ls, ws) = apply_api(api, fname)
    print('stanfordnlp', 'sents=', len(ws))


def bm():

    fname = 'examples/const.txt'
    #fname = 'examples/einstein.txt'
    #fname = 'examples/tesla.txt'
    for _ in range(3):
        print(tm(lambda: bm1(fname), number=1))
        print(tm(lambda: bm2(fname), number=1))

# t1()
t2()
# bm()
