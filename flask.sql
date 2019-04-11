-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 11, 2019 at 05:26 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nom` varchar(60) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `tel` varchar(12) NOT NULL,
  `email` varchar(80) DEFAULT NULL,
  `date_inscription` date NOT NULL,
  `password` varchar(200) NOT NULL,
  `compte` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `nom`, `prenom`, `tel`, `email`, `date_inscription`, `password`, `compte`) VALUES
(9, 'ISSOUFOU', 'Djibril', '80686719', 'issoufoudjib@gmail.com', '2019-04-11', 'ccc9c73a37651c6b35de64c3a37858ccae045d285f57fffb409d251d', 'root'),
(10, 'Sani', 'Ibrahim', '1234', '', '2019-04-11', 'ccc9c73a37651c6b35de64c3a37858ccae045d285f57fffb409d251d', 'normal'),
(12, 'Le NOM', 'Le Prenom', '227', '', '2019-04-11', 'ccc9c73a37651c6b35de64c3a37858ccae045d285f57fffb409d251d', 'root');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tel` (`tel`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
