# Task Management Application

## Overview
This application allows users to create, assign, and track tasks. It includes:
- A React front-end
- A Flask RESTful API backend
- A MySQL database

## Things to improve the application
  - Add paging to some of the requests
  - User login
  - Add https for the hosting
  - Indexes for tasks table on the assigned_to column
  - Setup CI/CD
  - Migrations
  - Use yarn as package manager
  - Extract the api url inside .env file

## Start the Application
1. Ensure Docker and Docker Compose are installed.
2. Copy `.env.example` to `.env`:
   ```sh
   cp .env.example .env
   ```
3. Start the application:
   ```sh
   docker-compose up --build
   ```
4. Access the application:
   - Frontend: [http://localhost](http://localhost)
   - Backend API: [http://localhost:5000](http://localhost:5000)
5. Stop the application:
   ```sh
   docker-compose down
   ```