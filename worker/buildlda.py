from __future__ import print_function

import re
from sklearn.neighbors import NearestNeighbors

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import LatentDirichletAllocation
from worker.models import JobDescription


class BuildLda:
    def __init__(self):
        self.build_model()
        self.transform_set()
        self.build_nearest_neighbours()


    def build_model(self):
        print('Building LDA')
        strings = JobDescription.objects.values('url', 'body')

        data_samples = []
        seen_strings = set()
        for string in strings:
            if string['body'] not in seen_strings:
                seen_strings.add(string['body'])
                data_samples.append({'url': string['url'], 'string': self.clean_string(string['body'])})

        self.data_samples = DataFrame(data_samples)

        n_features = 20000
        n_topics = 30
        n_top_words = 10
        max_iter = 200

        self.tf_vectorizer = CountVectorizer(max_features=n_features,
                                        stop_words='english')

        tf = self.tf_vectorizer.fit_transform(self.data_samples['string'])

        self.lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=max_iter,
                                        learning_method='online')

        self.lda.fit(tf)

        print()
        print("\nTopics in LDA model:")
        tf_feature_names = self.tf_vectorizer.get_feature_names()
        self.print_top_words(self.lda, tf_feature_names, n_top_words)

    def test_single_doc(self, string):
        data_samples = DataFrame([{'string': self.clean_string(string)}])
        test = self.tf_vectorizer.transform(data_samples['string'])
        return self.lda.transform(test)

    def transform_set(self):
        print('Getting LDA Transformation')
        vectorizor_data = self.tf_vectorizer.transform(self.data_samples['string'])
        self.results = self.lda.transform(vectorizor_data)

    def build_nearest_neighbours(self):
        print('Build Nearest Neighbours')
        self.nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(self.results)

    def get_neighbours(self, string, print=True):
        single_doc = self.test_single_doc(string)
        distances, indices = self.nbrs.kneighbors(single_doc)

        if print:
            self.print_neighbours(indices[0])

        return [distances, indices]

    def print_neighbours(self, indices):
        print('Closest 10 jobs:')
        for indice in indices:
            url = self.data_samples.get_value(indice, 'url')
            print('http://www.seek.com.au%s' % url)

    def print_top_words(self, model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):
            print("Topic "+str(topic_idx)+": "+" ".join([feature_names[i]
                            for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

    def clean_string(self, string):
        # 2. Remove non-letters
        letters_only = re.sub("[^a-zA-Z]", " ", string)
        return letters_only