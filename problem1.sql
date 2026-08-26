CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post varchar(255),
    user_fk int REFERENCES site_user(id)
);