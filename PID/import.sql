USE pid;

INSERT INTO PID_show(title, posteUrl, price, bookable) values
    ("L'opera rock", "url.opera_rock", 75.0, 1),
    ("Shakespeare in love", "url.shakespeare", 65.0, 1),
    ("Michel Sardou", "url.sardou", 90.0, 0),
    ("Romeo et Juliette", "url.r&j", 120.0, 1)
                                                              ;

INSERT INTO PID_role(id, role) values
    (2, "DA_ROLE");


INSERT INTO PID_user(login, password, firstname, lastname, email, langue, roleId_id) values
    ("Johnny", "banane", "", "", "", "", 2),
    ("Admin", "admin", "", "", "", "", 2),
    ("Feul", "test", "", "", "", "", 2),
    ("Romeo", "Juliette", "", "", "", "", 2)
                                                              ;