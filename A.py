import pandas as pd
from itertools import product

data = []

for p in [1,0]:
    for q in [1,0]:
        for r in [1,0]:
           not_r = 1 - r
           implication_q_not_r = int(not q or not_r)
           implication_p_q = int(not p or q)
           conjunction = int(implication_q_not_r and implication_p_q)
           implication_p_not_r = int(not p or not_r)
           final = int(conjunction or implication_p_not_r)
           data.append([p, q, r, not_r, implication_q_not_r, implication_p_q, conjunction, implication_p_not_r, final])

# Reemplazar 1 y 0 por "true" y "false"
data = [['TRUE' if x == 1 else 'FALSE' for x in row] for row in data]

col = ["p","q","r","¬r", "q->¬r", "p->q", "(q->¬r)∧(p->q)", "p->¬r", "((q->¬r)∧(p->q))->(p->¬r)"]
df = pd.DataFrame(data, columns=col)
print(df)
