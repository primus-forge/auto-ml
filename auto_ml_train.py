try:
    models
except:
    models = {}

def df__auto_ml_train(_df=None, feature_cols="*", target_col=None, model_name=None, **kwargs):
            
    if _df is None:
        raise ValueError("_df cannot be None")

    if target_col is None:
        raise ValueError("target_col cannot be None")

    if model_name is None:
        raise ValueError("model_name cannot be None")


    import pandas as pd
    from sklearn.model_selection import train_test_split
    from supervised.automl import AutoML

    pdf = _df.data
    
    feature_col_names = _df.cols.select(feature_cols).cols.names(target_col, invert=True)

    X_train, X_test, y_train, y_test = train_test_split(
        pdf[feature_col_names], pdf[target_col], test_size=0.25
    )
    
    if not len(kwargs):
        kwargs.update({"mode": "Explain"})

    automl = AutoML(**kwargs)
    automl.fit(X_train, y_train)
    
    # SAVE
    global models
    models.update({model_name: automl})
    # SAVE
    
    return _df
    # return automl.report()
