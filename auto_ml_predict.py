def df__auto_ml_predict(df, col_name="prediction_result", model_name=None):
    
    # TODO: check datadrift
    
    if model_name is None:
        raise ValueError("model_name cannot be None")

    import pickle

    with open(f"{model_name}.automlmodel", 'rb') as f:
        automl = pickle.load(f)

    predictions = automl.predict(df.data)
    return df.cols.assign({col_name: predictions})