# Podio Frontend

## Overview
This is the frontend for the Podio Task Management application. It is built with React, TypeScript, and Tailwind CSS, and uses Vite as the build tool.

## Prerequisites
- Node.js 18+ installed
- Docker and Docker Compose installed

## Start the Project Locally
1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```
4. Access the application at `http://localhost:5173`.

## Build for Production
1. Build the production-ready files:
   ```sh
   npm run build
   ```
2. Preview the production build:
   ```sh
   npm run preview
   ```

## Run with Docker
1. Build the Docker image:
   ```sh
   docker build -t podio-frontend .
   ```
2. Run the container:
   ```sh
   docker run -p 80:80 podio-frontend
   ```
3. Access the application at `http://localhost`.

## Linting
1. Run ESLint to check for code issues:
   ```sh
   npm run lint
   ```

## Project Structure
- `src/`: Contains the source code for the application.
- `index.html`: The entry point for the application.
- `tailwind.config.js`: Tailwind CSS configuration.
- `vite.config.ts`: Vite configuration.
