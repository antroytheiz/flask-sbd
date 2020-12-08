-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Dec 07, 2020 at 08:51 AM
-- Server version: 8.0.1-dmr
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `proyek_2`
--

-- --------------------------------------------------------

--
-- Table structure for table `DataLapor`
--

CREATE TABLE `DataLapor` (
  `nama` varchar(5) DEFAULT NULL,
  `kejadian` varchar(10) DEFAULT NULL,
  `nomorHP` bigint(11) DEFAULT NULL,
  `lembagaBerwenang` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `DataLapor`
--

INSERT INTO `DataLapor` (`nama`, `kejadian`, `nomorHP`, `lembagaBerwenang`) VALUES
('theis', 'kehilangan', 85231370385, 'ITS');

-- --------------------------------------------------------

--
-- Table structure for table `MedcenITS`
--

CREATE TABLE `MedcenITS` (
  `KTP` int(50) DEFAULT NULL,
  `alamatKantor` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `MedcenITS`
--

INSERT INTO `MedcenITS` (`KTP`, `alamatKantor`) VALUES
(9103, 'Sukolilo');

-- --------------------------------------------------------

--
-- Table structure for table `NomorLayanan`
--

CREATE TABLE `NomorLayanan` (
  `kodePolsek` int(4) DEFAULT NULL,
  `nomorLayananPolsek` int(4) DEFAULT NULL,
  `nomorLayananMedcen` int(4) DEFAULT NULL,
  `nomorDaruratPolsek` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `NomorLayanan`
--

INSERT INTO `NomorLayanan` (`kodePolsek`, `nomorLayananPolsek`, `nomorLayananMedcen`, `nomorDaruratPolsek`) VALUES
(9102, 8082, 8081, 808);

-- --------------------------------------------------------

--
-- Table structure for table `Polsek`
--

CREATE TABLE `Polsek` (
  `kodePolsek` int(50) NOT NULL,
  `KTP` int(50) DEFAULT NULL,
  `alamatKantor` varchar(100) DEFAULT NULL,
  `namaPolsek` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Polsek`
--

INSERT INTO `Polsek` (`kodePolsek`, `KTP`, `alamatKantor`, `namaPolsek`) VALUES
(9102, 9103, 'Jayapura', 'Polsek Sentani barat');

-- --------------------------------------------------------

--
-- Table structure for table `Pribadi`
--

CREATE TABLE `Pribadi` (
  `NRP` int(50) NOT NULL,
  `KTP` int(50) DEFAULT NULL,
  `KK` int(50) DEFAULT NULL,
  `STNK` int(50) DEFAULT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `nomorHP` bigint(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Pribadi`
--

INSERT INTO `Pribadi` (`NRP`, `KTP`, `KK`, `STNK`, `nama`, `alamat`, `nomorHP`) VALUES
(5211, 9103, 910304, 6758, 'theis', 'jayapura', 85231370385);

-- --------------------------------------------------------

--
-- Table structure for table `ProsedurLapor`
--

CREATE TABLE `ProsedurLapor` (
  `kodePolsek` int(4) DEFAULT NULL,
  `prosedurLaporPolsek` varchar(4) DEFAULT NULL,
  `prosedurLaporMedcen` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ProsedurLapor`
--

INSERT INTO `ProsedurLapor` (`kodePolsek`, `prosedurLaporPolsek`, `prosedurLaporMedcen`) VALUES
(9102, 'Test', 'Test');

-- --------------------------------------------------------

--
-- Table structure for table `WebsiteResmi`
--

CREATE TABLE `WebsiteResmi` (
  `kodePolsek` int(4) DEFAULT NULL,
  `WebsiteResmiMedcen` varchar(4) DEFAULT NULL,
  `WebsiteResmiPolsek` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `WebsiteResmi`
--

INSERT INTO `WebsiteResmi` (`kodePolsek`, `WebsiteResmiMedcen`, `WebsiteResmiPolsek`) VALUES
(9102, 'http', 'http');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `DataLapor`
--
ALTER TABLE `DataLapor`
  ADD UNIQUE KEY `nomorHP` (`nomorHP`),
  ADD KEY `nama` (`nama`);

--
-- Indexes for table `MedcenITS`
--
ALTER TABLE `MedcenITS`
  ADD KEY `KTP` (`KTP`);

--
-- Indexes for table `NomorLayanan`
--
ALTER TABLE `NomorLayanan`
  ADD KEY `kodePolsek` (`kodePolsek`);

--
-- Indexes for table `Polsek`
--
ALTER TABLE `Polsek`
  ADD PRIMARY KEY (`kodePolsek`),
  ADD KEY `KTP` (`KTP`);

--
-- Indexes for table `Pribadi`
--
ALTER TABLE `Pribadi`
  ADD PRIMARY KEY (`NRP`),
  ADD UNIQUE KEY `NRP` (`NRP`),
  ADD UNIQUE KEY `nomorHP` (`nomorHP`),
  ADD KEY `KTP` (`KTP`);

--
-- Indexes for table `ProsedurLapor`
--
ALTER TABLE `ProsedurLapor`
  ADD KEY `kodePolsek` (`kodePolsek`);

--
-- Indexes for table `WebsiteResmi`
--
ALTER TABLE `WebsiteResmi`
  ADD KEY `kodePolsek` (`kodePolsek`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `DataLapor`
--
ALTER TABLE `DataLapor`
  ADD CONSTRAINT `DataLapor_ibfk_1` FOREIGN KEY (`nomorHP`) REFERENCES `Pribadi` (`nomorHP`) ON UPDATE CASCADE;

--
-- Constraints for table `MedcenITS`
--
ALTER TABLE `MedcenITS`
  ADD CONSTRAINT `MedcenITS_ibfk_1` FOREIGN KEY (`KTP`) REFERENCES `Pribadi` (`KTP`) ON UPDATE CASCADE;

--
-- Constraints for table `NomorLayanan`
--
ALTER TABLE `NomorLayanan`
  ADD CONSTRAINT `NomorLayanan_ibfk_1` FOREIGN KEY (`kodePolsek`) REFERENCES `Polsek` (`kodePolsek`) ON UPDATE CASCADE;

--
-- Constraints for table `Polsek`
--
ALTER TABLE `Polsek`
  ADD CONSTRAINT `Polsek_ibfk_1` FOREIGN KEY (`KTP`) REFERENCES `Pribadi` (`KTP`) ON UPDATE CASCADE;

--
-- Constraints for table `ProsedurLapor`
--
ALTER TABLE `ProsedurLapor`
  ADD CONSTRAINT `ProsedurLapor_ibfk_1` FOREIGN KEY (`kodePolsek`) REFERENCES `Polsek` (`kodePolsek`) ON UPDATE CASCADE;

--
-- Constraints for table `WebsiteResmi`
--
ALTER TABLE `WebsiteResmi`
  ADD CONSTRAINT `WebsiteResmi_ibfk_1` FOREIGN KEY (`kodePolsek`) REFERENCES `Polsek` (`kodePolsek`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
