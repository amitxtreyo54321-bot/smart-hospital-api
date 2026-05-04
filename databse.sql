CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
SHOW TABLES;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(100),
    admitted_date DATE
);
SHOW TABLES;

CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(20),
    room_type VARCHAR(50),
    status VARCHAR(20)
);
SHOW TABLES;

CREATE TABLE admissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    room_id INT,
    admission_date DATE,
    discharge_date DATE,

    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
SHOW TABLES;


CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    heart_rate INT,
    temperature FLOAT,
    oxygen_level INT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (patient_id) REFERENCES patients(id)
);
SHOW TABLES;


CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    alert_message VARCHAR(255),
    alert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (patient_id) REFERENCES patients(id)
);
SHOW TABLES;


CREATE TABLE medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    medicine_name VARCHAR(100),
    dosage VARCHAR(50),
    prescribed_by INT,

    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (prescribed_by) REFERENCES doctors(id)
);
SHOW TABLES;

CREATE TABLE beds (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,
    bed_number VARCHAR(10),
    status VARCHAR(20),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
SHOW TABLES;

CREATE TABLE emergency_alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    message VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SHOW TABLES;






