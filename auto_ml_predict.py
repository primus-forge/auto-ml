def df__auto_ml_predict(df, col_name="prediction_result", model_name=None):
    
    # TODO: check datadrift
    
    if model_name is None:
        raise ValueError("model_name cannot be None")

    # LOAD
    global models
    if model_name not in models:
        raise AttributeError(f"'{model_name}' not found in saved models")
    automl = models[model_name]
    # LOAD

    predictions = automl.predict(df.data)
    return df.cols.assign({col_name: predictions})