from sklearn.base import BaseEstimator, TransformerMixin

from typing import List
import pandas as pd


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, variables: List[str]):
        if not isinstance(variables, list):
            raise ValueError('variable should be a list')

        self.variables = variables
        # self.reference_variables = reference_variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        for feature in self.variables:
            X[feature] = X[feature].str[0]

        return X
