import numpy as np

a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
csv_rows = ["{},{},{}".format(i, j, k) for i, j, k in a]
csv_text = "\n".join(csv_rows)

with open('sample.csv', 'w') as f:
    f.write(csv_text)