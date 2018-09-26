import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = np.loadtxt("/Users/muwuxu/Documents/visualized/data.csv", dtype=str, delimiter=",")
row, col = data.shape

# Put all the possible labels in label_list
label_list = []
for i in range(row):
  if data[i][0] not in label_list:
    label_list.append(data[i][0])
for i in range(row):
  if data[i][1] not in label_list:
    label_list.append(data[i][1])
print(label_list)

# Give every label an unique index.
label_to_idx = {}
for i in range(len(label_list)):
  label_to_idx[label_list[i]] = i

# Make an array to store the value for every pair.
val_arr = np.zeros((len(label_list),len(label_list)))
for i in range(row):
  label1 = data[i][0]
  label2 = data[i][1]
  val = float(data[i][2])
  idx1 = label_to_idx[label1]
  idx2 = label_to_idx[label2]
  if idx1>idx2:
    val_arr[idx1][idx2] = val
  else:
    val_arr[idx2][idx1] = val
val_arr = np.around(val_arr, decimals=3)
print(val_arr)

fig,ax = plt.subplots()
im = ax.imshow(val_arr, cmap=plt.cm.binary)

# Show the colorbar
cbar = ax.figure.colorbar(im, ax=ax,)
cbar.ax.set_ylabel("modify here for color bar label", rotation=-90, va="bottom")

# set axis x text labels
ax.set_xticks(np.arange(len(label_list)))
ax.set_xticklabels(label_list)

# set axis y text labels
ax.set_yticks(np.arange(len(label_list)))
ax.set_yticklabels(label_list)

# show the values on the grids
for i in range(len(label_list)):
  for j in range(0,i):
    text = ax.text(j,i, val_arr[i,j],ha="center", va="center", color="black")

ax.set_title("set your title here")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.show()