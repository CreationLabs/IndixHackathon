from sklearn.svm import SVC
from sklearn import svm
from time import time
import numpy as np
import pylab as pl
import pickle
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from operator import itemgetter

np.random.seed(42)

def optionize(x):
	score = x['L'] + -1*x['P']
	if score > 0:
		return 0
	else :
		return 1
	# Binary thresholding

import simplejson as json
from levenshtein import editDistance, editDistanceFast
tagfile = open('reversetags.json')
keyfile = open('reversekeys.json')
tags = open('tag.json')
keys = open('key.json')



tagdata = json.load(tagfile)
keydata = json.load(keyfile)
keysarray = json.load(keys)
tagsarray = json.load(tags)
tagmatrix = {}
#print tagmatrix
for tag in tagsarray.keys():
	tagmatrix[tag] = []
	for othertag in tagsarray.keys():
		try:
			tagmatrix[tag].append((othertag,editDistanceFast(tag,othertag)))		
		except:
			tagmatrix[tag].append((othertag,editDistance(tag,othertag)))
	tagmatrix[tag] = sorted(tagmatrix[tag],key=lambda tup:tup[1])
	#tagmatrix[tag] = tagmatrix[tag][:100]
clf = svm.SVC(kernel='poly', C=1.0)
X = []
y = []
for tag in tagmatrix.keys():
	X.append(map(itemgetter(1),tagmatrix[tag])+[tagsarray[tag]['L'],tagsarray[tag]['P']])
	y.append(optionize(tagsarray[tag]))
X = scale(X)
print X
print y
pickle.dump(X,open("X.p","wb"))
pickle.dump(y,open("y.p","wb"))
raw_input("Will die now")
clf.fit(X,y)


#w = clf.coef_[0]
#a = -w[0]/w[1]
#xx = np.linspace(-20,20)
#yy = a*xx - clf.intercept_[0]/ w[1]

n_samples = len(tagmatrix.keys())
n_features = 3
n_digits = 4
labels = y
sample_size = 600

print("n_digits: %d, \t n_samples %d, \t n_features %d"
      % (n_digits, n_samples, n_features))


print(79 * '_')
print('% 9s' % 'init'
      '    time  inertia    homo   compl  v-meas     ARI AMI  silhouette')


def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=sample_size)))

bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
              name="k-means++", data=X)

bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
              name="random", data=X)

# in this case the seeding of the centers is deterministic, hence we run the
# kmeans algorithm only once with n_init=1
pca = PCA(n_components=n_digits).fit(X)
bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),
              name="PCA-based",
              data=X)
print(79 * '_')

###############################################################################
# Visualize the results on PCA-reduced data

reduced_data = PCA(n_components=2).fit_transform(X)
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02    # point in the mesh [x_min, m_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() + 1, reduced_data[:, 0].max() - 1
y_min, y_max = reduced_data[:, 1].min() + 1, reduced_data[:, 1].max() - 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
pl.figure(1)
pl.clf()
pl.imshow(Z, interpolation='nearest',
          extent=(xx.min(), xx.max()/2, yy.min(), yy.max()/3),
          cmap=pl.cm.Paired,
          aspect='auto', origin='lower')

pl.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=10)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
pl.scatter(centroids[:, 0], centroids[:, 1],
           marker='x', s=169, linewidths=3,
           color='w', zorder=10)
pl.title('K-means clustering')
pl.xlim(x_min, x_max/2)
pl.ylim(y_min, y_max/3)
pl.xticks(())
pl.yticks(())
#h0 = pl.plot(xx,yy,'k-',label='no weights')
#pl.scatter(X[:, 0], X[:, 1], c=y, cmap=pl.cm.Paired)
#pl.legend()
#pl.axis('tight')
pl.show()
#for tag in tagdata:

