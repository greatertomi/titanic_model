import typing as t

import numpy as np
import pandas as pd

from regression_model import __version__ as _version
from regression_model.config.core import config
from regression_model.processing.data_manager import load_pipeline

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_titanic_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:
    data = pd.DataFrame(input_data)

    predictions = _titanic_pipe.predict(X=data[config.model_config.features])
    results = {
        "predictions": [np.exp(pred) for pred in predictions],
        "version": _version,
    }

    return results
