/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - yacca sports city
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`yacca sports city` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `yacca sports city`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `s_id` int(11) NOT NULL,
  `f_id` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

/*Table structure for table `feedbackj` */

DROP TABLE IF EXISTS `feedbackj`;

CREATE TABLE `feedbackj` (
  `fd_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `message` varchar(50) NOT NULL,
  `datetime` datetime NOT NULL,
  PRIMARY KEY (`fd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedbackj` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `password` varchar(10) NOT NULL,
  `usertype` varchar(6) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_id` int(11) NOT NULL,
  `date time` datetime NOT NULL,
  `amount` double DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `registration` */

DROP TABLE IF EXISTS `registration`;

CREATE TABLE `registration` (
  `login_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(20) NOT NULL,
  `address` varchar(30) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `email` varchar(20) NOT NULL,
  `phone number` int(11) NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `registration` */

/*Table structure for table `request package` */

DROP TABLE IF EXISTS `request package`;

CREATE TABLE `request package` (
  `r_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `f_id` int(11) NOT NULL,
  `from` date NOT NULL,
  `to` date NOT NULL,
  `s_id` int(11) NOT NULL,
  `status` varchar(6) NOT NULL,
  PRIMARY KEY (`r_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `request package` */

/*Table structure for table `slot` */

DROP TABLE IF EXISTS `slot`;

CREATE TABLE `slot` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_id` int(11) NOT NULL,
  `time period` int(11) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `slot` */

/*Table structure for table `turf/court` */

DROP TABLE IF EXISTS `turf/court`;

CREATE TABLE `turf/court` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(10) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(60) NOT NULL,
  `image` blob NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `turf/court` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
