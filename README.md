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

