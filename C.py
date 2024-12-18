import pandas as pd
from itertools import product

data = []

for p in [1,0]:
    for q in [1,0]:
        for r in [1,0]:
            
            not_q = 1 - q
            not_r = 1 - r
            not_p = 1 - p

            implication_p_not_q = int(not p or not_q)
            conjuntion_q_not_r = int(q or not_r)
            first_part = (implication_p_not_q and conjuntion_q_not_r)
            conjunction_fist_part_r = int(first_part and r)

            final = int(conjunction_fist_part_r or not_p)

            data.append([p, q, r, not_q, not_r, not_p, implication_p_not_q, conjuntion_q_not_r, first_part, conjunction_fist_part_r, final])

data = [['TRUE' if x == 1 else 'FALSE' for x in row] for row in data]

col = ["p","q","r","¬q", "¬r", "¬p", "p->¬q", "q∨¬r", "(p->¬q)∧(q∨¬r)", "(p->¬q)∧(q∨¬r)∧r", "((p->¬q)∧(q∨¬r)∧r)->¬p"]
df = pd.DataFrame(data, columns=col)
print(df)