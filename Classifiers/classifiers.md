# Classifiers
This lecture covers some basic machine learning classifiers: One Rule and K-Nearest-Neighbor.

## One Rule
One Rule, aka 1R or OneR, is possibly the simplest eager learning algorithm. It's fairly accurate, usually aroundd 60-80% accuracy. The algorithm finds the most accurate rule (a predictor leads to a target value) and saves it. When predicting, any predictor value that doesn't meet the rule gets assigned the other target value. This is why this only works as a binomial classifier. Unfortunately, there doesn't seem to be any major implementation of this online, but generally any other classifier will do a better job.

## K-Nearest-Neighbor
K-Nearest-Neighbor, aka KNN, is a lazy learner. While eager learners save some sort of trained model, requring extra time to train, lazy learners don't actually train. The KNN algorithm is actually very simple, even more than 1R. KNN centers around distance, and finding a variable number of objects close to the prediction data. This is very easy to conceptualize in one predictor dimension. Imagine this table:

| Target | Predictor |
| --- | --- | 
| A | 15 |
| B | 65 |
| B | 78 |
| A | 20 |
| A | 10 |
| B | 70 |

If we have an unclassifed value at 21 and K = 3, then the 3 closest neighbors are all A's. Given a generalized distance formula across an arbitrary number of dimensions, we can use KNN to classify wide data sets multinomially.