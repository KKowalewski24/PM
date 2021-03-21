CREATE TABLE IF NOT EXISTS `products`.`products` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) CHARACTER SET 'utf8' NULL DEFAULT NULL,
  `description` TEXT CHARACTER SET 'utf8' NULL DEFAULT NULL,
  `price` INT(11) NULL DEFAULT NULL,
  `amount` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_polish_ci;

INSERT INTO `products`.`products` (`name`, `description`, `price`, `amount`) VALUES ('Lenovo Y510P', 'Good laptop', 4000, 3);
INSERT INTO `products`.`products` (`name`, `description`, `price`, `amount`) VALUES ('Lenovo T520', 'OK, but expensive', 7000, 2);
INSERT INTO `products`.`products` (`name`, `description`, `price`, `amount`) VALUES ('Acer 1234', 'Powerful', 5000, 5);
