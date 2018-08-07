-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mylibrary
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `count` varchar(5) NOT NULL,
  `isbn` varchar(11) NOT NULL,
  `authors` varchar(250) NOT NULL,
  `year` varchar(10) NOT NULL,
  `title` varchar(145) NOT NULL,
  `language` varchar(45) NOT NULL,
  `rating` varchar(11) NOT NULL,
  `read` varchar(11) NOT NULL,
  `image` varchar(345) NOT NULL,
  PRIMARY KEY (`isbn`),
  FULLTEXT KEY `title` (`title`,`authors`),
  FULLTEXT KEY `title_2` (`title`),
  FULLTEXT KEY `title_3` (`title`),
  FULLTEXT KEY `title_4` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('7','121221213','George R.R. Martin','2011','A Dance with Dragons','eng','4','365957','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwiYmbnor-DXAhVEyLwKHd1gCwoQjRwIBw&url=https%3A%2F%2Fwww.target.com%2Fp%2Fa-dance-with-dragons-song-of-ice-and-fire-5-hardcover-george-r-r-martin%2F-%2FA-13455231&psig=AOvVaw0LgwUkNlT4UAaXckHcx5JH&ust=1511927721824671'),('5','140003468','Gabriel García Márquez, Edith Grossman','1985','El amor en los tiempos del cólera','eng','4','283807','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjF4OaateDXAhUJKo8KHT5yB-kQjRwIBw&url=http%3A%2F%2Fnotasomargonzalez.blogspot.com%2F2013%2F09%2Fel-amor-en-los-tiempos-del-colera.html&psig=AOvVaw1jkcW1YYMiZuC5Xl-qF0av&ust=1511929168024246'),('9','140042598','Jack Kerouac','1955','On the Road','eng','4','246602','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjpu7LMseDXAhVCNrwKHZMiA9wQjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FRoad-50th-Anniversary-Jack-Kerouac%2Fdp%2F0670063266&psig=AOvVaw0GaFDMmZt_9AOrZ1SKYdiJ&ust=1511928197244926'),('2','140283331','William Golding','1954','Lord of the Flies ','eng','4','1605019','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjt4cXhseDXAhUBkZQKHZwoCC8QjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLord_of_the_Flies&psig=AOvVaw0Ayrd9VqinhEu0BDPDkT_D&ust=1511928243840021'),('1','140285601','Kurt Vonnegut Jr.','1963','Cat\'s Cradle','eng','4','238940','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiVtZX4seDXAhUMxrwKHdKTBCYQjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCat%2527s_Cradle&psig=AOvVaw1p3lZewsOSCfTMdJ8WoGcN&ust=1511928291557885'),('5','14038572','S.E. Hinton','1967','The Outsiders','en-US','4','659248','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjL8KyHsuDXAhUFJZQKHShSBDIQjRwIBw&url=https%3A%2F%2Fwww.goodreads.com%2Fbook%2Fshow%2F231804.The_Outsiders&psig=AOvVaw17ACBt_ihTAXD86s0MtkZH&ust=1511928322747051'),('3','141301066','Roald Dahl, Quentin Blake','1988','Matilda','eng','4','440743','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjk36uSsuDXAhWHp5QKHR8LCNoQjRwIBw&url=https%3A%2F%2Fwww.goodreads.com%2Fbook%2Fshow%2F39988.Matilda&psig=AOvVaw209qPxcnbi3qruoq775aK2&ust=1511928346653368'),('4','14131088','Laurie Halse Anderson','1999','Speak','eng','4','360157','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjf3uCcsuDXAhXJpJQKHSwKAwgQjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSpeak_(Anderson_novel)&psig=AOvVaw1-jypwdYdxQJupZQ0NBoBb&ust=1511928368076131'),('4','141382899','Rick Riordan','2007','The Titan\'s Curse','eng','4','446668','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjvroSusuDXAhXDw7wKHbAyDtkQjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FThe_Titan%2527s_Curse&psig=AOvVaw2gmXCjpFEKlVIfBY279kFg&ust=1511928396941609'),('3','141439475','Mary Wollstonecraft Shelley, Percy Bysshe Shelley,','1818','Frankenstein; or, The Modern Prometheus','eng','4','808589','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjm5P_OsuDXAhWIVrwKHYi8DTUQjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FFrankenstein-Mary-Shelley%2Fdp%2F0553212478&psig=AOvVaw0VW-7qyEMAZL13Ic8yKMX5&ust=1511928433613369'),('12','141439580','Jane Austen, Fiona Stafford','1815','Emma','eng','4','459826','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwizmIvjsuDXAhVCvbwKHf1KD3QQjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FJane-Austens-Emma-Bernard-Hepton%2Fdp%2FB00JEEZSCI&psig=AOvVaw0l6xsZ5SNPbhAdMrd63SX5&ust=1511928514713547'),('6','141439602','Charles Dickens, Richard Maxwell, Hablot Knight Br','1859','A Tale of Two Cities','eng','4','637412','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiz6o7usuDXAhXEu7wKHfb7BN0QjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FA_Tale_of_Two_Cities&psig=AOvVaw2gQ8iB4kqTOJMTM3ku4Dya&ust=1511928539369900'),('6','141439661','Jane Austen, Tony Tanner, Ros Ballaster','1811','Sense and Sensibility','eng','4','738894','https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwju7J_9suDXAhUSNbwKHd1GDmQQjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FSense-Sensibility-Oxford-Worlds-Classics%2Fdp%2F0192804782&psig=AOvVaw0rl6V_PMKt4EfgnCcWhf5_&ust=1511928562015343');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-28 10:52:19
