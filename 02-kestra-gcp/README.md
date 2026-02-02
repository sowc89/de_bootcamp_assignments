# Kestra Environment Setup

This directory contains the Docker Compose setup for Kestra, an orchestration and scheduling platform, along with PostgreSQL and PgAdmin, for homework 2. 


## GCP Setup:

In the Google cloud console, create a new project, create a service account and download the JSON key file. 

The JSON key file should be encoded. The follwoing command is used to encode the JSON key file (Windows Powershell):

```bash
$jsonContent = Get-Content -Path ".\kestra-gcp-485922-4f5823db0b71.json" -Raw
$base64String = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($jsonContent))
Set-Content -Path ".env_encoded" -Value "SECRET_GCP_SERVICE_ACCOUNT=$base64String"
```

The encoded JSON key file should be placed in the same directory as the docker-compose.yml file. The env configuration is added to the docker-compose.yml file under kestra service. 

```yaml
env_file: .env_encoded
```

Now, once kestra is up, the secret can be accessed in a flow using the following code:

```yaml
serviceAccount: "{{secret('GCP_SERVICE_ACCOUNT')}}"
```

## Starting the services

1.  Navigate to this directory:
    ```bash
    cd 02-kestra-gcp
    ```

2.  Start the services using Docker Compose:
    ```bash
   docker compose -p kestra-gcp up -d
    ```

3. Access the Kestra UI at [http://localhost:8080](http://localhost:8080).


## Setting up the GCP Key Value pairs:

4. Setup the GCP Key Value pairs in Kestra UI using the gcp_kv.yaml flow in the flow directory.

5. The taxi data is processed using the kestra-gcp-scheduled.yaml flow in the flow directory.

##Assignment Answers: 

1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)? Refer image: q1.png

 > 134.5 MiB

2. What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

 > green_tripdata_2020-04.csv

3.  How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

 > 24648499

Execute the Kestra flow for all the months of 2020 in the yellow taxi dataand count the number of rows using the following query:

 ```bash
SELECT SUM(d) from

((SELECT count(*) as d FROM `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_01` k1
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_02` k2
union all
SELECT count(*) FROM `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_03` k3
union all
SELECT count(*) FROM `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_04` k4
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_05` k5
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_06` k6
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_07` k7
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_08` k8
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_09` k9
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_10` k10
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_11` k11
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.yellow_tripdata_2020_12` k12) )
as  CombinedCounts
```

4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?

> Answer: 1734051

Execute the Kestra flow for all the months of 2020 in the green taxi data and count the number of rows using the following query:

```bash
SELECT SUM(d) from

((SELECT count(*) as d FROM `kestra-gcp-485922.zoomcamp.green_tripdata_2020_01` k1
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_02` k2
union all
SELECT count(*) FROM `kestra-gcp-485922.zoomcamp.green_tripdata_2020_03` k3
union all
SELECT count(*) FROM `kestra-gcp-485922.zoomcamp.green_tripdata_2020_04` k4
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_05` k5
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_06` k6
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_07` k7
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_08` k8
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_09` k9
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_10` k10
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_11` k11
union all
SELECT count(*) FROM  `kestra-gcp-485922.zoomcamp.green_tripdata_2020_12` k12) )
as  CombinedCounts
```

5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file? Refer image: q5.png

> Answer: 1925152

6. How would you configure the timezone to New York in a Schedule trigger? Refer: kestra-gcp-scheduled.yaml 

> Answer: Add a timezone property set to America/New_York in the Schedule trigger configurationv