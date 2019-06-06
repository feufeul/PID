<<<<<<< HEAD
use PID;


                                                              ;

INSERT INTO PID_role(id, role) values
    (2, "DA_ROLE"),
    (3, "administrateur"),
    ;


INSERT INTO PID_user(login, password, firstname, lastname, email, langue, roleId_id) values
    ("Johnny", "banane", "Jean", "Laet", "Jean.Laet@gmail.com", "fr", 2),
    ("Admin", "admin", "administrateur", "dusite", "admin@gmail.com", "fr", 3),
    ("Feul", "test", "feulfeul", "testeur", "feultest@gmail.com", "nl", 2),
    ("Romeo", "Juliette", "Roméo", "Niro", "romeo.niro@gmail.com", "nl", 2)
    ("John", "lire", "John", "Lacoste", "Jolac@gmail.com", "fr", 2),
    ("Adele", "adel23", "Adèle", "Chantier", "adelchan@gmail.com", "fr", 2),
    ("Flor23", "12345", "Florence", "Uriel", "floU@gmail.com", "nl", 2),
    ("Romain", "Lier", "Romain", "De Smet", "romainDeSmet@gmail.com", "nl", 2)
    ;

INSERT INTO PID_localitie()
	
	;


INSERT INTO PID_location(designation, address, website, phone, localityId) values
	("Théatre des Beaux Arts", "Rue de la frèvre 248", "www.beauxArts.com", "02543765", 1082),
	("Théatre les tanneurs", "Rue des tanneurs 75-77", "www.lestanneurs.be", "02346567", 1000),
	("Le Cuberdon", "Boulevard Maurice Lemonier 99", "https://www.spectable.be/le-cuberdon-cafe-theatre/173657", "02567890", 1000),
	("Compagnie sur le fil", "Rue des tanneurs 75", "http://www.surlefil.be/", "0476876543", 1000),
	("Compagnie Mossoux-Bonté", "Rue des tanneurs 87", "http://www.mossoux-bonte.be/", "02765345", 1000),
	("Murmuur Scris FS", "Rue du chimiste 34", "", "02345678", 1070),
	("La monnaie de Munt", "Place de la monnaie", "www.lamonnaie.be", "02987458", 1000),
	("Théâtre du Vaudeville", "Galerie de la reine 13", "http://www.theatreduvaudeville.be/", "02987890", 1000),
	("Théâtre Royal De Toone", "Rue du marché aux herbes 66", "http://www.toone.be/", "02098654", 1000),
	("Théâtre royal des Galeries", "Galerie du Roi 32", "https://trg.be/", 1000)
	;


INSERT INTO PID_show(title, posteUrl, price, bookable, locationId) values
	("L'opera rock", "url.opera_rock", 75.0, 1, 1000),
    ("Shakespeare in love", "url.shakespeare", 65.0, 1, 1000),
    ("Michel Sardou", "url.sardou", 90.0, 0, 1000),
    ("Romeo et Juliette", "url.r&j", 120.0, 1, 1082)
    ("Don Quichotte", "url.don_quichotte", 60.0, 0, 1000 )
    ("Moi et tout", "url.moi&tout", 65, 1, 1070)
    ;


INSERT INTO PID_representation(when, showId, locationId) values
	("2019-05-25", 2, 1000),
	("2019-06-02", 1, 1000),
	("2019-07-23", 3, 1000),
	("2019-05-10", 4, 1082),
	("2019-05-06", 5, 1000),
	("2019-09-15", 6, 1070),
	("2019-12-25", 6, 1000),
	;

INSERT INTO PID_representationUser(places, representationId, userId) values
	(4, 1, 1),
	(3, 2, 2),
	(2, 3, 3),
	(1, 4, 4),
	(8, 3, 5),
	(6, 3, 6),
	(4, 5, 7),
	(3, 2, 8),
	;


INSERT INTO PID_artist(firstname, lastname) values
	("Jean", "Dupuis"),
	("Corinne", "De la Ruelle"),
	("Éric", "Van Couve")
	("Céline", "De Paepe"),
	("Orélie", "Soete"),
	("Quentin", "Bonjour"),
	("Vincent", "Quenelle"),
	("Jeanne", "D'arc"),
	("Lancelot", "Du lac"),
	("Merlin"), ("Du lac"),
	("Arthur"), ("Pendragon"),
	("François", "Kavamahanga")
	;


INSERT INTO PID_artisteType(artisteTypeId, showId) values
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 1),
	(8, 2),
	(9, 3),
	(10, 4),
	(11, 5),
	(12, 6),
	(1, 2),
	(2, 3),
	(3, 4),
	(4, 5),
	(5, 6),
	(6, 1),
	(7, 2),
	(8, 1),
	;



INSERT INTO PID_type(type) values
	("comédie"),
	("opéra"),
	("concert"),
	("comédie-musicale"),
	("tragédie")
	;


INSERT INTO PID_artisteTypeShow(artiste_type_id, show_id) values
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 1),
	(8, 2),
	(9, 3),
	(10, 4),
	(11, 5),
	(12, 6),
	(1, 1),
	(2, 2),
	(5, 3),
	(11, 4),
	(8, 5),
	(7, 6),
	(3, 1),
	(2, 2),
	;
=======
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
>>>>>>> 0eb72815b9067452680ed8d149cf6cd931cc264d
