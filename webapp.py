from flask import Flask
from utils import load_csv, filter_rows, column_stats

app = Flask(__name__)

@app.route("/")
def home():
    data = load_csv("students.csv")

    filtered = filter_rows(
        data,
        "Department",
        lambda x: x == "Data Science"
    )

    mean, median, count = column_stats(data, "Marks")

    return f"""
    <h1>Basic Python Utilities Project</h1>

    <h2>Column Statistics</h2>
    <p>Mean Marks: {mean}</p>
    <p>Median Marks: {median}</p>
    <p>Numeric Count: {count}</p>

    <h2>Filtered Data - Data Science</h2>
    <pre>{filtered}</pre>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
