#!/usr/bin/env python3
import sys

from fizzbuzz import fizzbuzz
from sklearn.ensemble import RandomForestClassifier

NUM = 0
FIZZ = 1
BUZZ = 2
FIZZBUZZ = 3

def num_div_1_to_k(n, k):
    return [int((n % x) == 0) for x in range(1,k)]


def make_training_set(height, width):
    data = []
    targets = []

    for n in range (1, height+1):
        result = fizzbuzz(n)

        if result == "Fizz":
            actual_result = FIZZ
        elif result == "Buzz":
            actual_result = BUZZ
        elif result == "FizzBuzz":
            actual_result = FIZZBUZZ
        else:
            actual_result = NUM

        features = num_div_1_to_k(n, width)
        data.append(features)
        targets.append(actual_result)

    return data, targets


def fizzbuzz_ml(clf, n, width):
    prediction, = clf.predict([num_div_1_to_k(n, width)])

    if prediction == NUM:
        answer = n
    elif prediction == FIZZ:
        answer = "Fizz"
    elif prediction == BUZZ:
        answer = "Buzz"
    elif prediction == FIZZBUZZ:
        answer = "FizzBuzz"
    else:
        answer = "Something went wrong"

    return answer

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print("Usage: {} <number of tests> <training set height> <num features/training set width>"
              .format(sys.argv[0]))
        exit(1)

    N = (int(sys.argv[1]) + 1)
    training_size = int(sys.argv[2])
    num_features = int(sys.argv[3])

    X, Y = make_training_set(training_size, num_features)
    clf = RandomForestClassifier()
    clf = clf.fit(X, Y)

    print("Trained on integers [1,{}], with {} mod-values."
          .format(training_size, num_features))

    success = 0
    failures = 0
    for n in range(1, N):
        #print("{}: {}/{}".format(n, fizzbuzz_ml(clf, n), fizzbuzz(n)))
        ml_result = fizzbuzz_ml(clf, n, num_features)
        expected_result = fizzbuzz(n)
        if ml_result == expected_result:
            success += 1
        else:
            print("F: {} => {}, should be {}"
                  .format(n, ml_result, expected_result))
            failures += 1

    print("Tested {} integers: {} successes and {} failures"
          .format(N-1, success, failures))
