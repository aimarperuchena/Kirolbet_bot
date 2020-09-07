CREATE TABLE `sport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `des` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;
CREATE TABLE `market` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sport_id` int(11) DEFAULT NULL,
  `des` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sport_id_fk_3_idx` (`sport_id`),
  CONSTRAINT `sport_id_fk_3` FOREIGN KEY (`sport_id`) REFERENCES `sport` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB;



CREATE TABLE `league` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sport_id` int(11) DEFAULT NULL,
  `des` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sport_id_fk_idx` (`sport_id`),
  CONSTRAINT `sport_id_fk_2` FOREIGN KEY (`sport_id`) REFERENCES `sport` (`id`)
) ENGINE=InnoDB ;


CREATE TABLE `game` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game` varchar(200) DEFAULT NULL,
  `sport_id` int(11) DEFAULT NULL,
  `league_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sport_id_fk_idx` (`sport_id`),
  KEY `league_id_fk_idx` (`league_id`),
  CONSTRAINT `league_id_fk` FOREIGN KEY (`league_id`) REFERENCES `league` (`id`),
  CONSTRAINT `sport_id_fk` FOREIGN KEY (`sport_id`) REFERENCES `sport` (`id`)
) ENGINE=InnoDB ;


CREATE TABLE `game_bet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(11) DEFAULT NULL,
  `market_id` int(11) DEFAULT NULL,
  `bookie` varchar(200) DEFAULT 'Kirolbet',
  PRIMARY KEY (`id`),
  KEY `game_id_fk_idx` (`game_id`),
  KEY `market_id_fk_idx` (`market_id`),
  CONSTRAINT `game_id_fk` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `market_id_fk` FOREIGN KEY (`market_id`) REFERENCES `market` (`id`)
) ENGINE=InnoDB;

CREATE TABLE `odds` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_bet_id` int(11) DEFAULT NULL,
  `des` varchar(200) DEFAULT NULL,
  `odd` double DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `game_bet_id_fk_idx` (`game_bet_id`),
  CONSTRAINT `game_bet_id_fk` FOREIGN KEY (`game_bet_id`) REFERENCES `game_bet` (`id`)
) ENGINE=InnoDB;



