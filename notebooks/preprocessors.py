from sklearn.base import BaseEstimator, TransformerMixin


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError('variable should be a list')

        self.variables = variables
        # self.reference_variables = reference_variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        for feature in self.variables:
            X[feature] = X[feature].str[0]

        return X
