-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: MonNovoa.mysql.eu.pythonanywhere-services.com    Database: MonNovoa$botFono
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add audio_etiqueta',7,'add_audio_etiqueta'),(26,'Can change audio_etiqueta',7,'change_audio_etiqueta'),(27,'Can delete audio_etiqueta',7,'delete_audio_etiqueta'),(28,'Can view audio_etiqueta',7,'view_audio_etiqueta'),(29,'Can add audio_fono',8,'add_audio_fono'),(30,'Can change audio_fono',8,'change_audio_fono'),(31,'Can delete audio_fono',8,'delete_audio_fono'),(32,'Can view audio_fono',8,'view_audio_fono'),(33,'Can add audio_persona',9,'add_audio_persona'),(34,'Can change audio_persona',9,'change_audio_persona'),(35,'Can delete audio_persona',9,'delete_audio_persona'),(36,'Can view audio_persona',9,'view_audio_persona'),(37,'Can add genero_usuario',10,'add_genero_usuario'),(38,'Can change genero_usuario',10,'change_genero_usuario'),(39,'Can delete genero_usuario',10,'delete_genero_usuario'),(40,'Can view genero_usuario',10,'view_genero_usuario'),(41,'Can add usuario',11,'add_usuario'),(42,'Can change usuario',11,'change_usuario'),(43,'Can delete usuario',11,'delete_usuario'),(44,'Can view usuario',11,'view_usuario'),(45,'Can add tipo_usuario',12,'add_tipo_usuario'),(46,'Can change tipo_usuario',12,'change_tipo_usuario'),(47,'Can delete tipo_usuario',12,'delete_tipo_usuario'),(48,'Can view tipo_usuario',12,'view_tipo_usuario'),(49,'Can add usuario bot',11,'add_usuariobot'),(50,'Can change usuario bot',11,'change_usuariobot'),(51,'Can delete usuario bot',11,'delete_usuariobot'),(52,'Can view usuario bot',11,'view_usuariobot'),(53,'Can add tipo_diagnostico_flgo',7,'add_tipo_diagnostico_flgo'),(54,'Can change tipo_diagnostico_flgo',7,'change_tipo_diagnostico_flgo'),(55,'Can delete tipo_diagnostico_flgo',7,'delete_tipo_diagnostico_flgo'),(56,'Can view tipo_diagnostico_flgo',7,'view_tipo_diagnostico_flgo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$gPyOQscB39VjRzFjjG5h47$7mtohNF7be6bYn1vXkCFNjEb/57jd2ktj/TWzGcsUR8=','2024-02-21 11:40:55.582959',1,'admin','Administrador','','admin@admin.cl',1,1,'2024-02-06 20:04:14.000000'),(2,'pbkdf2_sha256$320000$5tuzdWLoFwoFJF5nckmojM$LbKBXo5ocvnLBmxUgKLtKguFj/d7nkARPHu4emVYN2M=','2024-02-08 15:24:05.000000',0,'fono1','Fonoaudiólogo','Uno','',0,1,'2024-02-08 11:55:59.000000'),(3,'pbkdf2_sha256$320000$EbJOzMHz4W9Nh3Sx0mVaX0$Ii7g3hjXhzJCaU66zvTMsyZdBOixC9AyotL1E99cpzk=','2024-02-19 20:52:15.687957',0,'prueba','','','',0,1,'2024-02-08 12:44:47.554968'),(4,'pbkdf2_sha256$320000$FrQdeXVAu73b0sRvcRL8VD$hy7MZEIs0r27j7ue+GDSBkgXSpmZ30W0PhnGFrBcI9o=','2024-02-20 17:37:58.527097',0,'cristobal','','','',1,1,'2024-02-19 13:06:32.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `botApp_audio_fono`
--

DROP TABLE IF EXISTS `botApp_audio_fono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `botApp_audio_fono` (
  `id` int NOT NULL AUTO_INCREMENT,
  `audio_fo` varchar(100) NOT NULL,
  `ano_nac` varchar(10) NOT NULL,
  `tipo_diagnostico_flgo_id` int NOT NULL,
  `genero_usuario_id` int NOT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  `id_usuario` int NOT NULL,
  `nombre_paciente` varchar(20) NOT NULL,
  `audio_fo2` varchar(100) DEFAULT NULL,
  `audio_fo3` varchar(100) DEFAULT NULL,
  `audio_fo4` varchar(100) DEFAULT NULL,
  `audio_fo5` varchar(100) DEFAULT NULL,
  `otras_enfermedades` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `botApp_audio_fono_genero_usuario_id_dab8cd98_fk_botApp_ge` (`genero_usuario_id`),
  KEY `botApp_audio_fono_tipo_diagnostico_flg_eb478195_fk_botApp_ti` (`tipo_diagnostico_flgo_id`),
  CONSTRAINT `botApp_audio_fono_genero_usuario_id_dab8cd98_fk_botApp_ge` FOREIGN KEY (`genero_usuario_id`) REFERENCES `botApp_genero_usuario` (`id`),
  CONSTRAINT `botApp_audio_fono_tipo_diagnostico_flg_eb478195_fk_botApp_ti` FOREIGN KEY (`tipo_diagnostico_flgo_id`) REFERENCES `botApp_tipo_diagnostico_flgo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `botApp_audio_fono`
--

LOCK TABLES `botApp_audio_fono` WRITE;
/*!40000 ALTER TABLE `botApp_audio_fono` DISABLE KEYS */;
INSERT INTO `botApp_audio_fono` VALUES (9,'audios/biodynamic-impact-braam-tonal-dark-184276_MXP3UZZ.mp3','1991',5,1,'2024-02-19 15:41:17.089444',1,'prueba 1','','','','','1'),(10,'audios/biodynamic-impact-braam-tonal-dark-184276_hdjuwOX.mp3','1996',1,1,'2024-02-19 15:41:55.554860',1,'prueba 2','audios/biodynamic-impact-braam-tonal-dark-184276_2sxW7Ro.mp3','audios/labyrinth-for-the-brain-190096_tjJR3ws.mp3','','','1'),(11,'audios/biodynamic-impact-braam-tonal-dark-184276_tQJ5jrj.mp3','1994',2,1,'2024-02-19 20:41:47.060869',1,'Prueba 3','','','','','[\'parkinson\', \'hipertension\']'),(13,'audios/labyrinth-for-the-brain-190096_n4F7iQK.mp3','1991',3,4,'2024-02-19 20:52:41.897702',3,'Prueba 4','','','','','[\'Enf_parkinson\', \'Hipertensión\']');
/*!40000 ALTER TABLE `botApp_audio_fono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `botApp_audio_persona`
--

DROP TABLE IF EXISTS `botApp_audio_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `botApp_audio_persona` (
  `id` int NOT NULL AUTO_INCREMENT,
  `audio_us` varchar(100) NOT NULL,
  `wsp_usuario` int NOT NULL,
  `ano_nac` varchar(10) NOT NULL,
  `tipo_diagnostico_flgo_id` int NOT NULL,
  `genero_usuario_id` int NOT NULL,
  `fecha_registro_paciente` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `botApp_audio_persona_genero_usuario_id_0c8359a1_fk_botApp_ge` (`genero_usuario_id`),
  KEY `botApp_audio_persona_tipo_diagnostico_flg_7eed882f_fk_botApp_ti` (`tipo_diagnostico_flgo_id`),
  CONSTRAINT `botApp_audio_persona_genero_usuario_id_0c8359a1_fk_botApp_ge` FOREIGN KEY (`genero_usuario_id`) REFERENCES `botApp_genero_usuario` (`id`),
  CONSTRAINT `botApp_audio_persona_tipo_diagnostico_flg_7eed882f_fk_botApp_ti` FOREIGN KEY (`tipo_diagnostico_flgo_id`) REFERENCES `botApp_tipo_diagnostico_flgo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `botApp_audio_persona`
--

LOCK TABLES `botApp_audio_persona` WRITE;
/*!40000 ALTER TABLE `botApp_audio_persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `botApp_audio_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `botApp_genero_usuario`
--

DROP TABLE IF EXISTS `botApp_genero_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `botApp_genero_usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_genero` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `botApp_genero_usuario`
--

LOCK TABLES `botApp_genero_usuario` WRITE;
/*!40000 ALTER TABLE `botApp_genero_usuario` DISABLE KEYS */;
INSERT INTO `botApp_genero_usuario` VALUES (1,'Femenino'),(3,'Masculino'),(4,'Otro');
/*!40000 ALTER TABLE `botApp_genero_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `botApp_tipo_diagnostico_flgo`
--

DROP TABLE IF EXISTS `botApp_tipo_diagnostico_flgo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `botApp_tipo_diagnostico_flgo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_diagnostico` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `botApp_tipo_diagnostico_flgo`
--

LOCK TABLES `botApp_tipo_diagnostico_flgo` WRITE;
/*!40000 ALTER TABLE `botApp_tipo_diagnostico_flgo` DISABLE KEYS */;
INSERT INTO `botApp_tipo_diagnostico_flgo` VALUES (1,'Disartria'),(2,'Disfagia'),(3,'Voz y habla'),(5,'Paciente sano'),(6,'Otros');
/*!40000 ALTER TABLE `botApp_tipo_diagnostico_flgo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `botApp_tipo_usuario`
--

DROP TABLE IF EXISTS `botApp_tipo_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `botApp_tipo_usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_tipo_usuario` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `botApp_tipo_usuario`
--

LOCK TABLES `botApp_tipo_usuario` WRITE;
/*!40000 ALTER TABLE `botApp_tipo_usuario` DISABLE KEYS */;
INSERT INTO `botApp_tipo_usuario` VALUES (1,'Usuario'),(2,'Paciente'),(3,'admin');
/*!40000 ALTER TABLE `botApp_tipo_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-02-06 20:06:48.028799','1','Femenino',1,'[{\"added\": {}}]',10,1),(2,'2024-02-06 20:06:58.509428','2','Femenino',1,'[{\"added\": {}}]',10,1),(3,'2024-02-06 20:07:03.232675','3','Masculino',1,'[{\"added\": {}}]',10,1),(4,'2024-02-06 20:07:06.358899','4','Otro',1,'[{\"added\": {}}]',10,1),(5,'2024-02-06 20:07:21.492090','2','Femenino',3,'',10,1),(6,'2024-02-06 20:07:31.401298','1','Disartria',1,'[{\"added\": {}}]',7,1),(7,'2024-02-06 20:07:34.871132','2','Disfagia',1,'[{\"added\": {}}]',7,1),(8,'2024-02-06 20:07:37.460949','3','Voz_Habla',1,'[{\"added\": {}}]',7,1),(9,'2024-02-06 20:07:41.486688','4','Otro',1,'[{\"added\": {}}]',7,1),(10,'2024-02-07 11:47:02.586746','1','audio_fono object (1)',1,'[{\"added\": {}}]',8,1),(11,'2024-02-07 11:51:31.826032','1','audio_fono object (1)',3,'',8,1),(12,'2024-02-07 19:27:52.969235','2','audio_fono object (2)',3,'',8,1),(13,'2024-02-07 19:28:42.373273','1','Usuario',1,'[{\"added\": {}}]',12,1),(14,'2024-02-07 19:28:45.965457','2','Paciente',1,'[{\"added\": {}}]',12,1),(15,'2024-02-07 19:28:49.440209','3','admin',1,'[{\"added\": {}}]',12,1),(16,'2024-02-07 19:29:13.825253','1','1',1,'[{\"added\": {}}]',11,1),(17,'2024-02-08 11:55:59.624180','2','fono1',1,'[{\"added\": {}}]',4,1),(18,'2024-02-08 12:44:47.774688','3','prueba',1,'[{\"added\": {}}]',4,1),(19,'2024-02-08 17:27:16.485015','2','fono1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),(20,'2024-02-08 18:26:26.505991','1','admin',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',4,1),(21,'2024-02-09 16:35:26.863128','3','audio_fono object (3)',3,'',8,1),(22,'2024-02-09 16:35:37.029918','5','audio_fono object (5)',3,'',8,1),(23,'2024-02-09 16:35:37.035973','4','audio_fono object (4)',3,'',8,1),(24,'2024-02-19 13:06:32.438941','4','cristobal',1,'[{\"added\": {}}]',4,1),(25,'2024-02-19 13:06:41.749937','4','cristobal',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(26,'2024-02-19 15:40:20.916389','5','Paciente_Sano',1,'[{\"added\": {}}]',7,1),(27,'2024-02-19 15:40:29.210216','4','Otro',3,'',7,1),(28,'2024-02-19 15:40:36.265634','6','Otro',1,'[{\"added\": {}}]',7,1),(29,'2024-02-19 20:43:07.923873','8','audio_fono object (8)',3,'',8,1),(30,'2024-02-19 20:43:07.929190','6','audio_fono object (6)',3,'',8,1),(31,'2024-02-19 20:50:03.333934','12','audio_fono object (12)',3,'',8,1),(32,'2024-02-20 13:16:28.131446','1','Disartria',2,'[{\"changed\": {\"fields\": [\"Nombre diagnostico\"]}}]',7,1),(33,'2024-02-20 13:16:39.009220','2','Disfagia',2,'[{\"changed\": {\"fields\": [\"Nombre diagnostico\"]}}]',7,1),(34,'2024-02-20 13:16:47.558683','3','Voz y habla',2,'[{\"changed\": {\"fields\": [\"Nombre diagnostico\"]}}]',7,1),(35,'2024-02-20 13:16:58.469916','5','Paciente sano',2,'[{\"changed\": {\"fields\": [\"Nombre diagnostico\"]}}]',7,1),(36,'2024-02-20 13:16:59.347722','5','Paciente sano',2,'[]',7,1),(37,'2024-02-20 13:17:07.365804','6','Otros',2,'[{\"changed\": {\"fields\": [\"Nombre diagnostico\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'botApp','audio_fono'),(9,'botApp','audio_persona'),(10,'botApp','genero_usuario'),(7,'botApp','tipo_diagnostico_flgo'),(12,'botApp','tipo_usuario'),(11,'botApp','usuariobot'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-02-06 16:56:04.676469'),(2,'auth','0001_initial','2024-02-06 16:56:09.493515'),(3,'admin','0001_initial','2024-02-06 16:56:10.702466'),(4,'admin','0002_logentry_remove_auto_add','2024-02-06 16:56:10.776937'),(5,'admin','0003_logentry_add_action_flag_choices','2024-02-06 16:56:10.816662'),(6,'contenttypes','0002_remove_content_type_name','2024-02-06 16:56:11.311573'),(7,'auth','0002_alter_permission_name_max_length','2024-02-06 16:56:11.825721'),(8,'auth','0003_alter_user_email_max_length','2024-02-06 16:56:12.291403'),(9,'auth','0004_alter_user_username_opts','2024-02-06 16:56:12.327772'),(10,'auth','0005_alter_user_last_login_null','2024-02-06 16:56:12.634445'),(11,'auth','0006_require_contenttypes_0002','2024-02-06 16:56:12.687500'),(12,'auth','0007_alter_validators_add_error_messages','2024-02-06 16:56:12.738591'),(13,'auth','0008_alter_user_username_max_length','2024-02-06 16:56:13.069679'),(14,'auth','0009_alter_user_last_name_max_length','2024-02-06 16:56:13.403743'),(15,'auth','0010_alter_group_name_max_length','2024-02-06 16:56:13.819803'),(16,'auth','0011_update_proxy_permissions','2024-02-06 16:56:13.847177'),(17,'auth','0012_alter_user_first_name_max_length','2024-02-06 16:56:14.166378'),(18,'botApp','0001_initial','2024-02-06 16:56:16.852472'),(19,'sessions','0001_initial','2024-02-06 16:56:17.092572'),(20,'botApp','0002_tipo_usuario_remove_audio_fono_fecha_ingreso_fono_and_more','2024-02-07 19:25:07.157930'),(21,'botApp','0003_alter_usuario_tipo_usuario','2024-02-07 19:25:07.351813'),(22,'botApp','0004_rename_usuario_usuariobot','2024-02-07 19:25:07.421834'),(23,'botApp','0005_remove_usuariobot_audio_fono_and_more','2024-02-07 19:25:07.583438'),(24,'botApp','0006_alter_usuariobot_id','2024-02-07 19:25:07.632236'),(25,'botApp','0007_alter_usuariobot_id','2024-02-07 19:25:07.683673'),(26,'botApp','0008_audio_fono_id_paciente_ingresado','2024-02-07 19:25:07.719926'),(27,'botApp','0009_alter_audio_fono_ano_nac_and_more','2024-02-07 19:25:07.732368'),(28,'botApp','0010_remove_audio_fono_id_paciente_ingresado_and_more','2024-02-07 20:59:18.775947'),(29,'botApp','0011_audio_persona_id_fono','2024-02-08 12:42:47.298757'),(30,'botApp','0012_remove_audio_persona_id_fono','2024-02-08 12:42:47.460823'),(31,'botApp','0013_audio_fono_id_fono','2024-02-08 12:42:47.731876'),(32,'botApp','0014_rename_id_fono_audio_fono_id_usuario','2024-02-09 16:33:47.493749'),(33,'botApp','0015_audio_fono_nombre_paciente','2024-02-19 15:38:38.738187'),(34,'botApp','0016_alter_audio_etiqueta_nombre_etiqueta','2024-02-19 15:38:38.775232'),(35,'botApp','0017_audio_fono_otras_enfermedades','2024-02-19 15:38:39.067777'),(36,'botApp','0018_enfermedad_remove_audio_fono_otras_enfermedades_and_more','2024-02-19 15:38:40.503271'),(37,'botApp','0019_audio_fono_audio_fo2_audio_fono_audio_fo3_and_more','2024-02-19 15:38:40.847138'),(38,'botApp','0020_remove_audio_fono_otras_enfermedades_and_more','2024-02-19 15:38:41.094861'),(39,'botApp','0021_audio_fono_otras_enfermedades','2024-02-19 20:40:15.830935'),(40,'botApp','0022_rename_audio_etiqueta_tipo_diagnostico_flgo_and_more','2024-02-20 13:15:38.520727'),(41,'botApp','0023_remove_tipo_diagnostico_flgo_nombre_etiqueta_and_more','2024-02-20 13:15:38.763442');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('47qm388edycrea3pcbiv95l8kfga4z93','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rXgHw:XzuF289hKpAww9hMx7phpT3ooCwe7Pp2gRGLgOrgkxA','2024-02-21 11:40:24.976462'),('6ujj9015t6r1yhzpnif0cgu859kxmequ','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rZs5P:-gM0OZF5N2dJiIblvwxxbmRmwPJVfaYq7oc90hCoUYk','2024-02-27 12:40:31.208970'),('8ty24ra3l3q8a6l9ohtlubmz8hy0g21g','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rYVeh:wpCtqkSCG4undspISXL9bK8r2Bh5UNH8QbEN1xn3q8g','2024-02-23 18:31:19.913680'),('ea5bi6tcrkjbyprsfwj1kttuy4bpydzj','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rc5jg:kD6ZXUHXA0XJysPhKmh3ZXSPOudyu8unE3NnLhBiNc8','2024-03-04 15:39:16.628832'),('ecexfypp55ot2h58omt0t1l8qqno84ls','.eJxVjEsOwjAMBe-SNYpsp40cluw5QxXHCSmgVOpnhbg7VOoCtm9m3ssMcVvrsC15HkY1Z0Pm9LtJTI_cdqD32G6TTVNb51HsrtiDLvY6aX5eDvfvoMalfmsUx95BYY6pcIAUMyB2fQpJGLBkyagOyZP2RApOCQOxgLB66Lx5fwDbbzdX:1rY31v:h399eGq0eXP9eRBIoBMF7wX103ZVU1t2YXOkoWwq8L0','2024-02-22 11:57:23.976213'),('fx7wx0b7br84mgc35hnu33tf5wxl41a7','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rXgJW:RhKDxLIyJM9barYlTstkdWYHIrjvXc1Q53esCksEdYE','2024-02-21 11:42:02.505349'),('j1mam085zfnua6h66gq9lamf2bwptbcf','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rXgHL:5foSZdUcfQLTKzqNbPN4XwQBN8SZO3KU6BV9MNFa1gU','2024-02-21 11:39:47.305798'),('m4ummhjbycksduf6cudb0v656uvtnuwj','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rcky7:rrA_UKSSaVC0SKdZxRhfPElBeyuOlz6IGRDEtH1fNZA','2024-03-06 11:40:55.590574'),('rw597tt40jt96hznwbt9fmaakiv79qay','.eJxVjDsOwjAQBe_iGlmJP2uHkj5nsHbXDg4gW4qTCnF3EikFtDPz3lsE3NYctpaWMEdxFUZcfhkhP1M5RHxguVfJtazLTPJI5GmbHGtMr9vZ_h1kbHlfAxunFSoCa3uCPgFPQNpFo1VKntjtUFlvgcl1fuqU8aCGATUjM1rx-QLT8zei:1rc3eE:TCgR00pqzBZ92bd-pXjH3ZGwTEKqRtz7QrWtB-m13hs','2024-03-04 13:25:30.769420'),('sl2dfavtpyaznxkivbhma4tjx1mp6qw6','.eJxVjDsOwjAQBe_iGlmJP2uHkj5nsHbXDg4gW4qTCnF3EikFtDPz3lsE3NYctpaWMEdxFUZcfhkhP1M5RHxguVfJtazLTPJI5GmbHGtMr9vZ_h1kbHlfAxunFSoCa3uCPgFPQNpFo1VKntjtUFlvgcl1fuqU8aCGATUjM1rx-QLT8zei:1rcU46:CI8aOx2z_04eEjaGR_2VQGQc-HByfLWde_R3uBjzE4U','2024-03-05 17:37:58.562206'),('vce5gxln6gbszea4klw955e3frp8gbdn','.eJxVjEsOwjAMBe-SNYpsp40cluw5QxXHCSmgVOpnhbg7VOoCtm9m3ssMcVvrsC15HkY1Z0Pm9LtJTI_cdqD32G6TTVNb51HsrtiDLvY6aX5eDvfvoMalfmsUx95BYY6pcIAUMyB2fQpJGLBkyagOyZP2RApOCQOxgLB66Lx5fwDbbzdX:1rY6Fx:_nsMQoVatho7Dj9mUAvfJs_Ve7eBxQJH40n-b1wphss','2024-02-22 15:24:05.739510'),('zwmch1wroskstgf41qrq77p216y9nnbm','.eJxVjE0OwiAYBe_C2hCgIMWle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvWz0oHywFMKT5HLwylNkhZw4IeUBHPOKY9cBWWVTk2bOzJqFXyatNFZ8v_Go4vw:1rcAdF:tbUnMhLJYBXgLFYzG_qGF_FSDklheJ_jbw3Z8Fql9_A','2024-03-04 20:52:57.052181');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-21 12:10:38
