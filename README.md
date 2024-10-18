# Rule Engine with AST

## Objective
Develop a 3-tier rule engine application (Simple UI, API, Backend, Data) to determine user eligibility based on attributes like age, department, income, spend, etc. The system uses Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features
1. Create and store rules using an AST representation.
2. Combine multiple rules into a single AST.
3. Evaluate user attributes against the rules.
4. Modify existing rules.
5. Error handling for invalid inputs and rule strings.

## Data Structure
### Node Class
A class to represent the AST nodes.
```python
class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value
## API Endpoints
** Flask Endpoints**
POST /create_rule: Creates a rule and stores its AST.

POST /combine_rules: Combines multiple rules into a single AST.

POST /evaluate_rule: Evaluates the AST against user attributes.

POST /modify_rule: Modifies an existing rule.

2.# Weather Monitoring System

This is a weather monitoring system that fetches real-time weather data for specified cities using the OpenWeatherMap API. The system monitors temperature conditions and sends email alerts if the temperature exceeds a specified threshold. It also summarizes and visualizes daily weather data.

## Features

- Fetches weather data for multiple cities.
- Sends email alerts when the temperature exceeds a defined threshold.
- Summarizes daily weather data, including average, maximum, and minimum temperatures.
- Visualizes daily average temperatures using Matplotlib.

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `matplotlib`
  - `pandas`

## Installation

1. **Clone the repository:**
   ```bash
   git clone 
   cd weather-monitoring
