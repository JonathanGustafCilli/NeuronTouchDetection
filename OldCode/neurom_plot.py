import neurom as nm
from neurom import viewer
m = nm.load_morphology('51-5-DE-cor-rep-ax.swc')
fig, ax = viewer.draw(m)
fig.show()

fig, ax = viewer.draw(m, mode='3d') # valid modes '2d', '3d', 'dendrogram'
fig.show()
input("Your name: ")