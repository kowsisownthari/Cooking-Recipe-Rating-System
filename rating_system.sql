-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 25, 2024 at 12:18 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rating_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `chef_register`
--

CREATE TABLE `chef_register` (
  `id` int(20) NOT NULL,
  `chefName` varchar(20) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `phno` varchar(10) NOT NULL,
  `gender` varchar(8) NOT NULL,
  `DOB` varchar(15) NOT NULL,
  `Doorno` varchar(10) NOT NULL,
  `Address1` varchar(30) NOT NULL,
  `Address2` varchar(30) NOT NULL,
  `city` varchar(10) NOT NULL,
  `state` varchar(10) NOT NULL,
  `country` varchar(15) NOT NULL,
  `Restaurant` varchar(30) NOT NULL,
  `currentrole` varchar(20) NOT NULL,
  `Experience` varchar(10) NOT NULL,
  `cuisine` varchar(15) NOT NULL,
  `IDProof` varchar(100) NOT NULL,
  `profile` varchar(100) NOT NULL,
  `IDCard` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  `chef_id` varchar(10) NOT NULL,
  `designation` varchar(20) NOT NULL,
  `password` varchar(15) NOT NULL,
  `admin_status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chef_register`
--

INSERT INTO `chef_register` (`id`, `chefName`, `Email`, `phno`, `gender`, `DOB`, `Doorno`, `Address1`, `Address2`, `city`, `state`, `country`, `Restaurant`, `currentrole`, `Experience`, `cuisine`, `IDProof`, `profile`, `IDCard`, `status`, `chef_id`, `designation`, `password`, `admin_status`) VALUES
(1, 'Kaushalya ', 'kowsiudayakumar@gmail.com', '0934541118', 'FEMALE', '2024-10-14', 'PSRF,Tante', 'Coonoor', 'Nehru Nagar', 'Coonoor', 'Tamilnadu', 'India', 'FoodIn', 'Senior chef', '4', 'Indian', 'download (21).jpeg', 'download (25).jpeg', 'images (14).jpeg', 'Accept', 'chef2734', 'chef', '', ''),
(3, 'Thiya', 'kowsisowthari@gmail.com', '8765468908', 'FEMALE', '2024-10-21', '35/D/1,Sam', 'NSR Roard', 'Saibaba Colony', 'Avissawell', 'Tamilnadu', 'Sri Lanka', 'Flavour Heaven', 'Baker', '4', 'Chinese', 'download (20).jpeg', 'images (9).jpeg', 'images (15).jpeg', 'Reject', '', 'chef', '', ''),
(4, 'dhivya', 'c.dhivyasakthi@gmail.com', '9876549999', 'FEMALE', '2024-10-09', '26', '7th Street', 'ghandhipuram', 'Coimbatore', 'Tamilnadu', 'India', 'Eat and Treat', 'Pastry Chef', '5', 'Indian', 'download (19).jpeg', 'images (10).jpeg', 'images (16).jpeg', 'Accept', 'chef2735', '', '9999', 'passchanged');

-- --------------------------------------------------------

--
-- Table structure for table `food_recipes`
--

CREATE TABLE `food_recipes` (
  `recipeid` int(10) NOT NULL,
  `Recipe_Name` varchar(20) NOT NULL,
  `Steps` varchar(100) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `mainCategory` varchar(20) NOT NULL,
  `subCategory` varchar(20) NOT NULL,
  `ingredients` varchar(40) NOT NULL,
  `quantities` varchar(100) NOT NULL,
  `keyword` varchar(20) NOT NULL,
  `status` varchar(50) NOT NULL,
  `video` varchar(100) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `cookery_id` varchar(10) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `designation` varchar(20) NOT NULL,
  `Posted_Recipe_Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food_recipes`
--

INSERT INTO `food_recipes` (`recipeid`, `Recipe_Name`, `Steps`, `duration`, `mainCategory`, `subCategory`, `ingredients`, `quantities`, `keyword`, `status`, `video`, `Name`, `cookery_id`, `Email`, `designation`, `Posted_Recipe_Status`) VALUES
(3, 'Chicken Rice', 'add water,chicken with rice,add masala,after ten minute ready to serve', '10 min', 'meat', 'chicken', 'rice,chicken,water', '500kg,250gm,10ml', 'Fried', 'Reject', 'chicken rice.mp4', 'Kaushalya', 'chef2734', 'c.dhivyasakthi@gmail.com', 'chef', ''),
(4, 'Fish fry', 'take fish and clean it fully,add masala which is shown in video,keep it for 10  min and take tawa,pu', '15 min', 'seafood', 'shellfish', ',fish fry masala', '1,1 spoon', 'Dessert', 'pendingrecipe', 'fish fry.mp4', 'Kaushalya', 'chef2734', 'c.dhivyasakthi@gmail.com', 'chef', ''),
(14, 'Fish Gravy', 'add oil and other ingredients,add fish and masala,after 20 min ready to serve', '45 min', 'meat', 'veal', 'fish,masala', '500gm,1 spoon', 'Curry', 'Accept', 'fish gravy.mp4', 'Kaushalya', 'chef2734', 'c.dhivyasakthi@gmail.com', 'chef', ''),
(22, 'Noodles', 'Take vessel add water and noodle ,take other vessels add some oil and add vegetables,add cooked nood', '20 min', 'grains', 'spelt', 'noodle,onion', '1 packet,1', 'noodles', 'Reject', 'noodle.mp4', 'Kaushalya', 'chef2734', 'c.dhivyasakthi@gmail.com', 'chef', ''),
(26, 'Chicken Chilli', 'take cleaned chicken,Add masala like chicken chilli masala and salt ,put some some water and mix it,', '10 min', 'meat', 'chicken', 'chicken,masala', '100g,1 spoon', 'Dessert', 'Accept', 'chilli chicken.mp4', 'Kalai', '1', 'kowsisowthari@gmail.com', 'visitor', ''),
(27, 'Chapathi', 'take wheat flour,add some water and mix it,take tawa add put in tawa,its reday', '20 min', 'grains', 'wheat', 'wheat,water', '250 gm,1 spoon', 'Salad', 'High Rated', 'chappathi.mp4', 'Kalai', '1', 'kowsisowthari@gmail.com', 'visitor', ''),
(28, 'Maggi', 'take water let it boil,add maggi,Add masala', '20 min', 'vegetables', 'onions', 'Maggi', '1 packet', 'maggi', 'High Rated', 'maggi.mp4', 'Kalai', '1', 'kowsisowthari@gmail.com', 'visitor', ''),
(29, 'Dosa', 'take dosa batter,put in tawa as shown in video,it should be in round shape add gee', '5 min', 'grians', 'rice flour', 'dosa batter,gee', '1 scope,1 spoon', 'Salad', 'Low Rated', 'dosa.mp4', 'kavyasri', 'tech9426', 'kowsisowthari@gmail.com', 'student', ''),
(30, 'Fried Rice', 'take fried chicken,add boiled rice with some vegetable,add that chicken also', '45 min', 'meat', 'chicken', 'chicken,rice', '250gm,500gm', 'noodles', 'Accept', 'fried rice veg.mp4', 'kavyasri', 'tech9426', 'kowsisowthari@gmail.com', 'student', ''),
(31, 'tomato Gravy', 'take tomato ,put onion and tomato in oil ,add masala', '20 min', 'vegetables', 'tomatoes', 'tamoto,onion,water', '2 ,1,', 'Salad', 'Reject', 'tomato gravy.mp4', 'kavyasri', 'tech9426', 'kowsisowthari@gmail.com', 'student', ''),
(32, 'Chinese Chicken', 'grind the cashew nut and take garlic and ginger paste,take clean chicken add  salt,milk,grind cashew', '30 minutes', 'meat', 'chicken', 'chicken,gee,spices,cheese', '250gm,1 spoon,as needed,1 pack', 'Dessert', 'Low Rated', 'chinese chicken.mp4', 'kavyasri', 'tech9426', 'kavya023@gmail.com', 'student', '');

-- --------------------------------------------------------

--
-- Table structure for table `keywords`
--

CREATE TABLE `keywords` (
  `id` int(10) NOT NULL,
  `keyword` varchar(200) NOT NULL,
  `custom_keyword` varchar(600) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `keywords`
--

INSERT INTO `keywords` (`id`, `keyword`, `custom_keyword`) VALUES
(1, 'Salad', ''),
(2, 'noodles', ''),
(3, 'maggi', ''),
(4, 'Dessert', ''),
(5, 'Italian', ''),
(6, 'Chinese', ''),
(7, 'Mexican', ''),
(8, 'Fried', ''),
(9, 'Baked', ''),
(10, 'Gravy', ''),
(11, 'sauteed vegetables', '');

-- --------------------------------------------------------

--
-- Table structure for table `recipe_ratings`
--

CREATE TABLE `recipe_ratings` (
  `id` int(10) NOT NULL,
  `chefName` varchar(20) NOT NULL,
  `recipeid` varchar(10) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `comment` varchar(100) NOT NULL,
  `chefid` varchar(10) NOT NULL,
  `designation` varchar(10) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `recipe_ratings`
--

INSERT INTO `recipe_ratings` (`id`, `chefName`, `recipeid`, `rating`, `comment`, `chefid`, `designation`, `status`) VALUES
(2, 'Kaushalya', '32', '3', 'bad', 'chef2734', 'chef', 'Low Rated'),
(14, 'Kaushalya', '30', '2', 'not good', 'chef2734', 'chef', 'Low Rated'),
(28, 'Kaushalya', '30', '2', 'poor video quality', 'chef2734', 'chef', 'Low Rated'),
(31, 'dhivya', '31', '2', 'can improve better', 'chef2735\n', 'chef', ''),
(32, 'Kaushalya', '32', '2', 'improve', 'chef2734', 'chef', 'Low Rated'),
(33, 'Kalai', '31', '2', 'no clear info', 'chef2734', 'chef', ''),
(37, 'Kaushalya', '26', '4', 'good', 'chef2734', 'chef', 'High Rated'),
(38, 'Kaushalya', '26', '5', 'Excellent', 'chef2734', '', 'High Rated'),
(44, 'dhivya', '32', '2', 'Can improve', 'chef2735', 'chef', 'Low Rated'),
(45, 'Kaushalya ', '27', '4', 'Nice', 'chef2734', 'chef', 'High Rated'),
(46, 'Kaushalya ', '28', '3', 'good', 'chef2734', 'chef', 'High Rated'),
(51, 'dhivya', '29', '3', 'Nice', 'chef2735', 'chef', 'Low Rated'),
(52, 'Kaushalya ', '29', '2', 'gud', 'chef2734', 'chef', 'Low Rated');

-- --------------------------------------------------------

--
-- Table structure for table `student_register`
--

CREATE TABLE `student_register` (
  `id` int(10) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `phno` varchar(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `DOB` varchar(15) NOT NULL,
  `Doorno` varchar(10) NOT NULL,
  `Address1` varchar(20) NOT NULL,
  `Address2` varchar(20) NOT NULL,
  `city` varchar(10) NOT NULL,
  `state` varchar(18) NOT NULL,
  `country` varchar(15) NOT NULL,
  `Restaurant` varchar(15) NOT NULL,
  `TrainingType` varchar(20) NOT NULL,
  `TrainingPeriod` varchar(15) NOT NULL,
  `Location` varchar(15) NOT NULL,
  `IDProof` varchar(50) NOT NULL,
  `profile` varchar(50) NOT NULL,
  `IDCard` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `cookery_id` varchar(20) NOT NULL,
  `designation` varchar(20) NOT NULL,
  `admin_status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_register`
--

INSERT INTO `student_register` (`id`, `Name`, `Email`, `phno`, `gender`, `DOB`, `Doorno`, `Address1`, `Address2`, `city`, `state`, `country`, `Restaurant`, `TrainingType`, `TrainingPeriod`, `Location`, `IDProof`, `profile`, `IDCard`, `status`, `password`, `cookery_id`, `designation`, `admin_status`) VALUES
(2, 'Kalai', 'kowsiudayakumar@gmail.com', '0934541118', '2024-10-25', 'FEMALE', 'PSRF,Tante', 'PSRF', 'nonsuch', 'Kotagiri', 'None', 'India', 'chef inn', 'Baking', '10 months', 'coimbatore', 'download (22).jpeg', 'download (13).jpeg', 'download (24).jpeg', 'Registered', '', '', 'student', ''),
(3, 'kavyasri', 'kavya023@gmail.com', '8790876567', '2024-10-14', 'FEMALE', 'PSRF', 'Tantea Estate', 'Tantea', 'Coonoor', 'Tamilnadu', 'India', 'grillday', 'Marriott', '12 months', 'chennai', 'download (23).jpeg', 'download (14).jpeg', 'images (12).jpeg', 'Accept', '00000', 'tech9426', 'student', ''),
(4, 'kavitha', 'kowsisowthari@gmail.com', '7890765789', '2024-09-30', 'FEMALE', 'Tante', '7TH Street', 'Dehigahapitiya', 'Mettupalay', 'Tamilnadu', 'India', 'Hilton Hotel', 'Knife Skills', '6 months', 'erode', 'images (11).jpeg', 'download (15).jpeg', 'images (13).jpeg', 'Reject', '', '', 'student', '');

-- --------------------------------------------------------

--
-- Table structure for table `visitor_register`
--

CREATE TABLE `visitor_register` (
  `id` int(10) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `phno` varchar(10) NOT NULL,
  `DOB` varchar(15) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `Doorno` varchar(10) NOT NULL,
  `Address1` varchar(20) NOT NULL,
  `Address2` varchar(25) NOT NULL,
  `city` varchar(10) NOT NULL,
  `state` varchar(15) NOT NULL,
  `country` varchar(15) NOT NULL,
  `worksector` varchar(20) NOT NULL,
  `cuisine` varchar(15) NOT NULL,
  `password` varchar(10) NOT NULL,
  `IDProof` varchar(50) NOT NULL,
  `profile` varchar(50) NOT NULL,
  `designation` varchar(20) NOT NULL,
  `admin_status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `visitor_register`
--

INSERT INTO `visitor_register` (`id`, `Name`, `Email`, `phno`, `DOB`, `gender`, `Doorno`, `Address1`, `Address2`, `city`, `state`, `country`, `worksector`, `cuisine`, `password`, `IDProof`, `profile`, `designation`, `admin_status`) VALUES
(1, 'Kalai', 'kowsisowthari@gmail.com', '9345411189', 'MALE', '2024-10-29', 'PSRF,Tante', 'Coonoor', 'Tantea', 'Coonoor', 'Tamilnadu', 'India', 'manufacturing', 'Chinese', '0301', 'download (18).jpeg', 'download (16).jpeg', 'visitor', ''),
(2, 'Maya', 'kaushalyaudayakumar@gmail.com', '8976544689', 'FEMALE', '2001-06-19', '23', 'saibaba kovil', '1st street', 'coimbatore', 'Tamilnadu', 'India', 'healthcare', 'Indian', '98765', 'images (11).jpeg', 'images (9).jpeg', 'visitor', '');

-- --------------------------------------------------------

--
-- Table structure for table `wishlist_recipe`
--

CREATE TABLE `wishlist_recipe` (
  `id` int(10) NOT NULL,
  `recipeid` varchar(10) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Added_byid` varchar(20) NOT NULL,
  `Added_ByDesignation` varchar(20) NOT NULL,
  `Posted_Recipe_Status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wishlist_recipe`
--

INSERT INTO `wishlist_recipe` (`id`, `recipeid`, `Name`, `Added_byid`, `Added_ByDesignation`, `Posted_Recipe_Status`) VALUES
(1, '3', 'Kaushalya', 'chef2734', 'chef', 'wishlist'),
(2, '3', 'Kalai', '1', 'visitor', 'wishlist'),
(3, '26', 'Kaushalya ', 'chef2734', 'chef', 'wishlist'),
(4, '14', 'kavyasri', 'tech9426', 'student', 'wishlist'),
(5, '14', 'kavyasri', 'tech9426', 'student', 'Removed');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chef_register`
--
ALTER TABLE `chef_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `food_recipes`
--
ALTER TABLE `food_recipes`
  ADD PRIMARY KEY (`recipeid`);

--
-- Indexes for table `keywords`
--
ALTER TABLE `keywords`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recipe_ratings`
--
ALTER TABLE `recipe_ratings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_register`
--
ALTER TABLE `student_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `visitor_register`
--
ALTER TABLE `visitor_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wishlist_recipe`
--
ALTER TABLE `wishlist_recipe`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chef_register`
--
ALTER TABLE `chef_register`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `food_recipes`
--
ALTER TABLE `food_recipes`
  MODIFY `recipeid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `keywords`
--
ALTER TABLE `keywords`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `recipe_ratings`
--
ALTER TABLE `recipe_ratings`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `student_register`
--
ALTER TABLE `student_register`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `visitor_register`
--
ALTER TABLE `visitor_register`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `wishlist_recipe`
--
ALTER TABLE `wishlist_recipe`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
