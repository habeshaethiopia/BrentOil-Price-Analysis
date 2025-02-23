# BrentOil-Price-Analysis
This repository analyzes how major political and economic events impact Brent oil prices. Using historical data (1987–2022), it applies statistical modeling, Bayesian inference, and machine learning to provide insights for investors and policymakers.

## Project Structure
- **data/**: Contains raw and processed data.
  - **raw/**: Stores raw, unprocessed data, such as historical Brent oil prices.
  - **processed/**: Contains cleaned and preprocessed data.
  
- **notebooks/**: Jupyter notebooks for data exploration and analysis.
  - **analysis.ipynb**: Initial data exploration and analysis notebook.
  
- **src/**: Source code for the project.
  - **backend/**: Flask backend application.
    - **app.py**: Main Flask application code.
    - **requirements.txt**: Python dependencies for the backend.
  - **frontend/**: React frontend application.
    - **public/**: Static files for the React frontend.
    - **src/**: Source files for the React application.
      - **App.js**: Main React component.
      - **index.js**: Entry point for the React application.
  
- **reports/**: Final report or documentation of the analysis.
  - **report.md**: Contains the final report.
  
- **docs/**: Project documentation and instructions.
  - **documentation.md**: Provides project documentation.
  
- **.gitignore**: Specifies files and directories to be ignored by Git.

- **README.md**: Overview of the project and instructions for setup and usage.

- **setup.py**: Used for packaging the project and specifying dependencies.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd BrentOil-Price-Analysis
   ```
3. Install the required dependencies:
   ```
   pip install -r src/backend/requirements.txt
   ```

## Usage
- To run the Flask backend, execute:
  ```
  python src/backend/app.py
  ```
- For the React frontend, navigate to the `src/frontend` directory and run:
  ```
  npm start
  ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.