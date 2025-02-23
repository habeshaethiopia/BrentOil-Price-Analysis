# Brent Oil Price Analysis Documentation

## Project Overview
The Brent Oil Price Analysis project aims to analyze the impact of major political and economic events on Brent oil prices using historical data from 1987 to 2022. The project employs statistical modeling, Bayesian inference, and machine learning techniques to derive insights beneficial for investors and policymakers.

## Directory Structure
The project is organized into the following directories:

- **data/**: Contains raw and processed data.
  - **raw/**: Stores unprocessed historical Brent oil prices.
  - **processed/**: Contains cleaned and preprocessed data for analysis.

- **notebooks/**: Includes Jupyter notebooks for data exploration and analysis.
  - **analysis.ipynb**: The main notebook for initial data exploration.

- **src/**: Contains the source code for the project.
  - **backend/**: Holds the Flask backend application.
    - **app.py**: Main application code for the backend.
    - **requirements.txt**: Lists Python dependencies for the backend.
  - **frontend/**: Contains the React frontend application.
    - **public/**: Holds static files like `index.html`.
    - **src/**: Contains React components.
      - **App.js**: Main React component.
      - **index.js**: Entry point for the React application.

- **reports/**: Contains the final report of the analysis.
  - **report.md**: Documentation of the analysis findings.

- **docs/**: Provides project documentation and instructions.
  - **documentation.md**: Detailed project documentation.

## Installation Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd BrentOil-Price-Analysis
   ```

2. Install backend dependencies:
   ```
   pip install -r src/backend/requirements.txt
   ```

3. Set up the frontend:
   Navigate to the `src/frontend` directory and run:
   ```
   npm install
   ```

## Usage
- To run the Flask backend, execute:
  ```
  python src/backend/app.py
  ```

- To start the React frontend, navigate to the `src/frontend` directory and run:
  ```
  npm start
  ```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.