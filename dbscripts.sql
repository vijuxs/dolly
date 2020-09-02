use desk_assist;

create table users (user_id INT NOT NULL AUTO_INCREMENT,
	username VARCHAR(20),
	password VARCHAR(50),
	PRIMARY KEY (user_id)
)
create table notes (note_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	text varchar(200) NOT NULL,
    user_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users (user_id)
	
);



