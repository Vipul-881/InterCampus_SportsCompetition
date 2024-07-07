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
-- Table structure for table `wins`
--

DROP TABLE IF EXISTS `wins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wins` (
  `teamID` int NOT NULL,
  `sportID` int NOT NULL,
  `noOfWins` int DEFAULT NULL,
  PRIMARY KEY (`teamID`),
  KEY `fkwinsport` (`sportID`),
  CONSTRAINT `fkwinsport` FOREIGN KEY (`sportID`) REFERENCES `sport` (`sportID`),
  CONSTRAINT `fkwinsteam` FOREIGN KEY (`teamID`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wins`
--

LOCK TABLES `wins` WRITE;
/*!40000 ALTER TABLE `wins` DISABLE KEYS */;
INSERT INTO `wins` VALUES (7,100,0),(9,100,0),(11,100,0),(13,101,3),(15,101,0),(23,104,0),(31,199,0),(33,104,0),(43,104,1),(47,145,0),(52,101,2),(56,145,0),(67,105,0),(68,105,0),(69,105,2),(75,105,0),(80,145,1),(81,102,2),(90,102,0),(99,102,0),(100,201,1),(101,201,0),(102,201,0);
/*!40000 ALTER TABLE `wins` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-07  9:32:15
