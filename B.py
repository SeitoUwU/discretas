import pandas as pd
from itertools import product

data = []

for p in [1,0]:
    for q in [1,0]:
        for r in [1,0]:
            implication_p_r = int(not p or r)
            implication_q_p = int(not q or p)
            conjunction_p_q = int(p and q)
            left = (implication_p_r and implication_q_p and conjunction_p_q)
            conjunction_q_r = int(q and r)
            final = int(not left or conjunction_q_r)
            data.append([p, q, r, implication_p_r, implication_q_p, conjunction_p_q, left, conjunction_q_r, final])

data = [['TRUE' if x == 1 else 'FALSE' for x in row] for row in data]

col = ["p","q","r","p->r", "q->p", "p∧q", "(p->r)∧(q->p)∧(p∧q)", "q∧r", "((p->r)∧(q->p)∧(q∧p))->(q∧r)"]
df = pd.DataFrame(data, columns=col)
print(df)