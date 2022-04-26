DEBUG = False
METHOD_NAME = "levirank_baseline"
INPUT_FILE_NAME = "topics.xml"
OUTPUT_FILE_NAME = "run.txt"
TEST_TITLES_FILE_LOCATION = "./data/topics.xml"
CORPUS_JSONL_FILE_LOCATION = "./data/touche-task2-passages-version-002.jsonl"
CORPUS_PICKLE_FILE_LOCATION = "./data/corpus.pkl"
INDEX_FILE_LOCATION = "./data/index"
PRINT_STATUS_UPDATE_SPEED = 100
DUO_T5_COVERAGE = 30
INITIAL_RETRIEVAL_AMOUNT = 1375
STANCE_MODEL_N_PATH = "./data/neutral_no_object_classifier"
STANCE_MODEL_S_PATH = "./data/object1_object2_classifier"
LABELS = ("NO", "NEUTRAL", "FIRST", "SECOND")
