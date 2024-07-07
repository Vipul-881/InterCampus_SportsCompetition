-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dbsproj
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `teamID` int NOT NULL,
  `campusID` int DEFAULT NULL,
  `teamName` varchar(20) DEFAULT NULL,
  `noOfPlayers` int DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `sportID` int NOT NULL,
  PRIMARY KEY (`teamID`),
  KEY `fkTeamcampus` (`campusID`),
  KEY `fkTeamSport` (`sportID`),
  CONSTRAINT `fkTeamcampus` FOREIGN KEY (`campusID`) REFERENCES `campus` (`campusID`),
  CONSTRAINT `fkTeamSport` FOREIGN KEY (`sportID`) REFERENCES `sport` (`sportID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES (7,123,'HackingHeights',2,'M',100),(9,234,'RippingBalls',2,'M',100),(11,345,'SquashingGirls',2,'F',100),(13,123,'BadShots',13,'M',101),(15,234,'Sunfallers',14,'M',101),(23,123,'KeepingGiants',11,'M',104),(31,345,'CarromKings',2,'M',199),(33,234,'HittingRats',11,'F',104),(43,345,'MaskingMasks',11,'M',104),(47,345,'BreathingCasers',1,'M',145),(52,234,'Capitalists',15,'M',101),(56,234,'DropDeads',1,'F',145),(67,123,'CravingHunters',2,'F',105),(68,234,'TrickingBatters',2,'M',105),(69,345,'WinningClasses',2,'M',105),(75,123,'Holihawks',2,'M',105),(80,123,'SwimSuiters',1,'M',145),(81,123,'RisingTacklers',8,'F',102),(90,234,'BasketingHoles',7,'M',102),(99,345,'PilaniLights',7,'F',102),(100,123,'ShuttleGivers',2,'M',201),(101,234,'NetTakers',2,'M',201),(102,345,'ShotHitters',2,'M',201);
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `add_to_wins` AFTER INSERT ON `teams` FOR EACH ROW insert into wins(teamID,sportID,noOfWins) values (new.teamID,new.sportID,0) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-07  9:32:15
