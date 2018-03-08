#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
from scraputils import split


class NaiveBayesClassifier:

    def __init__(self, alpha=1):
        self.alpha = alpha

    def fit(self, x, y):
        """ Fit Naive Bayes classifier according to X, y. """
        self.labels = [i for i in set(y)]
        self.labels.sort()
        how_many_labels = len(self.labels)
        cnt_label = [0] * how_many_labels
        for i in range(len(y)):
            y[i] = self.labels.index(y[i]) + 1
            cnt_label[y[i] - 1] += 1
        self.words_attributes = [[] for _ in range(how_many_labels * 2 + 1)]
        self.predict_labels = [math.log(number / sum(cnt_label)) for number in cnt_label]
        for i in range(len(x)):
            words = split(x[i])
            for word in words:
                if word in self.words_attributes[0]:
                    self.words_attributes[y[i]][self.words_attributes[0].index(word)] += 1
                else:
                    self.words_attributes[0].append(word)
                    self.words_attributes[y[i]].append(1)
                    prob_of_label = y[i]
                    for j in range(how_many_labels - 1):
                        prob_of_label = (prob_of_label % how_many_labels) + 1
                        self.words_attributes[prob_of_label].append(0)
                    for col in range(how_many_labels + 1, how_many_labels * 2 + 1):
                        self.words_attributes[col].append(0)
        words_on_labels = [sum(self.words_attributes[i + 1]) for i in range(how_many_labels)]

        for row in range(len(self.words_attributes[0])):
            for col in range(how_many_labels + 1, how_many_labels * 2 + 1):
                self.words_attributes[col][row] = (self.words_attributes[col - how_many_labels][row] + self.alpha) / \
                                       (words_on_labels[col - how_many_labels - 1] + self.alpha *
                                        len(self.words_attributes[0]))

    def predict(self, x):
        """ Perform classification on an array of test vectors X. """
        labels = []
        how_many_labels = len(self.labels)
        for string in x:
            string_labels = [i for i in self.predict_labels]
            words = split(string)
            for word in words:
                if word in self.words_attributes[0]:
                    for i in range(how_many_labels):
                        string_labels[i] += math.log(self.words_attributes[i + how_many_labels + 1][self.words_attributes[0].index(word)])
            for i in range(how_many_labels):
                if string_labels[i] == max(string_labels):
                    labels.append(self.labels[i])
                    break
        return labels

    def score(self, x_testing, y_testing):
        """ Returns the mean accuracy on the given test data and labels. """
        prediction = self.predict(x_testing)
        count = 0
        for i in range(len(prediction)):
            if prediction[i] == y_testing[i]:
                count += 1
        return count / len(y_testing)