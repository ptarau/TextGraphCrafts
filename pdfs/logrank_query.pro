query_dep(0, 'What', 'WP', 'cop', 'are', 'VBP').
query_dep(0, 'What', 'WP', 'nsubj', 'applications', 'NNS').
query_dep(0, 'applications', 'NNS', 'det', 'the', 'DT').
query_dep(0, 'applications', 'NNS', 'nmod', 'dialogs', 'NNS').
query_dep(0, 'dialogs', 'NNS', 'case', 'of', 'IN').
query_dep(0, 'dialogs', 'NNS', 'compound', 'voice', 'NN').
query_dep(0, 'What', 'WP', 'punct', '?', '.').
query_dep(1, 'use', 'VB', 'aux', 'Do', 'VB').
query_dep(1, 'use', 'VB', 'nsubj', 'you', 'PRP').
query_dep(1, 'use', 'VB', 'dobj', 'Dependencies', 'NNPS').
query_dep(1, 'Dependencies', 'NNPS', 'compound', 'Universal', 'NNP').
query_dep(1, 'use', 'VB', 'punct', '?', '.').
query_dep(2, 'used', 'VBN', 'nsubjpass', 'parser', 'NN').
query_dep(2, 'parser', 'NN', 'det', 'What', 'WDT').
query_dep(2, 'used', 'VBN', 'auxpass', 'is', 'VBZ').
query_dep(2, 'used', 'VBN', 'punct', '?', '.').
 
query_edge(0, 'be', 'VBP', 'cop', 'what', 'WP').
query_edge(0, 'be', 'VBP', 'recommends', 0, 'SENT').
query_edge(0, 'what', 'WP', 'nsubj', 'application', 'NNS').
query_edge(0, 'application', 'NNS', 'first_in', 0, 'SENT').
query_edge(0, 'the', 'DT', 'det', 'application', 'NNS').
query_edge(0, 'the', 'DT', 'recommends', 0, 'SENT').
query_edge(0, 'application', 'NNS', 'nmod', 'dialog', 'NNS').
query_edge(0, 'dialog', 'NNS', 'first_in', 0, 'SENT').
query_edge(0, 'of', 'IN', 'case', 'dialog', 'NNS').
query_edge(0, 'of', 'IN', 'recommends', 0, 'SENT').
query_edge(0, 'dialog', 'NNS', 'compound', 'voice', 'NN').
query_edge(0, 'voice', 'NN', 'first_in', 0, 'SENT').
query_edge(0, 'dialog', 'NNS', 'fused', 'voice dialog', 'NNS').
query_edge(0, 'voice', 'NN', 'fused', 'voice dialog', 'NN').
query_edge(0, 0, 'SENT', 'predicate', 'what', 'WP').
query_edge(1, 'do', 'VB', 'aux', 'use', 'VB').
query_edge(1, 'do', 'VB', 'recommends', 1, 'SENT').
query_edge(1, 'you', 'PRP', 'nsubj', 'use', 'VB').
query_edge(1, 'you', 'PRP', 'recommends', 1, 'SENT').
query_edge(1, 'use', 'VB', 'dobj', 'Dependencies', 'NNPS').
query_edge(1, 1, 'SENT', 'about', 'Dependencies', 'NNPS').
query_edge(1, 'Dependencies', 'NNPS', 'first_in', 1, 'SENT').
query_edge(1, 'Dependencies', 'NNPS', 'compound', 'Universal', 'NNP').
query_edge(1, 'Universal', 'NNP', 'first_in', 1, 'SENT').
query_edge(1, 'Dependencies', 'NNPS', 'fused', 'Universal Dependencies', 'NNPS').
query_edge(1, 'Universal', 'NNP', 'fused', 'Universal Dependencies', 'NNP').
query_edge(1, 1, 'SENT', 'predicate', 'use', 'VB').
query_edge(2, 'use', 'VBN', 'nsubjpass', 'parser', 'NN').
query_edge(2, 2, 'SENT', 'about', 'parser', 'NN').
query_edge(2, 'parser', 'NN', 'first_in', 2, 'SENT').
query_edge(2, 'what', 'WDT', 'det', 'parser', 'NN').
query_edge(2, 'what', 'WDT', 'recommends', 2, 'SENT').
query_edge(2, 'be', 'VBZ', 'auxpass', 'use', 'VBN').
query_edge(2, 'be', 'VBZ', 'recommends', 2, 'SENT').
query_edge(2, 2, 'SENT', 'predicate', 'use', 'VBN').
 
query_rank('parser', 0.15268789894382484).
query_rank('use', 0.12287421398417958).
query_rank('Dependencies', 0.09246838778222813).
query_rank(2, 0.08846883009774224).
query_rank('what', 0.06569301996702034).
query_rank('Universal Dependencies', 0.05499713113928836).
query_rank(1, 0.05089217659886602).
query_rank('Universal', 0.038594555230229394).
query_rank('application', 0.03627574171247087).
query_rank('dialog', 0.03307999728538456).
query_rank('voice dialog', 0.031018836677345698).
query_rank(0, 0.030091204636021083).
query_rank('voice', 0.021767680978313983).
query_rank('you', 0.012395154782678703).
query_rank('be', 0.012395154782678703).
query_rank('do', 0.012395154782678703).
query_rank('the', 0.012395154782678703).
query_rank('of', 0.012395154782678703).
 
query_w2l('are', 'be', 'VBP').
query_w2l('voice', 'voice', 'NN').
query_w2l('Universal', 'Universal', 'NNP').
query_w2l('Dependencies', 'Dependencies', 'NNPS').
query_w2l('dialogs', 'dialog', 'NNS').
query_w2l('What', 'what', 'WDT').
query_w2l('?', '?', '.').
query_w2l('applications', 'application', 'NNS').
query_w2l('the', 'the', 'DT').
query_w2l('of', 'of', 'IN').
query_w2l('use', 'use', 'VB').
query_w2l('is', 'be', 'VBZ').
query_w2l('used', 'use', 'VBN').
query_w2l('you', 'you', 'PRP').
query_w2l('Do', 'do', 'VB').
query_w2l('parser', 'parser', 'NN').
query_w2l('What', 'what', 'WP').
 
query_sent(0, ['What', 'are', 'the', 'applications', 'of', 'voice', 'dialogs', '?']).
query_sent(1, ['Do', 'you', 'use', 'Universal', 'Dependencies', '?']).
query_sent(2, ['What', 'parser', 'is', 'used', '?']).
 
 
query_rel('application', 'is_a', 'use', -13).
query_rel('parser', 'is_a', 'program', -106).
query_rel('Dependencies', 'is_a', 'state', -156).
query_rel('reliance', 'is_a', 'Dependencies', -636).
query_rel('technology', 'is_a', 'application', -974).
query_rel('Universal', 'is_a', 'rule', -1718).
query_rel('dialog', 'is_a', 'talk', -1808).
 
