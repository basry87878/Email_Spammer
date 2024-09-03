text =   ''' 

import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
print(df)
#text = df.astype(str)


output:
A   B   C   D
0    1  82  10  82
1   82  42  18  14
2   30  80  15  77
3   29  98  57  80
4    9  70  48  45
..  ..  ..  ..  ..
95  18  10  70  83
96   1  53   3  73
97  26  26   3  98
98  71  16  97  47
99  51  95  57  53 

'''