def df__auto_ml_predict(df, col_name="prediction_result", model_name=None):
    
    # TODO: check datadrift
    
    assert model_name is not None

    # LOAD
    global models
    assert model_name in models
    automl = models[model_name]
    # LOAD

    predictions = automl.predict(df.data)
    return df.cols.assign({col_name: predictions})