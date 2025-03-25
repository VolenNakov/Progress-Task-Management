# Podio Task Management

## Prerequisites
- Docker and Docker Compose installed
- Python 3.10+ installed (for running tests locally)

## Start the Project
1. Copy `.env.example` to `.env` in the root directory:
   ```sh
   cp .env.example .env
   ```
2. Start the services using Docker Compose:
   ```sh
   docker-compose up --build
   ```
3. Access the frontend at `http://localhost` and the backend API at `http://localhost:5000`.

## Set Up Virtual Environment (venv)
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment:
   ```sh
   python3 -m venv .venv
   ```
3. Activate the virtual environment:
   - On Linux/Mac:
     ```sh
     source .venv/bin/activate
     ```
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Run Tests
1. Ensure the virtual environment is activated.
2. Run the tests:
   ```sh
   python -m unittest discover -s tests
   ```
