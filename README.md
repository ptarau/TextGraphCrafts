# TextGraphCrafts
Python-based summary, keyphrase and relation extractor from text documents using dependency graphs.

HOME: https://github.com/ptarau/TextGraphCrafts

## Project Description

** The system uses dependency links for building Text Graphs, that with help of a centrality algorithm like *PageRank*, extract relevant keyphrases, summaries and relations from text documents.  Developed with *Python 3*, on OS X, but portable to Linux.**


## Dependencies:

- python 3.7 or newer, pip3, java 9.x or newer. Also, having git installed is recommended for easy updates
- ```pip3 install nltk```
-  also, run in python3 something like 


```
import nltk
nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')
```

- or, if that fails on a Mac, use run``` python3 down.py``` 
to collect the desired nltk resource files.
- ```pip3 install networkx```
- ```pip3 install requests```
- ```pip3 install graphviz```, also ensure .gv files can be viewed
- ```pip3 install stanfordnlp``` parser

Tested with the above on a Mac, with macOS Mojave and Catalina and on Ubuntu Linux 18.x.

## Running it:
#### in a shell window, run
 *start_server.sh*
#### in another shell window, start with

```python3 -i deepRank.py```

or by typing 

```python3 -i go.py```

to launch a script doing the same. 

#### interactively, at the ">>>" prompt, try

```
>>> test1()
>>> test2()
>>> ...
>>> test9()
>>> test12()
>>> test0()
```

#### see how to activate other outputs in file 

```deepRank.py```

#### text file inputs (including the US Constitution const.txt) are in the folder

```examples/```

 
### Handling PDF documents

The easiest way to do this is to install *pdftotext*, which is part of [Poppler tools](https://poppler.freedesktop.org/).

If pdftotext is installed, you can place a file like *textrank.pdf*
already in subdirectory pdfs/ and try something similar to:

Change setting in file params.py to use the system with
other global parameter settings.

### Alternative NLP toolkit

*Optionally*, you can activate the alternative Stanford CoreNLP toolkit as follows:

- install [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) and unzip in a derictory of your choice (ag., the local directory)
- edit if needed ```start_parser.sh``` with the location of the parser directory
- edit params.py and set ```corenlp=True```

*Note however that the Stanford CoreNLP is GPL-licensed, which can place restrictions on proprietary software activating this option.*

