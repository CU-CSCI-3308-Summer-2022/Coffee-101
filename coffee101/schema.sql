DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS drink;
DROP TABLE IF EXISTS record;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstName TEXT  NOT NULL,
  lastName TEXT  NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE drink (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  drink_name  TEXT  UNIQUE NOT NULL,
  image       TEXT  NOT NULL,
  keywords    TEXT
);

CREATE TABLE record (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  drink_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (drink_id) REFERENCES drink (id)
);

INSERT INTO drink (drink_name, image, keywords)
   VALUES
       ('Breve', 'static/img/bev/breve.png', 'dairy'),
       ('Cappuccino', 'static/img/bev/cappuccino.png', 'dairy'),
       ('Dry Cappuccino', 'static/img/bev/dry_cappuccino.png', 'dairy'),
       ('Americano', 'static/img/bev/americano.png', 'non-dairy'),
       ('Espresso', 'static/img/bev/espresso.png', 'non-dairy'),
       ('Latte', 'static/img/bev/latte.png', 'dairy'),
       ('Mocha', 'static/img/bev/mocha.png', 'dairy'),
       ('Macchiato', 'static/img/bev/macchiato.png', 'dairy'),
       ('Hawaiian', 'static/img/bev/hawaiian.png', 'non-dairy'),
       ('Irish', 'static/img/bev/irish.png', 'dairy_alcohol'),
       ('Flat White', 'static/img/bev/flat_white.png', 'dairy'),
       ('Caramel Macchiato', 'static/img/bev/caramel_macchiato.png', 'dairy');