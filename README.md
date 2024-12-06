# Anomaly Detection in Stock Market Data  

This project demonstrates anomaly detection in stock market data using machine learning techniques. The workflow includes data preprocessing, model training, visualization of anomalies, application on test data, and optional deployment of the model as a user-friendly application.  

---

## Table of Contents  

1. [Project Overview](#project-overview)  
2. [Tasks Breakdown](#tasks-breakdown)  
   - [Task 1: Preprocessing of Training Data](#task-1-preprocessing-of-training-data)  
   - [Task 2: Training a Model](#task-2-training-a-model)  
   - [Task 3: Visualization of Anomalies](#task-3-visualization-of-anomalies)  
   - [Task 4: Applying the Model to the Test Dataset](#task-4-applying-the-model-to-the-test-dataset)  
   - [Brownie Task: Model Deployment](#brownie-task-model-deployment)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Technologies Used](#technologies-used)  
6. [Outputs](#outputs)  
7. [License](#license)  

---

## Project Overview  

This project focuses on detecting anomalies in stock market data, such as unexpected spikes or drops in prices. The end-to-end workflow includes:  
1. Preprocessing raw training and test datasets.  
2. Training an anomaly detection model.  
3. Visualizing detected anomalies.  
4. Applying the model to unseen test data.  
5. Deploying the model for practical use.  

---

## Tasks Breakdown  

### Task 1: Preprocessing of Training Data  

**Objective**: Clean and preprocess the provided training dataset.  
- **Input**: A dataset with columns: `date`, `open`, `high`, `low`, `close`, `volume`, `dividends`, `stock splits`.  
- **Steps**:  
  - Handle missing or inconsistent values.  
  - Perform feature engineering to create meaningful inputs.  
  - Scale or normalize features if required.  
- **Output**: A clean and preprocessed dataset ready for model training.  

---

### Task 2: Training a Model  

**Objective**: Train an anomaly detection model using the preprocessed data.  
- **Guidelines**:  
  - Use any machine learning or deep learning algorithm.  
  - Document model selection rationale, training process, and hyperparameter tuning.  
- **Output**: A trained model capable of detecting anomalies in stock market data.  

---

### Task 3: Visualization of Anomalies  

**Objective**: Visualize detected anomalies in the training data.  
- **Steps**:  
  - Split the dataset by year (2004–2024).  
  - Use Matplotlib, Seaborn, or Plotly for visualization.  
  - Highlight anomalies in clear, insightful plots.  
- **Output**: Year-wise plots showcasing detected anomalies in training data.  

---

### Task 4: Applying the Model to the Test Dataset  

**Objective**: Use the trained model to detect anomalies in the test dataset.  
- **Input**: Test dataset with columns: `date`, `company name`, `adj close`, `close`, `high`, `low`, `open`, `volume`.  
- **Output**: A CSV file listing `company name` and `date` for each detected anomaly.  

---

### Brownie Task: Model Deployment  

**Objective**: Deploy the anomaly detection model as a user-friendly application.  
- **Requirements**:  
  - The application should accept a CSV file as input and output detected anomalies.  
  - Use tools like Streamlit, Flask, or FastAPI for deployment.  
- **Output**:  
  - A demo video showcasing the deployment and its usage.  
  - Code for loading and using the model.  
  - Saved model file for evaluation.  

---

## Installation  

### Prerequisites  

- Python 3.6+  
- Libraries:  
  - `numpy`, `pandas` for data manipulation.  
  - `scikit-learn`, `PyTorch`, or similar for model development.  
  - `matplotlib`, `seaborn`, or `plotly` for visualization.  
  - Deployment tools: `streamlit`, `flask`, or `fastapi`.  

### Steps  
Install dependencies:
bash
Copy code
pip install -r requirements.txt  
Usage
Data Preprocessing: Run the script to clean and prepare the training dataset:

bash
Copy code
python preprocess_train.py  
Model Training: Train the anomaly detection model:

bash
Copy code
python train_model.py  
Visualization: Generate anomaly plots:

bash
Copy code
python visualize_anomalies.py  
Test Dataset Application: Apply the trained model to test data:

bash
Copy code
python detect_anomalies_test.py  
Model Deployment: Run the deployment script:

bash
Copy code
streamlit run deploy_app.py  
Technologies Used
Programming Language: Python
Libraries:
Data Preprocessing: pandas, numpy
Model Development: scikit-learn, PyTorch
Visualization: matplotlib, seaborn, plotly
Deployment: streamlit, flask, fastapi

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your_username/anomaly-detection-stock-data.git  
   cd anomaly-detection-stock-data  

