from joblib import dump, load
from sklearn.datasets import fetch_openml
# from sklearn.svm import SVC
# from sklearn.linear_model import SGDClassifier

# mnist = fetch_openml("mnist_784", as_frame=False)
# X,y = mnist.data, mnist.target

# class Model:
#     """Model Class for predictions"""
#     def __init__(self):
#         svm_clf = SVC(random_state=42)
#         sgd_clf = SGDClassifier(random_state=42)
#         # svm_clf.fit(X[:3000], y[:3000])
#         sgd_clf.fit(X[:59000], y[:59000])        
#         # self.model = joblib.load("my_classifier_model.pkl")
#         # self.model = svm_clf
#         self.model = sgd_clf
        
#     def predict_input(self, arr):
#         output = self.model.predict([arr.reshape(784)])
#         # print(output)
#         return output
    
#     def save_model(self):
#         dump(self.model, 'sgd_clf.joblib')
        
        
# my_model = Model()
# any_num = X[0]
# my_model.predict_input(any_num)
# print("Shape:", any_num.shape)


def predict(arr, model=None):
    output = model.predict([arr.reshape(784)])
    return output
