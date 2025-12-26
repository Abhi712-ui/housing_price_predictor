import pandas as pd
import config
from sklearn.model_selection import train_test_split

def load_df() -> pd.DataFrame:
    return pd.read_csv(config.DATA_FILE)

def split_features_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    pass

def split_dataset(
    df: pd.DataFrame, 
    training_size: float = config.TRAINING_SIZE,
    validation_size: float = config.VALIDATION_SIZE,
    test_size: float = config.TEST_SIZE,
    random_state: int = config.RANDOM_STATE
    ) -> tuple[
        pd.DataFrame, 
        pd.DataFrame, 
        pd.DataFrame, 
        pd.Series, 
        pd.Series, 
        pd.Series
    ]:
        Y = df[config.TARGET_COL]
        X = df.drop(columns=[config.TARGET_COL])
        X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y, config.TEST_SIZE, config.RANDOM_STATE)
        relative_val_size = config.VALIDATION_SIZE/(1.0 - config.TEST_SIZE)
        X_train, X_val, Y_train, Y_val = train_test_split(X_train_val, Y_train_val, relative_val_size, config.RANDOM_STATE)
        return [X_train, X_val, X_test, Y_train, Y_val, Y_test]
    
    