# Background

SQL sublanguage: DDL (Data Definition Language)

A foreign key is a column in one table that refers to the primary key in another table. This is how we relate
tables together.

CREATE TABLE song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name varchar(100),
    artist_fk int REFERENCES artist(id)
);

If we try to insert an `artist_fk` value that isn't in the `artist` table, an exception will be raised.

## Problem 1

Assume the following table already exists.

| id | firstname | lastname |
|----|-----------|----------|
| 1 | Steve | Garcia |
| 2 | Alexa | Smith |
| 3 | Steve | Jones |
| 4 | Brandon | Smith |
| 5 | Adam | Jones |

Create a `post` table in `problem1.sql` with the following columns: `id` (auto-incrementing primary key), `post`
(varchar(255)), and `user_fk` (int, referencing `site_user(id)`).
