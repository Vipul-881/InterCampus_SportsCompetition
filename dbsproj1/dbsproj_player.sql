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
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `bitsID` varchar(20) NOT NULL,
  `playerName` varchar(20) DEFAULT NULL,
  `sportID` int DEFAULT NULL,
  `campusID` int DEFAULT NULL,
  `teamID` int DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `heightCentimeters` int DEFAULT NULL,
  `weightKilograms` int DEFAULT NULL,
  `injuries` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`bitsID`),
  KEY `fkPlayerSport` (`sportID`),
  KEY `fkPlayerCampus` (`campusID`),
  KEY `fkPlayerTeam` (`teamID`),
  CONSTRAINT `fkPlayerCampus` FOREIGN KEY (`campusID`) REFERENCES `campus` (`campusID`),
  CONSTRAINT `fkPlayerSport` FOREIGN KEY (`sportID`) REFERENCES `sport` (`sportID`),
  CONSTRAINT `fkPlayerTeam` FOREIGN KEY (`teamID`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES ('2021A7PS0098H','Arjun',101,123,13,'M',182,78,'nil'),('2022A3PS0700H','Rustin',199,345,31,'M',169,60,'nil'),('2022A7PS0001H','Sarah',105,123,67,'F',172,75,'cramp'),('2022A7PS0002H','Tina',145,234,56,'F',168,55,'fracture'),('2022A7PS0019H','Sandeep',104,345,43,'M',182,80,'nil'),('2022A7PS0030H','tomas',199,345,31,'M',175,74,'nil'),('2022A7PS0117H','David',101,123,13,'M',179,73,'nil'),('2022A7PS0150H','Rohith',100,234,9,'M',178,79,'nil'),('2022A7PS0193H','Manmeeth',105,123,67,'F',170,59,'nil'),('2022A7PS0195H','Anand',145,345,47,'M',181,81,'nil'),('2022A8PS0600H','Abhinaya',145,234,56,'F',173,73,'nil'),('2022AAPS0434H','Nani',104,345,43,'M',171,65,'nil'),('2022AAPS0435H','Sravika',104,234,33,'F',172,70,'nil'),('2022AAPS0500H','Bhargav',145,345,47,'M',175,59,'nil'),('2022AAPS0510H','Malavika',104,234,33,'F',170,67,'nil');
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-07  9:32:14
