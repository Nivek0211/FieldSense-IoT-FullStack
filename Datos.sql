SELECT * FROM fieldsense_db.lecturas;
-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS fieldsense_db;
USE fieldsense_db;

-- Estructura de la tabla para las lecturas del sensor
CREATE TABLE IF NOT EXISTS `lecturas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `sensor_id` VARCHAR(50) NOT NULL,
  `temperatura` FLOAT NOT NULL,
  `humedad` FLOAT NOT NULL,
  `latitud` FLOAT NOT NULL,
  `longitud` FLOAT NOT NULL,
  `fecha_hora` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;