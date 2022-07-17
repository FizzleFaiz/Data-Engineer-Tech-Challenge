BEGIN

CREATE TABLE [IF NOT EXISTS] my_database.sales_trans (
   sales_id int NOT NULL,
   cust_name varchar(255)  NOT NULL,
   cust_phone varchar(30)  NOT NULL,
   cust_salesman_id int NOT NULL,
   car_manu varchar(255)  NOT NULL,
   car_model varchar(255)  NOT NULL ,
   car_serial varchar(255)  NOT NULL,
   car_weight decimal(17,2) NOT NULL, 
   car_price decimal(17,2)  NOT NULL,
   sales_ts timestamp,
   PRIMARY KEY (sales_id),
   FOREIGN KEY (cust_salesman_id)
    REFERENCES (my_database.salesperson.cust_salesman_id)
);

CREATE TABLE [IF NOT EXISTS] my_database.car (
   car_manu varchar(255)  NOT NULL,
   car_model varchar(255)  NOT NULL ,
   car_serial varchar(255)  NOT NULL,
   car_weight decimal(17,2) NOT NULL, 
   car_price decimal(17,2)  NOT NULL
);

CREATE TABLE [IF NOT EXISTS] my_database.salesperson (
   cust_salesman_id int NOT NULL,
   cust_salesman_name varchar(255)  NOT NULL ,
   cust_salesman_phone varchar(30)  NOT NULL,
   PRIMARY KEY (cust_salesman_id)
);


END