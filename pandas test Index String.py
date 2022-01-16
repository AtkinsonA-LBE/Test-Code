import pandas as pd
import numpy as np

ind = pd.Index(['Mouse', 'dog', 'house and parrot', '23.0', np.NaN])
ind.str.contains('oG', regex=False)

ind = pd.DataFrame(ind)

print(ind.head())


