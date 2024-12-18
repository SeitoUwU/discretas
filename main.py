import pandas as pd
from itertools import product

data = []

for p in [1,0]:
    for q in [1,0]:
        for r in [1,0]:
            for s in [1,0]:
                not_R = 1 - r
                not_S = 1 - s
                
                implication_p_q = int(not p or q)
                implication_not_R_not_S = int(not not_R or not_S)
                conjuntion_p_s = int(p and s)
                left = (implication_p_q and implication_not_R_not_S and conjuntion_p_s)
                conjuntion_q_s = int(q and s)

                final = int(not left or conjuntion_q_s)
                data.append([p, q, r, s, not_R, not_S, implication_p_q, implication_not_R_not_S, conjuntion_p_s, left, conjuntion_q_s, final])

col = ["p","q","r","s","¬r", "¬s", "p→q", "¬r->¬s", "p∧s", "(p→q)∧(¬r->¬s)∧(p∧s)", "q∧s", "((p->q)^(¬r->¬s)^(p^s))->(q^s)"]
df = pd.DataFrame(data, columns=col)
print(df)