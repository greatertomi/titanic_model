from sklearn.pipeline import Pipeline

from feature_engine.imputation import AddMissingIndicator, CategoricalImputer, MeanMedianImputer
from feature_engine.encoding import RareLabelEncoder, OneHotEncoder

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from regression_model.processing.features import ExtractLetterTransformer
from regression_model.config.core import config

# set up the pipeline
titanic_pipe = Pipeline([

    # ===== IMPUTATION =====
    # impute categorical variables with string missing
    ('categorical_imputation', CategoricalImputer(
        imputation_method='missing', variables=config.model_config.categorical_variables)),

    # add missing indicator to numerical variables
    ('missing_indicator', AddMissingIndicator(variables=config.model_config.numerical_variables)),

    # impute numerical variables with the median
    ('median_imputation', MeanMedianImputer(
        imputation_method='median', variables=config.model_config.numerical_variables)),

    # Extract letter from cabin
    ('extract_letter', ExtractLetterTransformer(variables=config.model_config.cabin)),

    # == CATEGORICAL ENCODING ======
    # remove categories present in less than 5% of the observations (0.05)
    # group them in one category called 'Rare'
    ('rare_label_encoder', RareLabelEncoder(
        tol=0.05, n_categories=1, variables=config.model_config.categorical_variables)),

    # encode categorical variables using one hot encoding into k-1 variables
    ('categorical_encoder', OneHotEncoder(
        drop_last=True, variables=config.model_config.categorical_variables)),

    # scale
    ('scaler', StandardScaler()),

    ('Logit', LogisticRegression(C=config.model_config.c, random_state=config.model_config.random_state)),
])
