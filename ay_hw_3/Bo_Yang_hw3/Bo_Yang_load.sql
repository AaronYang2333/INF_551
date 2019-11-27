DROP DATABASE IF EXISTS inf551;
CREATE DATABASE IF NOT EXISTS inf551;

use inf551;

drop table if exists inspections;
drop table if exists violations;

CREATE TABLE inspections (
  serial_number varchar(255) DEFAULT NULL,
  activity_date date DEFAULT NULL,
  facility_name varchar(255) DEFAULT NULL,
  score varchar(255) DEFAULT NULL,
  grade varchar(255) DEFAULT NULL,
  service_code varchar(255) DEFAULT NULL,
  service_description varchar(255) DEFAULT NULL,
  employee_id varchar(255) DEFAULT NULL,
  facility_address varchar(255) DEFAULT NULL,
  facility_city varchar(255) DEFAULT NULL,
  facility_id varchar(255) DEFAULT NULL,
  facility_state varchar(255) DEFAULT NULL,
  facility_zip varchar(255) DEFAULT NULL,
  owner_id varchar(255) DEFAULT NULL,
  owner_name varchar(255) DEFAULT NULL,
  pe_description varchar(255) DEFAULT NULL,
  program_element_pe varchar(255) DEFAULT NULL,
  program_name varchar(255) DEFAULT NULL,
  program_status varchar(255) DEFAULT NULL,
  record_id varchar(255) DEFAULT NULL
);

CREATE TABLE violations (
  serial_number varchar(255) DEFAULT NULL,
  activity_date date DEFAULT NULL,
  facility_name varchar(255) DEFAULT NULL,
  violation_code varchar(255) DEFAULT NULL,
  violation_description varchar(255) DEFAULT NULL,
  violation_status varchar(255) DEFAULT NULL,
  points varchar(255) DEFAULT NULL,
  grade varchar(255) DEFAULT NULL,
  facility_address varchar(255) DEFAULT NULL,
  facility_city varchar(255) DEFAULT NULL,
  facility_id varchar(255) DEFAULT NULL,
  facility_state varchar(255) DEFAULT NULL,
  facility_zip varchar(255) DEFAULT NULL,
  employee_id varchar(255) DEFAULT NULL,
  owner_id varchar(255) DEFAULT NULL,
  owner_name varchar(255) DEFAULT NULL,
  pe_description varchar(255) DEFAULT NULL,
  program_element_pe varchar(255) DEFAULT NULL,
  program_name varchar(255) DEFAULT NULL,
  program_status varchar(255) DEFAULT NULL,
  record_id varchar(255) DEFAULT NULL,
  score varchar(255) DEFAULT NULL,
  service_code varchar(255) DEFAULT NULL,
  service_description varchar(255) DEFAULT NULL,
  row_id varchar(255) DEFAULT NULL
);

LOAD DATA LOCAL INFILE './inspections.csv' 
INTO TABLE inspections 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE './violations.csv' 
INTO TABLE violations 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;