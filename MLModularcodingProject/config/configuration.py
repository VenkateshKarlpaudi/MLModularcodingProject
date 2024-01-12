from MLModularcodingProject.constants import *
import os, sys


ROOT_DIR = ROOT_DIR_KEY

#Dataset_url = 


DATASET_PATH = os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY)

# C:\Users\venky\Desktop\SkillSplash\Project_template\MLModularcodingProject\Data

RAW_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP, DATA_INGESTION_RAW_DATA_DIR,
                             RAW_DATA_DIR_KEY)

TRAIN_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP, DATA_INGESTION_INGESTED_DATA_DIR_KEY,
                             TRAIN_DATA_DIR_KEY)

TEST_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP, DATA_INGESTION_INGESTED_DATA_DIR_KEY,
                             TEST_DATA_DIR_KEY)
