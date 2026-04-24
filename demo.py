from mlProject import logger
from mlProject.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline 
from mlProject.pipeline.stage_02_data_validation import DataValidionTrainingPipeline


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