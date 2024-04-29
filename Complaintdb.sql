-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema complaints
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema complaints
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `complaints` DEFAULT CHARACTER SET utf8 ;
USE `complaints` ;

-- -----------------------------------------------------
-- Table `complaints`.`Course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `complaints`.`Course` (
  `Course id` INT NOT NULL AUTO_INCREMENT,
  `CourseName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Course id`),
  UNIQUE INDEX `CourseName_UNIQUE` (`CourseName` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `complaints`.`Student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `complaints`.`Student` (
  `StudMatricule` INT NOT NULL AUTO_INCREMENT,
  `StudName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`StudMatricule`),
  UNIQUE INDEX `StudName_UNIQUE` (`StudName` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `complaints`.`Major`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `complaints`.`Major` (
  `MajorCode` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`MajorCode`),
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `complaints`.`Complaint`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `complaints`.`Complaint` (
  `ComplaintID` INT NOT NULL AUTO_INCREMENT,
  `Status` VARCHAR(45) NOT NULL,
  `StudMatricule` INT NOT NULL,
  `Course id` INT NOT NULL,
  PRIMARY KEY (`ComplaintID`, `StudMatricule`, `Course id`),
  INDEX `fk_Complaint_Students1_idx` (`StudMatricule` ASC) VISIBLE,
  INDEX `fk_Complaint_Courses1_idx` (`Course id` ASC) VISIBLE,
  CONSTRAINT `fk_Complaint_Students1`
    FOREIGN KEY (`StudMatricule`)
    REFERENCES `complaints`.`Student` (`StudMatricule`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Complaint_Courses1`
    FOREIGN KEY (`Course id`)
    REFERENCES `complaints`.`Course` (`Course id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



