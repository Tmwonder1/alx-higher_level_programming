# Introduction to SQL

## Project Overview
This project is designed for beginners to understand the basics of Structured Query Language (SQL), the standard language for relational database management systems. SQL statements are used to perform tasks such as update data on a database, or retrieve data from a database.

## Learning Objectives
- Understand what SQL and databases are.
- Learn how to create and manipulate databases.
- Perform CRUD (Create, Read, Update, Delete) operations on database tables.
- Understand how to use simple queries to filter and sort data.

## Prerequisites
Before you begin this course, ensure you have:
- Installed a SQL database system like MySQL, PostgreSQL, or SQLite.
- Basic knowledge of how databases work.

## Installation Guide
1. **MySQL Installation:**
   - Windows: Download from [MySQL official website](https://dev.mysql.com/downloads/mysql/) and follow the installation instructions.
   - MacOS/Linux: Use a package manager like `brew` or `apt` to install MySQL.
   - `brew install mysql` (MacOS)
   - `sudo apt-get install mysql-server` (Linux)

2. **SQLite Installation:**
   - Most operating systems come with SQLite pre-installed. If you need to install it, follow instructions on [SQLite's download page](https://sqlite.org/download.html).

## SQL Basics
Here are some of the fundamental concepts and operations you'll learn:

### Databases and Tables
- **Creating a database:** `CREATE DATABASE example;`
- **Switching databases:** `USE example;`
- **Creating a table:**
  ```sql
  CREATE TABLE users (
    id INT AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    PRIMARY KEY (id)
  );
