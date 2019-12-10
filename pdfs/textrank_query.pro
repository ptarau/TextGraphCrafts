query_dep(0, 'What', 'WP', 'cop', 'are', 'VBP').
query_dep(0, 'What', 'WP', 'nsubj', 'applications', 'NNS').
query_dep(0, 'applications', 'NNS', 'det', 'the', 'DT').
query_dep(0, 'applications', 'NNS', 'nmod', 'TextRank', 'NNP').
query_dep(0, 'TextRank', 'NNP', 'case', 'of', 'IN').
query_dep(0, 'What', 'WP', 'punct', '?', '.').
query_dep(1, 'works', 'VBZ', 'advmod', 'How', 'WRB').
query_dep(1, 'works', 'VBZ', 'nsubj', 'extraction', 'NN').
query_dep(1, 'extraction', 'NN', 'compound', 'sentence', 'NN').
query_dep(1, 'works', 'VBZ', 'punct', '?', '.').
query_dep(2, 'What', 'WP', 'cop', 'is', 'VBZ').
query_dep(2, 'What', 'WP', 'nsubj', 'role', 'NN').
query_dep(2, 'role', 'NN', 'det', 'the', 'DT').
query_dep(2, 'role', 'NN', 'nmod', 'PageRank', 'NNP').
query_dep(2, 'PageRank', 'NNP', 'case', 'of', 'IN').
query_dep(2, 'What', 'WP', 'punct', '?', '.').
 
query_edge(0, 'be', 'VBP', 'cop', 'what', 'WP').
query_edge(0, 'be', 'VBP', 'recommends', 0, 'SENT').
query_edge(0, 'what', 'WP', 'nsubj', 'application', 'NNS').
query_edge(0, 'application', 'NNS', 'first_in', 0, 'SENT').
query_edge(0, 'the', 'DT', 'det', 'application', 'NNS').
query_edge(0, 'the', 'DT', 'recommends', 0, 'SENT').
query_edge(0, 'application', 'NNS', 'nmod', 'TextRank', 'NNP').
query_edge(0, 'TextRank', 'NNP', 'first_in', 0, 'SENT').
query_edge(0, 'of', 'IN', 'case', 'TextRank', 'NNP').
query_edge(0, 'of', 'IN', 'recommends', 0, 'SENT').
query_edge(0, 0, 'SENT', 'predicate', 'what', 'WP').
query_edge(1, 'how', 'WRB', 'advmod', 'work', 'VBZ').
query_edge(1, 'how', 'WRB', 'recommends', 1, 'SENT').
query_edge(1, 'work', 'VBZ', 'nsubj', 'extraction', 'NN').
query_edge(1, 1, 'SENT', 'about', 'extraction', 'NN').
query_edge(1, 'extraction', 'NN', 'first_in', 1, 'SENT').
query_edge(1, 'extraction', 'NN', 'compound', 'sentence', 'NN').
query_edge(1, 'sentence', 'NN', 'first_in', 1, 'SENT').
query_edge(1, 'extraction', 'NN', 'fused', 'sentence extraction', 'NN').
query_edge(1, 'sentence', 'NN', 'fused', 'sentence extraction', 'NN').
query_edge(1, 1, 'SENT', 'predicate', 'work', 'VBZ').
query_edge(2, 'be', 'VBZ', 'cop', 'what', 'WP').
query_edge(2, 'be', 'VBZ', 'recommends', 2, 'SENT').
query_edge(2, 'what', 'WP', 'nsubj', 'role', 'NN').
query_edge(2, 'role', 'NN', 'first_in', 2, 'SENT').
query_edge(2, 'the', 'DT', 'det', 'role', 'NN').
query_edge(2, 'the', 'DT', 'recommends', 2, 'SENT').
query_edge(2, 'role', 'NN', 'nmod', 'PageRank', 'NNP').
query_edge(2, 'PageRank', 'NNP', 'first_in', 2, 'SENT').
query_edge(2, 'of', 'IN', 'case', 'PageRank', 'NNP').
query_edge(2, 'of', 'IN', 'recommends', 2, 'SENT').
query_edge(2, 2, 'SENT', 'predicate', 'what', 'WP').
 
query_rank('what', 0.20280501098637876).
query_rank('application', 0.1002416729771124).
query_rank('role', 0.1002416729771124).
query_rank(0, 0.07317364837059837).
query_rank(2, 0.07317364837059837).
query_rank('extraction', 0.06223179863075554).
query_rank('TextRank', 0.056653141658817116).
query_rank('PageRank', 0.056653141658817116).
query_rank('sentence extraction', 0.04163782117628062).
query_rank('work', 0.036300613665054854).
query_rank('sentence', 0.02921947449750463).
query_rank(1, 0.02520563404215813).
query_rank('how', 0.011587023012724948).
query_rank('be', 0.011587023012724948).
query_rank('of', 0.011587023012724948).
query_rank('the', 0.011587023012724948).
 
query_w2l('TextRank', 'TextRank', 'NNP').
query_w2l('the', 'the', 'DT').
query_w2l('PageRank', 'PageRank', 'NNP').
query_w2l('applications', 'application', 'NNS').
query_w2l('extraction', 'extraction', 'NN').
query_w2l('sentence', 'sentence', 'NN').
query_w2l('is', 'be', 'VBZ').
query_w2l('What', 'what', 'WP').
query_w2l('of', 'of', 'IN').
query_w2l('?', '?', '.').
query_w2l('works', 'work', 'VBZ').
query_w2l('role', 'role', 'NN').
query_w2l('are', 'be', 'VBP').
query_w2l('How', 'how', 'WRB').
 
query_sent(0, ['What', 'are', 'the', 'applications', 'of', 'TextRank', '?']).
query_sent(1, ['How', 'sentence', 'extraction', 'works', '?']).
query_sent(2, ['What', 'is', 'the', 'role', 'of', 'PageRank', '?']).
 
 
query_rel('application', 'is_a', 'use', -10).
query_rel('sentence', 'is_a', 'term', -520).
query_rel('technology', 'is_a', 'application', -1057).
 
query_param('quest_memory', 3).
query_param('max_answers', 3).
query_param('repeat_answers', 'yes').
query_param('by_rank', 'yes').
