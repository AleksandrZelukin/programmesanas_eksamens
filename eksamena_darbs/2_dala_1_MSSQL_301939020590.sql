);


CREATE TABLE GRAMATAS (
    id SERIAL PRIMARY KEY,
    nosaukums VARCHAR(255) NOT NULL,
    autors VARCHAR(255) NOT NULL,
    zanrs VARCHAR(100) NOT NULL,
    izdosanas_gads INT CHECK (izdosanas_gads > 0),
    lappusu_skaits INT CHECK (lappusu_skaits > 0)
);


CREATE TABLE LIETOTAJI (
    id SERIAL PRIMARY KEY,
    vards VARCHAR(100) NOT NULL,
    uzvards VARCHAR(100) NOT NULL,
    personas_kods VARCHAR(20) UNIQUE NOT NULL,
    epasts VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE STATISTIKA (
    id SERIAL PRIMARY KEY,
    lietotaja_id INT NOT NULL REFERENCES LIETOTAJI(id),
    gramatas_id INT NOT NULL REFERENCES GRAMATAS(id),
    sakuma_datums DATE NOT NULL,
    ilgums_dienas INT CHECK (ilgums_dienas > 0)
);