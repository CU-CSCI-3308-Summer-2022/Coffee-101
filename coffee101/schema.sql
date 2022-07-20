/* Reset + (Re)Generate SQLite Data-frames   /
/  WARNING: Execution of this file directly  /
/           -will- result in loss of user    /
/           and post data.	    	     /
/ ----------------------------------------- */

--reset
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS drinks;

--user:
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  saved_coffees TEXT[] NOT NULL
);

--post:
CREATE TABLE post (
  id   	    INTEGER   PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER   NOT NULL,
  created   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title     TEXT      NOT NULL,
  body 	    TEXT      NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

--drinks: 
CREATE TABLE drinks (
  id   	    INTEGER PRIMARY KEY AUTOINCREMENT,
  drink_name  TEXT  UNIQUE NOT NULL,
  image       TEXT  NOT NULL,
  keywords    TEXT  
);	

--Add in the usual suspects.
INSERT INTO drinks (drink_name, image_file, keywords)
   VALUES
       ('Breve', 'img/bev/breve.png', 'dairy'),
       ('Cappuccino', 'img/bev/cappuccino.png', 'dairy'),
       ('Dry Cappuccino', 'img/bev/dry_cappuccino.png', 'dairy'),
       ('Americano', 'img/bev/americano.png', 'non-dairy'),
       ('Espresso', 'img/bev/espresso.png', 'non-dairy'),
       ('Latte', 'img/bev/latte.png', 'dairy'),
       ('Mocha', 'img/bev/mocha.png', 'dairy'),
       ('Macchiato', 'img/bev/macchiato.png', 'dairy'),
       ('Hawaiian', 'img/bev/hawaiian.png', 'non-dairy'),
       ('Irish', 'img/bev/irish.png', 'dairy_alcohol'),
       ('Flat White', 'img/bev/flat_white.png', 'dairy'),
       ('Caramel Macchiato', 'img/bev/caramel_macchiato.png', 'dairy');