## 🏠 House Price Prediction Web App

#### 🚀 From Machine Learning Model to Production-Ready Web Application

This project showcases how a trained Machine Learning model can be transformed into a real-world, production-ready application by integrating it with a web interface and deploying it to the cloud.

Unlike typical ML projects that stop at model training in notebooks, this project emphasizes end-to-end product development, real-time predictions, and deployment for real users.

### 🌐 Live Demo
### 👉 Live Application: https://house-price-app-4-y1qc.onrender.com/

#### 🎯 Project Objective

The primary goal of this project was not to learn frontend or Flask basics, but to:

Convert a trained ML model into a real product
Expose predictions via a REST API
Connect frontend inputs to backend ML logic
Deploy and run the application for real users

#### 🧠 What This Project Covers
✔ Machine Learning model training
✔ Model serialization using .pkl
✔ Flask-based REST API
✔ Frontend integration (HTML, CSS, JavaScript)
✔ Real-time predictions
✔ Cloud deployment using Render
✔ Production server using Gunicorn

#### 🛠 Tech Stack
| Layer           | Technologies          |
| --------------- | --------------------- |
| Programming     | Python                |
| ML              | Scikit-learn          |
| Backend         | Flask                 |
| Frontend        | HTML, CSS, JavaScript |
| Server          | Gunicorn              |
| Deployment      | Render                |
| Version Control | Git & GitHub          |

#### 📁 Project Structure
House-Price-App/
├── app.py                  # Flask application
├── model.pkl               # Trained ML model
├── requirements.txt        # Dependencies
├── Procfile                # Render start command
├── templates/
│   └── index.html          # Frontend UI
└── README.md               # Project documentation

#### ⚙️ How It Works
User enters house details via the web UI
JavaScript sends input data to /predict API
Flask backend:
Receives request
Loads trained ML model
Performs prediction
Predicted house price is returned and displayed on UI

☁️ Deployment

#### The application is deployed on Render using:
Gunicorn as the production server
GitHub-based CI/CD deployment
Any push to the main branch automatically triggers a redeploy.

#### 📌 Key Learning Outcomes
Understanding the gap between ML models and ML products
Building production-ready APIs
Debugging real deployment issues
Handling frontend–backend communication
Deploying ML applications for real users
