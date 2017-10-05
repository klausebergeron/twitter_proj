import sklearn
from sklearn import datasets
categories = ['fLearnWord', 'tLearnWord']
tData = sklearn.datasets.load_files('/home/bergeron/scikit-learn/scikit-learn-master/sklearn/twitter_data/data/tData', load_content=True, encoding='utf-8')
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(tData.data)
#print('X_traincounts_shape: ')
#X_train_counts.shape
from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
import numpy as np
from sklearn import metrics
from sklearn.pipeline import Pipeline

#specific to naive bayes------------------------------
from sklearn.naive_bayes import MultinomialNB
text_clf = Pipeline([('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('clf', MultinomialNB()),
	])
#-----------------------------------------------------

#specific to support vector machine-------------------
from sklearn.linear_model import SGDClassifier
text_clf = Pipeline([('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('clf', SGDClassifier(loss='hinge', penalty='l2',
		alpha=1e-3, random_state=42, max_iter=5, tol=None)),
	])
#-----------------------------------------------------

#Get metrics---------------------------------------------start--
text_clf.fit(tData.data, tData.target)
docs_test = tData.data
predicted = text_clf.predict(docs_test)
np.mean(predicted == tData.target)
metrics.confusion_matrix(tData.target, predicted)
print(metrics.classification_report(tData.target, predicted,
	target_names=tData.target_names))
#Get metrics---------------------------------------------end--

#Grid Search--------------------------------------------
from sklearn.model_selection import GridSearchCV
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
	'tfidf__use_idf': (True, False),
	'clf__alpha': (1e-2, 1e-3),
	}
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(tData.data, tData.target)
gs_clf.best_score_
for param_name in sorted(parameters.keys()):
	print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))

predicted = gs_clf.predict(docs_test)
np.mean(predicted == tData.target)
metrics.confusion_matrix(tData.target, predicted)
print(metrics.classification_report(tData.target, predicted,
	target_names=tData.target_names))
tData.target_names[gs_clf.predict(['I am always so sad'])[0]]
#------------------------------------------------------


