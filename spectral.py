import pickle
import numpy as np
import pylab as pl
from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

x = pickle.load(open("X.p","rb"))
y = pickle.load(open("y.p","rb"))
print y
l = 100
x, y = np.indices((l, l))
print x[0]

center1 = (15.3,-5)
center2 = (40.2,-9.1)
center3 = (64,-10)
center4 = (83.1 , -3)

radius1, radius2, radius3, radius4 = 9,3.5,4,18

circle1 = (x - center1[0]) ** 2 + (y - center1[1]) ** 2 < radius1 ** 2
circle2 = (x - center2[0]) ** 2 + (y - center2[1]) ** 2 < radius2 ** 2
circle3 = (x - center3[0]) ** 2 + (y - center3[1]) ** 2 < radius3 ** 2
circle4 = (x - center4[0]) ** 2 + (y - center4[1]) ** 2 < radius4 ** 2

img = circle1 + circle2 + circle3 + circle4
mask = img.astype(bool)
img = img.astype(float)

img += 1 + 0.2 * np.random.randn(*img.shape)
graph = image.img_to_graph(img, mask=mask)
graph.data = np.exp(-graph.data / graph.data.std())

labels = spectral_clustering(graph, n_clusters=4, eigen_solver='arpack')
label_im = -np.ones(mask.shape)
label_im[mask] = labels
pl.matshow(img)
pl.matshow(label_im)