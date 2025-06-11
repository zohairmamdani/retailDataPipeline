from ingestion.ingestData import ingestData
from transform.transformData import transformData

def run_pipeline():
    print("Starting data pipeline")
    ingestData()
    transformData()
    print("Pipeline completed successfully.")

if __name__ == '__main__':
    run_pipeline()