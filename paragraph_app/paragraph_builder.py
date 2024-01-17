from flask import Flask, render_template
from random import choice

app = Flask(__name__)

statement_types = ["question", "exclamation", "statement", "implication"]
basic_conjunctions = ["because", "but", "so"]
exp = [
    "analyse",
    "comment",
    "compare",
    "contrast",
    "criticize",
    "define",
    "describe",
    "discuss",
    "enumerate",
    "evaluate",
    "explain",
    "illustrate",
    "interpret",
    "justify",
    "ooutline",
    "relate",
    "state",
    "summarize",
    "trace",
]
q_terms = ["Who?", "What?", "When?", "Where?", "Why?", "How?"]
subordinating_conjugations = [
    "before",
    "after",
    "if",
    "when",
    "even though",
    "although",
    "since",
    "while",
    "unless",
    "whenever",
]

to_do = ["summarize", "make topic sentence", "make SPO", "add appositive"]

phases = ["plan", "draft", "revise", "edit"]

transitions = [
"Time—sequence of events or steps in a process",
"Conclusion—summary, cause and effect, point of view, solution",
"Illustration—give examples, support details, explain or elaborate on a statement",
"Change of direction—contrasting thoughts",
"Emphasis—prove a point or statement; reaffirm something previously stated",
]

@app.route("/")
@app.route("/new")
def home():
    return render_template(
        'index.html',
        statement_type = choice(statement_types),
        basic_conjunction = choice(basic_conjunctions),
        expository_term = choice(exp),
        question_term = choice(q_terms),
        subordinating_conjunction = choice(subordinating_conjugations),
        to_do = choice(to_do),
        phase = choice(phases),
        transition = choice(transitions),
    )

if __name__ == "__main__":
    app.run(debug=True)
