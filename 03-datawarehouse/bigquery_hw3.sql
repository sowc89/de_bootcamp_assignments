// Create external tables in BigQuery

CREATE OR REPLACE EXTERNAL TABLE `kestra-gcp-485922.hw3datawarehouse.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://sow_dezoomcamp_hw3_2025/yellow_tripdata_2024-*.parquet']
);

// Create non-partitioned table

CREATE OR REPLACE TABLE `kestra-gcp-485922.hw3datawarehouse.yellow_tripdata_non_partitioned` AS
SELECT * FROM `kestra-gcp-485922.hw3datawarehouse.external_yellow_tripdata`;



//Q3: Understanding columnar storage - bytes processed comparision 
select e1.PULocationID from `hw3datawarehouse.yellow_tripdata_non_partitioned` e1 

select e1.PULocationID, e1.DOLocationID from `hw3datawarehouse.yellow_tripdata_non_partitioned` e1 



//Q5 : Create partitioned table
CREATE OR REPLACE TABLE `kestra-gcp-485922.hw3datawarehouse.yellow_tripdata_partitioned`
PARTITION BY
  DATE(tpep_dropoff_datetime) 
CLUSTER BY VendorID 
  AS
SELECT * FROM `kestra-gcp-485922.hw3datawarehouse.external_yellow_tripdata`;


//Q6: Distinct vendor IDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15
select distinct VendorID from `hw3datawarehouse.yellow_tripdata_non_partitioned` where tpep_dropoff_datetime between '2024-03-01' and '2024-03-15'
select distinct VendorID from `hw3datawarehouse.yellow_tripdata_partitioned` where tpep_dropoff_datetime between '2024-03-01' and '2024-03-15'