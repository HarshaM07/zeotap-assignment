# Projects Overview

This repository contains two projects: a **Weather Monitoring System** and a **Rule Engine with Abstract Syntax Tree (AST)**.

---

## 1. Weather Monitoring System

### Objective
The weather monitoring system fetches real-time weather data for specified cities using the OpenWeatherMap API. It monitors temperature conditions and sends email alerts if the temperature exceeds a specified threshold. It also summarizes and visualizes daily weather data.

### Features
- Fetches weather data for multiple cities.
- Sends email alerts when the temperature exceeds a defined threshold.
- Summarizes daily weather data, including average, maximum, and minimum temperatures.
- Visualizes daily average temperatures using Matplotlib.

### Requirements
- Python 3.x
- Required Python packages:
  - `requests`
  - `matplotlib`
  - `pandas`

### Installation
1. **Clone the repository:**
   ```bash
   git clone 
   cd weather-monitoring

### 2. Rule Engine with AST
### Objective
Develop a 3-tier rule engine application (Simple UI, API, Backend, Data) to determine user eligibility based on attributes like age, department, income, spend, etc. The system uses Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

### Features
Create and store rules using an AST representation.
Combine multiple rules into a single AST.
Evaluate user attributes against the rules.
Modify existing rules.
Error handling for invalid inputs and rule strings.
Data Structure
Node Class
### A class to represent the AST nodes.

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value
### API Endpoints
### Flask Endpoints
POST /create_rule: Creates a rule and stores its AST.
POST /combine_rules: Combines multiple rules into a single AST.
POST /evaluate_rule: Evaluates the AST against user attributes.
POST /modify_rule: Modifies an existing rule.
Installation

### Clone the repository:
git clone 
cd rule-engine
Install required packages:


pip install Flask
Usage
### To run the Rule Engine, execute the following command:
python app.py
