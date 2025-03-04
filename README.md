# House Price Prediction

## Overview

This project is a web-based application that predicts house prices based on user inputs using a machine learning model. The application is built using Flask as the backend framework, with a trained machine learning model for predictions.

## Features

- User-friendly web interface for inputting house details
- Machine learning model to predict house prices
- Flask-based backend for handling requests and predictions
- Interactive and responsive UI
- Scalable and easily deployable

## Tech Stack

- **Backend:** Flask, Python
- **Frontend:** HTML, CSS, Bootstrap
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Database (Optional):** SQLite/PostgreSQL

## Installation

### Prerequisites

Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/amandange2001/house-price-prediction.git
   cd house-price-prediction
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open the browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

- Enter house features such as size, location, number of bedrooms, and bathrooms.
- Click the **Predict** button.
- The application will display the estimated house price.

## Project Structure

```
house-price-prediction/
│── templates/          # HTML templates for frontend
│── static/             # CSS, JS, and assets
│── models/             # Trained ML models
│── app.py              # Flask application
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

## Future Enhancements

- Integrate real-time data sources for better predictions
- Deploy on cloud platforms like AWS, Heroku, or Azure
- Improve UI/UX with interactive charts

## License

This project is open-source and available under the MIT License.

## Contact

For any queries or contributions, feel free to reach out:

- **GitHub:** [amandange2001](https://github.com/amandange2001)
- **Email:** [amandange2018@gmail.com](mailto\:amandange2018@gmail.com)

