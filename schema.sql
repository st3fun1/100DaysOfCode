DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id integer primary key autoincrement,
    name text not null,
    context text not null
);