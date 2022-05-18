CREATE DATABASE IF NOT EXISTS Musical_instruments_store DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE Musical_instruments_store;

DELIMITER $$

DROP PROCEDURE IF EXISTS INSERT_ORDER_LIST$$
CREATE PROCEDURE INSERT_ORDER_LIST (IN user_id BIGINT(20), IN title varchar(255) CHARSET utf8, IN status_id BIGINT(20), IN closed BOOLEAN)  BEGIN

INSERT INTO order_list(user_id, title, status_id, closed) 
VALUES (user_id, title, status_id, closed);

END$$

DROP PROCEDURE IF EXISTS INSERT_USER_LIST$$
CREATE PROCEDURE INSERT_USER_LIST (IN login varchar(255), IN first_name varchar(255), IN last_name varchar(255), IN email varchar(255), IN phone CHAR(13), IN password varchar(255), IN enabled BOOLEAN)  BEGIN

INSERT INTO user_list (login, first_name, last_name, email, phone, password, enabled) 
VALUES (login, first_name, last_name, email, phone, password, enabled);

END$$

DROP PROCEDURE IF EXISTS INSERT_INSTRUMENT_LIST$$
CREATE PROCEDURE INSERT_INSTRUMENT_LIST (IN description VARCHAR(255), IN title varchar(255), IN status_id BIGINT(20), IN price DECIMAL(17, 2), IN closed BOOLEAN)  BEGIN

INSERT INTO instrument_list (description, title, status_id, price, closed) 
VALUES (description, title, status_id, price, closed);

END$$

DROP PROCEDURE IF EXISTS INSERT_INSTRUMENT_ORDER$$
CREATE PROCEDURE INSERT_INSTRUMENT_ORDER (IN price decimal(17, 2), IN quantity TINYINT(30))  BEGIN

INSERT INTO instrument_order (price, quantity) 
VALUES (price, quantity);

END$$

DROP PROCEDURE IF EXISTS INSERT_ORDER_HISTORY$$
CREATE PROCEDURE INSERT_ORDER_HISTORY (IN user_id BIGINT(20), IN total_sum DECIMAL(17, 2), IN title varchar(255), IN rating BIGINT, IN status_id BIGINT)  BEGIN

INSERT INTO order_history(user_id, total_sum, title, rating, status_id) 
VALUES (user_id, total_sum, title, rating, status_id);

END$$

DROP PROCEDURE IF EXISTS UPDATE_USER_LIST$$
CREATE PROCEDURE UPDATE_USER_LIST (IN uid bigint(20), logi varchar(255), IN first_nam varchar(255), IN last_nam varchar(255), IN emai varchar(255), IN phon CHAR(13), IN passwor varchar(255))  BEGIN

UPDATE user_list
	SET login = logi, first_name= first_nam, last_name = last_nam, email = emai, phone = phon, password = passwor
	WHERE user_id = uid;

END$$

DROP PROCEDURE IF EXISTS UPDATE_INSTRUMENT_LIST$$
CREATE PROCEDURE UPDATE_INSTRUMENT_LIST (IN iid bigint(20), IN descriptio VARCHAR(255), IN titl varchar(255), IN sid BIGINT(20), IN pric DECIMAL(17, 2), IN close BOOLEAN)  BEGIN

UPDATE instrument_list 
	SET description = descriptio, title = titl, status_id = sid, price = pric, closed = close
	WHERE instrument_id = iid;

END$$

DROP PROCEDURE IF EXISTS UPDATE_INSTRUMENT_ORDER$$
CREATE PROCEDURE UPDATE_INSTRUMENT_ORDER (IN oid bigint(20), IN iid bigint(20), IN pric decimal(17, 2), IN quantit TINYINT(30))  BEGIN
UPDATE instrument_order 
	SET price = pric, quantity = quantit 
    WHERE order_id = oid and instrument_id = iid;

END$$

DROP PROCEDURE IF EXISTS DELETE_ORDER_LIST$$
CREATE PROCEDURE DELETE_ORDER_LIST (IN oid bigint(20))  BEGIN

DELETE FROM order_list WHERE order_id = oid;

END$$

DROP PROCEDURE IF EXISTS DELETE_USER_LIST$$
CREATE PROCEDURE DELETE_USER_LIST (IN id bigint(20))  BEGIN

DELETE FROM Musical_instruments_store.user_list
WHERE user_id = id;

END$$

DROP PROCEDURE IF EXISTS DELETE_INSTRUMENT_LIST$$
CREATE PROCEDURE DELETE_INSTRUMENT_LIST (IN iid varchar(255))  BEGIN

DELETE FROM instrument_list WHERE instrument_id = iid;

END$$

DROP PROCEDURE IF EXISTS DELETE_INSTRUMENT_ORDER$$
CREATE PROCEDURE DELETE_INSTRUMENT_ORDER (IN oid bigint(20), IN iid bigint(20))  BEGIN

DELETE FROM instrument_order WHERE order_id = oid and instrument_id = iid;

END$$

DROP FUNCTION IF EXISTS FUNC_COUNT_RATING$$
CREATE FUNCTION FUNC_COUNT_RATING(rating bigint)
RETURNS BIGINT UNSIGNED DETERMINISTIC
BEGIN

	DECLARE rat BIGINT UNSIGNED default 0;
    SELECT count(*) into rat
		from order_history
        where rating = rat;
	RETURN rat;
    
END$$

DELIMITER ;

DROP TABLE IF EXISTS user_list;
CREATE TABLE IF NOT EXISTS user_list (
	user_id 		bigint(20) 		unsigned 	NOT NULL AUTO_INCREMENT,
	login 			varchar(255) 	NOT NULL,
	first_name 		varchar(255) 	NOT NULL,
    last_name 		varchar(255) 	NOT NULL,
    email 			varchar(255) 	NOT NULL,
    phone 			char(13) 		NOT NULL,
    password 		varchar(255) 	NOT NULL,
    enabled 		tinyint(1) 		NOT NULL 	DEFAULT 1,
    date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
    date_modified 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY 		user_list_idx1 	(login),
    UNIQUE KEY 		user_list_idx2 	(email),
    UNIQUE KEY 		user_list_idx3 	(phone),
    CONSTRAINT		pk_user_list 	PRIMARY KEY (user_id)
);

DROP TRIGGER IF EXISTS IN_TRIM_USER_LIST;
DELIMITER $$
CREATE TRIGGER IN_TRIM_USER_LIST BEFORE INSERT ON user_list FOR EACH ROW BEGIN

SET NEW.login = TRIM(NEW.login);   
SET NEW.first_name = TRIM(NEW.first_name);   
SET NEW.last_name = TRIM(NEW.last_name);   
SET NEW.email = TRIM(NEW.email);   
SET NEW.phone = TRIM(NEW.phone);   

END
$$

DELIMITER ;

DROP TRIGGER IF EXISTS UP_TRIM_USER_LIST;
DELIMITER $$
CREATE TRIGGER UP_TRIM_USER_LIST BEFORE UPDATE ON user_list FOR EACH ROW BEGIN

SET NEW.login = TRIM(NEW.login);   
SET NEW.first_name = TRIM(NEW.first_name);   
SET NEW.last_name = TRIM(NEW.last_name);   
SET NEW.email = TRIM(NEW.email);   
SET NEW.phone = TRIM(NEW.phone);   

END
$$

DELIMITER ;

DROP TABLE IF EXISTS role;
CREATE TABLE IF NOT EXISTS role (
	role_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	code 			varchar(255) 	NOT NULL,
	name 			varchar(255) 	NOT NULL,
    UNIQUE KEY 		role_idx1 		(name),
    UNIQUE KEY 		role_idx2 		(code),
    CONSTRAINT		pk_role 		PRIMARY KEY (role_id)
);

DROP TABLE IF EXISTS user_role;
CREATE TABLE IF NOT EXISTS user_role (
	user_id 		bigint(20) 		unsigned 	NOT NULL,
	role_id 		bigint(20) 		unsigned 	NOT NULL,
    CONSTRAINT 		pk_user_role PRIMARY KEY (user_id, role_id),
	CONSTRAINT 		fk_user_role_user_list FOREIGN KEY (user_id) references user_list(user_id),
	CONSTRAINT 		fk_user_role_role FOREIGN KEY (role_id) references role(role_id)
);

DROP TABLE IF EXISTS status;
CREATE TABLE IF NOT EXISTS status (
	status_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
    code 			varchar(255) 	NOT NULL,
    name 			varchar(255) 	NOT NULL,
    closed 			BOOLEAN 		NOT NULL DEFAULT 1,
    UNIQUE KEY 		status_idx1 	(name),
    UNIQUE KEY 		status_idx2 	(code),
    CONSTRAINT 		pk_status 		PRIMARY KEY (status_id)
);

DROP TABLE IF EXISTS next_status;
CREATE TABLE IF NOT EXISTS next_status (
    status_id 		bigint(20) 		unsigned NOT NULL,
    next_status_id 	bigint(20) 		unsigned NOT NULL,
    CONSTRAINT 		fk_next_status_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT 		fk_next_status_status1 FOREIGN KEY (next_status_id) references status(status_id)
);

DROP TABLE IF EXISTS order_history;
CREATE TABLE IF NOT EXISTS order_history (
	history_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
	user_id  		bigint(20) 		unsigned 	NOT NULL,
	total_sum 		DECIMAL(17, 2) 	NOT NULL DEFAULT 0,
	title 			varchar(255) 	NOT NULL,
	rating			bigint(20) 		unsigned 	NOT NULL,
	status_id 		bigint(20) 		unsigned 	NOT NULL,
	CONSTRAINT 		fk_order_history_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT 		fk_order_history_user FOREIGN KEY (user_id) references user_list(user_id),
    CONSTRAINT		pk_order_history 	PRIMARY KEY (history_id)
);

DROP TABLE IF EXISTS instrument_list;
CREATE TABLE IF NOT EXISTS instrument_list (
	instrument_id 	bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
	date_updated 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	description 	varchar(255) 	NOT NULL,
	title 			varchar(255) 	NOT NULL,
	status_id 		bigint(20) 		unsigned NOT NULL,
    price 			DECIMAL(17, 2) 	NOT NULL DEFAULT 0,
	closed 			BOOLEAN 		NOT NULL 	DEFAULT 1,
    UNIQUE KEY 		instrument_list_idx1 	(title),
    UNIQUE KEY 		instrument_list_idx2 	(description),
	CONSTRAINT 		fk_instrument_list_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT		pk_instrument_list 	PRIMARY KEY (instrument_id)
);

DROP TABLE IF EXISTS order_list;
CREATE TABLE IF NOT EXISTS order_list (
	order_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
	user_id 		bigint(20) 		unsigned NOT NULL ,
	title 			varchar(255) 	NOT NULL,
	status_id 		bigint(20) 		unsigned NOT NULL ,
	closed 			BOOLEAN 		NOT NULL 	DEFAULT 1,
    CONSTRAINT 		fk_order_list_user_list FOREIGN KEY (user_id) references user_list(user_id),
    CONSTRAINT 		fk_order_list_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT		pk_order_list 	PRIMARY KEY (order_id)
);

DROP TABLE IF EXISTS instrument_order;
CREATE TABLE IF NOT EXISTS instrument_order (
	instrument_id 	bigint(20) 		unsigned NOT NULL ,
	order_id 		bigint(20) 		unsigned NOT NULL ,
	price 			DECIMAL(17, 2) 	NOT NULL DEFAULT 0,
	quantity 		TINYINT(30) 	NOT NULL DEFAULT 0,
	CONSTRAINT 		fk_instrument_order_instrument_list FOREIGN KEY (instrument_id) references instrument_list(instrument_id),
	CONSTRAINT 		fk_instrument_order_order_list FOREIGN KEY (order_id) references order_list(order_id),
    CONSTRAINT		pk_instrument_order 	PRIMARY KEY (instrument_id, order_id)
);
