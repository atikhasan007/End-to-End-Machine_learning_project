from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
import os
from mlProject import logger




STAGE_NAME = "Data validation stage"

class DataValidionTrainingPipeline:
    def __init_(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validation_all_columns()


if __name__=="__main__": # read only
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj = DataValidionTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e