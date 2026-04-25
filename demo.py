from mlProject import logger
from mlProject.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline 
from mlProject.pipeline.stage_02_data_validation import DataValidionTrainingPipeline
from mlProject.pipeline.state_03_data_transformatoin import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data validaion stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = DataValidionTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformaton stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e