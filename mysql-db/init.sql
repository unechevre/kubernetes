CREATE DATABASE IF NOT EXISTS advices;
USE advices;

CREATE TABLE IF NOT EXISTS advice (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255) NOT NULL
);

INSERT INTO advice (text) VALUES
('N\'abandonne jamais tes rêves.'),
('La patience est la clé de la réussite.'),
('Chaque échec est une leçon déguisée.'),
('Fais confiance à ton instinct.');
