from flask import Flask, request, jsonify
import json
import mysql.connector

app = Flask(__name__)

db_config = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "database": "rule_engine1",
}


class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value


def save_rule_to_db(rule_string, ast):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO rules (rule_string, ast) VALUES (%s, %s)",
        (rule_string, json.dumps(ast, default=lambda o: o.__dict__)),
    )
    conn.commit()
    cursor.close()
    conn.close()


@app.route("/create_rule", methods=["POST"])
def create_rule():
    rule_string = request.json["rule_string"]
    ast = parse_rule(rule_string)
    save_rule_to_db(rule_string, ast)
    return jsonify({"ast": json.dumps(ast, default=lambda o: o.__dict__)})


@app.route("/combine_rules", methods=["POST"])
def combine_rules():
    rules = request.json["rules"]
    combined_ast = combine(rules)
    return jsonify(
        {"combined_ast": json.dumps(combined_ast, default=lambda o: o.__dict__)}
    )


@app.route("/evaluate_rule", methods=["POST"])
def evaluate_rule():
    ast = json.loads(request.json["ast"], object_hook=lambda d: Node(**d))
    data = request.json["data"]
    result = evaluate(ast, data)
    return jsonify({"result": result})


@app.route("/modify_rule", methods=["POST"])
def modify_rule():
    rule_id = request.json["rule_id"]
    new_rule_string = request.json["new_rule_string"]
    new_ast = parse_rule(new_rule_string)
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE rules SET rule_string = %s, ast = %s WHERE id = %s",
        (new_rule_string, json.dumps(new_ast, default=lambda o: o.__dict__), rule_id),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"ast": json.dumps(new_ast, default=lambda o: o.__dict__)})


def parse_rule(rule_string):
    # Simplified example parsing
    return Node(
        "operator",
        "AND",
        Node("operand", value="age > 30"),
        Node("operand", value="salary > 50000"),
    )


def combine(rules):
    # Simplified combination logic
    root = Node("operator", "AND")
    for rule in rules:
        if root.left is None:
            root.left = parse_rule(rule)
        else:
            root.right = parse_rule(rule)
    return root


def evaluate(ast, data):
    if ast.type == "operator":
        if ast.left and ast.right:
            left_result = evaluate(ast.left, data)
            right_result = evaluate(ast.right, data)
            if ast.value == "AND":
                return left_result and right_result
            elif ast.value == "OR":
                return left_result or right_result
    elif ast.type == "operand":
        # Evaluate condition
        condition = ast.value.replace("age", str(data["age"])).replace(
            "salary", str(data["salary"])
        )
        return eval(condition)
    return False


def validate_attributes(data):
    required_attributes = ["age", "department", "salary", "experience"]
    for attr in required_attributes:
        if attr not in data:
            return False
    return True


if __name__ == "__main__":
    app.run(debug=True)
