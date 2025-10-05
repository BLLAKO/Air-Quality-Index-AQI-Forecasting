import lightgbm as lgb

def train_model(X_train, y_train):
    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)
    return model
