-- Creates table hbtn_0d_usa with table states.
CREATE DATABASE if NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE if NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);
