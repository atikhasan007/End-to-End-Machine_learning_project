from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
import os
from mlProject import logger




STAGE_NAME = "Data Evaluatio stage"

class ModelEvaluationTrainingPipeline:
    def __init_(self):
        pass

    def main(self):
        config = ConfigurationManager()
        
        model_eval_config = config.get_model_evaluation_config()
            
        model_evaluation = ModelEvaluation(config=model_eval_config)
            
        model_evaluation.save_result()


if __name__=="__main__": # read only
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e