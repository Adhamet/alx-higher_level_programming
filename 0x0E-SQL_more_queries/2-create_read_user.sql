-- Creates the database hbtn_0d_2 and the user user_0d_2
CREATE database if NOT EXISTS hbtn_0d_2;
CREATE user if NOT EXISTS user_0d_2@localhost IDENTIFIED BY `user_0d_2_pwd`;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost
