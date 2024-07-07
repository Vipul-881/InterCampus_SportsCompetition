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
-- Table structure for table `matches`
--

DROP TABLE IF EXISTS `matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matches` (
  `matchID` int NOT NULL,
  `team1ID` int DEFAULT NULL,
  `team2ID` int DEFAULT NULL,
  `sportID` int DEFAULT NULL,
  `date` varchar(15) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `refereeID` int DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `venue` varchar(20) DEFAULT NULL,
  `winID` int DEFAULT NULL,
  PRIMARY KEY (`matchID`),
  KEY `fkMatchteam1` (`team1ID`),
  KEY `fkMatchteam2` (`team2ID`),
  KEY `fkMatchSport` (`sportID`),
  KEY `fkMatchRef` (`refereeID`),
  CONSTRAINT `fkMatchRef` FOREIGN KEY (`refereeID`) REFERENCES `referee` (`refereeID`),
  CONSTRAINT `fkMatchSport` FOREIGN KEY (`sportID`) REFERENCES `sport` (`sportID`),
  CONSTRAINT `fkMatchteam1` FOREIGN KEY (`team1ID`) REFERENCES `teams` (`teamID`),
  CONSTRAINT `fkMatchteam2` FOREIGN KEY (`team2ID`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matches`
--

LOCK TABLES `matches` WRITE;
/*!40000 ALTER TABLE `matches` DISABLE KEYS */;
INSERT INTO `matches` VALUES (213,13,52,101,'13-4-2023','3:00',12,'M','CricketGround',13),(241,13,52,101,'13-3-2023','2:45',12,'M','CricketGround',52),(290,47,80,145,'12-3-2-23','8:00',13,'M','SwimmingPool',80),(333,13,15,101,'13-3-2023','9:00',12,'M','CricketGround',13),(390,69,68,105,'10-3-2023','9:00',15,'M','TennisCourt',69),(391,69,68,105,'16-4-2023','1:00',12,'M','BadmintonCourt',69),(450,81,99,102,'14-3-2023','11:00',15,'F','BasketballCourt',81),(534,13,15,101,'11-3-2023','1:00',12,'M','CricketGround',13),(680,23,43,104,'16-3-2023','4:00',13,'M','HockeyGround',43),(767,81,99,102,'9-3-2023','10:00',98,'F','BasketballCourt',81),(789,100,101,201,'15-3-2023','9:00',98,'M','BadmintonCourt',100),(800,52,13,101,'16-3-2023','10:00',98,'M','CricketGround',52);
/*!40000 ALTER TABLE `matches` ENABLE KEYS */;
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
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `inc_wins` AFTER UPDATE ON `matches` FOR EACH ROW update wins
set noOfWins=noOfWins+1
where wins.teamID=new.winID */;;
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
