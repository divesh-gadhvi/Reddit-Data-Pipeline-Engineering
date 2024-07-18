# Reddit Data Pipeline Engineering

This project showcases the integration of multiple technologies to create a seamless ETL (Extract, Transform, Load) process for Reddit data. The project leverages Apache Airflow, Celery, Postgres, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift to build a robust data pipeline.

## Key Features

### Data Extraction
**Extract Data from Reddit**: Implement data extraction from Reddit using its API. The pipeline captures posts, comments, and other metadata to enable comprehensive analysis.

### ETL Orchestration
**Apache Airflow & Celery**: Utilize Apache Airflow for orchestrating ETL workflows and Celery for managing asynchronous tasks, ensuring efficient scheduling and execution of data processing tasks.

### Data Storage
**Amazon S3**: Store extracted data efficiently in Amazon S3, integrated seamlessly with Airflow to manage and organize data storage.

### Data Transformation
**AWS Glue**: Leverage AWS Glue for data cataloging and ETL jobs, transforming raw Reddit data into a structured format suitable for analysis and querying.

### Data Querying
**Amazon Athena**: Use Amazon Athena for querying and transforming the structured data with SQL, enabling quick and powerful data exploration.

### Data Warehousing
**Amazon Redshift**: Set up an Amazon Redshift cluster as a data warehouse, adhering to best practices for loading and managing data to facilitate advanced analytics.

## Steps Followed

1. **Setting up Apache Airflow**: 
   - Configured Apache Airflow with a Celery backend and Postgres for metadata storage.
   - Set up DAGs (Directed Acyclic Graphs) to define the ETL workflow.

2. **Reddit Data Pipeline**:
   - Implemented data extraction pipelines in Airflow to fetch data from the Reddit API.
   - Ensured data integrity and consistency during extraction.

3. **Data Cleaning and Transformation**:
   - Applied data cleaning techniques to handle missing or corrupted data.
   - Transformed data into a normalized format for better usability.

4. **Connecting to AWS**:
   - Established secure connections from Airflow to various AWS services like S3, Glue, Athena, and Redshift.

5. **AWS Glue Data Transformation**:
   - Used AWS Glue for complex data transformations and to create a data catalog for easy data access.

6. **Querying Data with Athena**:
   - Queried the transformed data using Amazon Athena to validate the transformation process and gain initial insights.

7. **Setting up Redshift Data Warehouse**:
   - Configured an Amazon Redshift cluster, optimized for performance.
   - Set up schemas and tables in Redshift for storing the processed data.

8. **Redshift Data Warehouse Query Tool**:
   - Implemented tools for querying and managing data within the Redshift data warehouse.

9. **Loading Data into Data Warehouse**:
   - Loaded the cleaned and transformed data into Redshift using COPY commands and optimized loading strategies.

10. **Charting with Redshift**:
    - Created visualizations using data stored in Redshift to derive meaningful insights.

## Technology Stack

### Languages
- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white): Python is used for scripting ETL processes, data extraction, transformation, and orchestration.

### Data Extraction and Orchestration
- ![Apache Airflow](https://img.shields.io/badge/-Apache_Airflow-017CEE?style=flat&logo=apache-airflow&logoColor=white): Apache Airflow is used to schedule and manage the ETL workflows.  
- ![Celery](https://img.shields.io/badge/-Celery-37814A?style=flat&logo=celery&logoColor=white): Celery handles the asynchronous task queue for background processing in ETL.

### Data Storage and Processing
- ![Postgres](https://img.shields.io/badge/-Postgres-4169E1?style=flat&logo=postgresql&logoColor=white): Postgres is used as the metadata database for Airflow.  
- ![Amazon S3](https://img.shields.io/badge/-Amazon_S3-569A31?style=flat&logo=amazon-s3&logoColor=white): Amazon S3 provides scalable storage for the extracted and transformed data.  
- ![AWS Glue](https://img.shields.io/badge/-AWS_Glue-FF9900?style=flat&logo=amazon-aws&logoColor=white): AWS Glue is used for data cataloging and ETL transformations.  
- ![Amazon Athena](https://img.shields.io/badge/-Amazon_Athena-232F3E?style=flat&logo=amazon-athena&logoColor=white): Amazon Athena allows querying data stored in S3 using standard SQL.  
- ![Amazon Redshift](https://img.shields.io/badge/-Amazon_Redshift-232F3E?style=flat&logo=amazon-redshift&logoColor=white): Amazon Redshift serves as the data warehouse for scalable and performant analytics.

### APIs
- ![Reddit API](https://img.shields.io/badge/-Reddit_API-FF4500?style=flat&logo=reddit&logoColor=white): Reddit API is used to extract data from Reddit, including posts, comments, and metadata.

### IDEs
- ![VS Code](https://img.shields.io/badge/-VS_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white): Visual Studio Code is used for code development and debugging.  

## Conclusion

The "Reddit Data Pipeline Engineering" project is an effort to create an efficient and robust ETL pipeline leveraging modern technologies. This project demonstrates full-stack development skills and the ability to handle data processing and analytics. It provides a comprehensive guide for integrating various tools and frameworks to build a scalable data pipeline.
