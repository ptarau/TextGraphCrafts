from text_graph_crafts import DialogAgent


def chat(fname):
    DialogAgent().chat_about("examples/"+fname+".txt")


def dialog_about(fname, query=None):
    DialogAgent().chat_about(fname+".txt", question=query)


def ranked_txt_quest(Folder, FNameNoSuf, QuestFileNoSuf):
    Q = []
    qfname = Folder + "/" + QuestFileNoSuf + ".txt"
    qs = list(ev.file2seq(qfname))
    print('qs', qs)
    dialog_about(Folder+"/"+FNameNoSuf, qs)


def test_00():
    dialog_about('examples/tesla',
                 "How I have a flat tire repaired?")


def test_00a():
    dialog_about('examples/tesla',
                 "How I have a flat tire repaired?  \
             Do I have Autopilot enabled? \
             How I navigate to work? Should I check tire pressures?")


def test_00b():
    ranked_txt_quest('examples', 'tesla', 'quests')


def test_01():
    dialog_about('../examples/bfr',
                 "What space vehicles SpaceX develops?")


def test_02():
    # dialog_about('examples/bfr')
    dialog_about('examples/hindenburg',
                 "How did the  fire start on the Hindenburg?")


def test_03():
    dialog_about('examples/const',
                 # "How many votes are needed for the impeachment of a President?"
                 'How can a President be removed from office?'
                 )


def test_04():
    dialog_about('examples/summary',
                 "How we obtain summaries and keywords from dependency graphs?")


def test_05():
    dialog_about('examples/heaven',
                 "What does the Pope think about heaven?")


def test_06():
    dialog_about('examples/einstein',
                 "What does quantum theory tell us about our \
              description of reality for an observer?")


def test_07():
    dialog_about('examples/kafka',
                 # "What does the doorkeeper say about entering?"
                 "Why does K. want access to the law at any price?"
                 )


def test_08():
    dialog_about('examples/test',
                 "Does Mary have a book?")


def test_09():
    dialog_about('examples/relativity',
                 "What happens to light in the presence of gravitational fields?")
