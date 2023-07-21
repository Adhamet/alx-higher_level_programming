-- Creates database hbtn_0d_usa & table cities.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` ( 
    PRIMARY KEY(`id`),
    `id`       INT          unique    auto_generated,
    `state_id` INT          not NULL,
    `name`     VARCHAR(256) not NULL,
    FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
