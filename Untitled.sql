CREATE DATABASE IF NOT EXISTS Musical_instruments_store DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE Musical_instruments_store;

DELIMITER $$

DROP PROCEDURE IF EXISTS INSERT_ORDER_LIST$$
CREATE DEFINER=root@localhost PROCEDURE INSERT_ORDER_LIST (IN user_id BIGINT(20), IN title VARCHAR(50) CHARSET utf8, IN status_id BIGINT(20), IN closed BOOLEAN, OUT nid BIGINT(20) UNSIGNED)  BEGIN

INSERT INTO order_list(user_id, title, status_id, closed) 
VALUES (user_id, title, status_id, closed);

SELECT LAST_INSERT_ID() into nid;

END$$

DROP PROCEDURE IF EXISTS INSERT_USER_LIST$$
CREATE DEFINER=root@localhost PROCEDURE INSERT_USER_LIST (IN login VARCHAR(50) CHARSET utf8, IN first_name VARCHAR(50) CHARSET utf8, IN last_name VARCHAR(50) CHARSET utf8, IN email VARCHAR(50) CHARSET utf8, IN phone CHAR(13) CHARSET utf8, IN password VARCHAR(64) CHARSET utf8, IN enabled TINYINT(1))  BEGIN

INSERT INTO user_list (login, first_name, last_name, email, phone, password, enabled) 
VALUES (login, first_name, last_name, email, phone, password, enabled);

END$$

DROP PROCEDURE IF EXISTS INSERT_INSTRUMENT_LIST$$
CREATE DEFINER=root@localhost PROCEDURE INSERT_INSTRUMENT_LIST (IN description VARCHAR(255) CHARSET utf8, IN title VARCHAR(50) CHARSET utf8, IN status_id BIGINT(20), IN price DECIMAL(17, 2), IN closed BOOLEAN, OUT nid BIGINT(20) UNSIGNED)  BEGIN
INSERT INTO instrument_list (description, title, status_id, price, closed) 
VALUES (description, title, status_id, price, closed);

SELECT LAST_INSERT_ID() into nid;

END$$

DROP PROCEDURE IF EXISTS INSERT_INSTRUMENT_ORDER$$
CREATE DEFINER=root@localhost PROCEDURE INSERT_INSTRUMENT_ORDER (IN price decimal(17, 2), IN quantity TINYINT(30), OUT nid BIGINT(20) UNSIGNED)  BEGIN
INSERT INTO instrument_order (price, quantity) 
VALUES (price, quantity);

SELECT LAST_INSERT_ID() into nid;

END$$

DROP PROCEDURE IF EXISTS INSERT_ORDER_HISTORY$$
CREATE DEFINER=root@localhost PROCEDURE INSERT_ORDER_HISTORY (IN user_id BIGINT(20), IN total_sum DECIMAL(17, 2), IN title VARCHAR(50), IN rating BIGINT, IN status_id BIGINT, OUT nid BIGINT(20) UNSIGNED)  BEGIN

INSERT INTO order_history(user_id, total_sum, title, rating, status_id) 
VALUES (user_id, total_sum, title, rating, status_id);

SELECT LAST_INSERT_ID() into nid;

END$$

DROP PROCEDURE IF EXISTS UPDATE_USER_LIST$$
CREATE DEFINER=root@localhost PROCEDURE UPDATE_USER_LIST (IN user_id bigint(20), login VARCHAR(50) CHARSET utf8, IN first_name VARCHAR(50) CHARSET utf8, IN last_name VARCHAR(50) CHARSET utf8, IN email VARCHAR(50) CHARSET utf8, IN phone CHAR(13) CHARSET utf8, IN password VARCHAR(64) CHARSET utf8)  BEGIN
UPDATE user_list
	SET login = login, first_name= first_name, last_name = last_name, email = email, phone = phone, password = password
	WHERE user_id = user_id;

END$$

DROP PROCEDURE IF EXISTS UPDATE_INSTRUMENT_LIST$$
CREATE DEFINER=root@localhost PROCEDURE UPDATE_INSTRUMENT_LIST (IN instrument_id bigint(20), IN description VARCHAR(255) CHARSET utf8, IN title VARCHAR(50) CHARSET utf8, IN status_id BIGINT(20), IN price DECIMAL(17, 2), IN closed BOOLEAN)  BEGIN
UPDATE instrument_list 
	SET description = description, title = title, status_id = status_id, price = price, closed = closed
	WHERE instrument_id = instrument_id;

END$$

DROP PROCEDURE IF EXISTS UPDATE_INSTRUMENT_ORDER$$
CREATE DEFINER=root@localhost PROCEDURE UPDATE_INSTRUMENT_ORDER (IN order_id bigint(20), IN instrument_id bigint(20), IN price decimal(17, 2), IN quantity TINYINT(30))  BEGIN
UPDATE instrument_order 
	SET price = price, quantity = quantity 
    WHERE order_id = order_id and instrument_id = instrument_id;

END$$

DROP PROCEDURE IF EXISTS DELETE_ORDER_LIST$$
CREATE DEFINER=root@localhost PROCEDURE DELETE_ORDER_LIST (IN order_id bigint(20))  BEGIN

DELETE FROM order_list WHERE order_id = order_id;

END$$

DROP PROCEDURE IF EXISTS DELETE_USER_LIST$$
CREATE DEFINER=root@localhost PROCEDURE DELETE_USER_LIST (IN login VARCHAR(50) CHARSET utf8)  BEGIN

DELETE FROM user_list WHERE login = login;

END$$

DROP PROCEDURE IF EXISTS DELETE_INSTRUMENT_LIST$$
CREATE DEFINER=root@localhost PROCEDURE DELETE_INSTRUMENT_LIST (IN title VARCHAR(50) CHARSET utf8)  BEGIN

DELETE FROM instrument_list WHERE title = title;

END$$

DROP PROCEDURE IF EXISTS DELETE_INSTRUMENT_ORDER$$
CREATE DEFINER=root@localhost PROCEDURE DELETE_INSTRUMENT_ORDER (IN order_id bigint(20), IN instrument_id bigint(20))  BEGIN

DELETE FROM instrument_order WHERE order_id = order_id and instrument_id = instrument_id;

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
	login 			varchar(50) 	COLLATE 	utf8_unicode_ci NOT NULL,
	first_name 		varchar(50) 	COLLATE 	utf8_unicode_ci NOT NULL,
    last_name 		varchar(50) 	COLLATE 	utf8_unicode_ci NOT NULL,
    email 			varchar(50) 	COLLATE 	utf8_unicode_ci NOT NULL,
    phone 			char(13) 		COLLATE 	utf8_unicode_ci NOT NULL,
    password 		varchar(64) 	COLLATE 	utf8_unicode_ci NOT NULL,
    enabled 		tinyint(1) 		NOT NULL 	DEFAULT '1',
    date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
    date_modified 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY 		user_list_idx1 	(login),
    UNIQUE KEY 		user_list_idx2 	(email),
    UNIQUE KEY 		user_list_idx3 	(phone),
    CONSTRAINT		pk_user_list 	PRIMARY KEY (user_id)
) ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS role;
CREATE TABLE IF NOT EXISTS role (
	role_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	code 			varchar(255) 	COLLATE utf8_unicode_ci NOT NULL,
	name 			varchar(255) 	COLLATE utf8_unicode_ci NOT NULL,
    UNIQUE KEY 		role_idx1 	(name),
    UNIQUE KEY 		role_idx2 	(code),
    CONSTRAINT		pk_role 		PRIMARY KEY (role_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS user_role;
CREATE TABLE IF NOT EXISTS user_role (
	user_id 		bigint(20) 		unsigned 	NOT NULL,
	role_id 		bigint(20) 		unsigned 	NOT NULL,
    CONSTRAINT 		pk_user_role PRIMARY KEY (user_id, role_id),
	CONSTRAINT 		fk_user_role_user_list FOREIGN KEY (user_id) references user_list(user_id),
	CONSTRAINT 		fk_user_role_role FOREIGN KEY (role_id) references role(role_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS status;
CREATE TABLE IF NOT EXISTS status (
	status_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
    code 			varchar(255) 	COLLATE utf8_unicode_ci NOT NULL,
    name 			varchar(255) 	COLLATE utf8_unicode_ci NOT NULL,
    closed 			tinyint(1) 		NOT NULL DEFAULT '1',
    UNIQUE KEY 		status_idx1 	(name),
    UNIQUE KEY 		status_idx2 	(code),
    CONSTRAINT 		pk_status 		PRIMARY KEY (status_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS next_status;
CREATE TABLE IF NOT EXISTS next_status (
    status_id 		bigint(20) 		unsigned NOT NULL,
    next_status_id 	bigint(20) 		unsigned NOT NULL,
    CONSTRAINT 		fk_next_status_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT 		fk_next_status_status1 FOREIGN KEY (next_status_id) references status(status_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS order_history;
CREATE TABLE IF NOT EXISTS order_history (
	history_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
	user_id  		bigint(20) 		unsigned 	NOT NULL,
	total_sum 		DECIMAL(17, 2) 	NOT NULL DEFAULT '0',
	title 			varchar(50) 	COLLATE utf8_unicode_ci NOT NULL,
	rating			bigint(20) 		unsigned 	NOT NULL,
	status_id 		bigint(20) 		unsigned 	NOT NULL,
	CONSTRAINT 		fk_order_history_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT 		fk_order_history_user FOREIGN KEY (user_id) references user_list(user_id),
    CONSTRAINT		pk_order_history 	PRIMARY KEY (history_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS instrument_list;
CREATE TABLE IF NOT EXISTS instrument_list (
	instrument_id 	bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
	date_updated 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	description 	varchar(255) 	COLLATE utf8_unicode_ci NOT NULL,
	title 			varchar(50) 	COLLATE utf8_unicode_ci NOT NULL,
	status_id 		bigint(20) 		unsigned NOT NULL,
    price 			DECIMAL(17, 2) 	NOT NULL DEFAULT '0',
	closed 			tinyint(1) 		NOT NULL 	DEFAULT '1',
    UNIQUE KEY 		instrument_list_idx1 	(title),
    UNIQUE KEY 		instrument_list_idx2 	(description),
	CONSTRAINT 		fk_instrument_list_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT		pk_instrument_list 	PRIMARY KEY (instrument_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS order_list;
CREATE TABLE IF NOT EXISTS order_list (
	order_id 		bigint(20) 		unsigned NOT NULL AUTO_INCREMENT,
	date_created 	TIMESTAMP 		DEFAULT 	CURRENT_TIMESTAMP,
	user_id 		bigint(20) 		unsigned NOT NULL ,
	title 			varchar(50) 	COLLATE utf8_unicode_ci NOT NULL,
	status_id 		bigint(20) 		unsigned NOT NULL ,
	closed 			tinyint(1) 		NOT NULL 	DEFAULT '1',
    CONSTRAINT 		fk_order_list_user_list FOREIGN KEY (user_id) references user_list(user_id),
    CONSTRAINT 		fk_order_list_status FOREIGN KEY (status_id) references status(status_id),
    CONSTRAINT		pk_order_list 	PRIMARY KEY (order_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS instrument_order;
CREATE TABLE IF NOT EXISTS instrument_order (
	instrument_id 	bigint(20) 		unsigned NOT NULL ,
	order_id 		bigint(20) 		unsigned NOT NULL ,
	price 			DECIMAL(17, 2) 	NOT NULL DEFAULT '0',
	quantity 		TINYINT(30) 	NOT NULL DEFAULT '0',
	CONSTRAINT 		fk_instrument_order_instrument_list FOREIGN KEY (instrument_id) references instrument_list(instrument_id),
	CONSTRAINT 		fk_instrument_order_order_list FOREIGN KEY (order_id) references order_list(order_id),
    CONSTRAINT		pk_instrument_order 	PRIMARY KEY (instrument_id, order_id)
)ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8
COLLATE=utf8_unicode_ci;
