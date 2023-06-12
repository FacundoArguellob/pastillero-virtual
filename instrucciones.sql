CREATE DATABASE IF NOT EXISTS pastillero_db ;

USE pastillero_db;

CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    passwd VARCHAR(100) NOT NULL,
    
    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDB;

CREATE TABLE remedios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    
    CONSTRAINT pk_remedios PRIMARY KEY (id)
)ENGINE=InnoDB;

CREATE TABLE recordatorios (
    id INT NOT NULL AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    remedio_id INT NOT NULL,
    dia VARCHAR(20) NOT NULL,
    hora VARCHAR(20) NOT NULL,

    CONSTRAINT pk_recordatorios PRIMARY KEY (id),
    CONSTRAINT fk_recordatorios_usuarios FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    CONSTRAINT fk_recordatorios_remedios FOREIGN KEY (remedio_id) REFERENCES remedios(id)
)ENGINE=InnoDB;