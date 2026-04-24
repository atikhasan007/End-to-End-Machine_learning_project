import os
from mlProject import logger 
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config



    
   # Note:
# You can add different data transformation techniques such as scaling, PCA, feature engineering, etc.
# You can also perform EDA steps in the ML lifecycle here before passing data to the model.

# For now, I am only performing train-test splitting because the dataset is already cleaned.

# In future improvements, we can enhance this stage with feature scaling, encoding, and dimensionality reduction.




    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        #split the data into training and test sets (0.75, 0.25)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)



        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)



    