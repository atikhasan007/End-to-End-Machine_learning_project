

from mlProject.config.configuration import ConfigurationManager
from mlProject import logger
from mlProject.components.model_trainer import ModelTrainer




STAGE_NAME = "Data trainer stage"

class ModelTrainerTrainingPipeline:
    def __init_(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__=="__main__": # read only
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e