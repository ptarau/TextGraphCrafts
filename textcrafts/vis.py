from graphviz import Digraph as DotGraph
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def showGraph(dot, show=True, file_name='textgraph.gv'):
  dot.render(file_name, view=show)

'''
def gshow0(g, file_name='textgraph.gv', show=True):
  dot = DotGraph()
  for e in g.edges():
    f, t = e
    # w = g[f][t]['weight']
    w = ''
    dot.edge(str(f), str(t), label=str(w))
  dot.render(file_name, view=show)
'''

def show_ranks(rank_dict,file_name="cloud.pdf",show=True) :
  if not show : return
  cloud=WordCloud(width=800,height=400)
  cloud.fit_words(rank_dict)
  f=plt.figure()
  plt.imshow(cloud, interpolation='bilinear')
  plt.axis("off")
  # plt.show()
  '''
  if exists_file(file_name) :
    for i in range(6):
      fname = file_name.replace("quest_cloud","quest_cloud"+str(i))
      if not exists_file(fname) :
        file_name=fname
        break
  '''
  f.savefig(file_name,bbox_inches='tight')

if __name__=="__main__":
  d = {'a': 0.1, 'b': 0.2, 'c': 0.33, 'd': 0.2}
  show_ranks(d)
