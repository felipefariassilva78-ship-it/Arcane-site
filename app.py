from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")

# História
@app.route("/historia")
def historia():
    return render_template("historia.html")

# Temporadas
@app.route("/temporadas")
def temporadas():
    return render_template("temporadas.html")

# Personagens
@app.route("/personagens/jinx")
def jinx():
    return render_template("personagens/jinx.html")

@app.route("/personagens/vi")
def vi():
    return render_template("personagens/vi.html")

@app.route("/personagens/ekko")
def ekko():
    return render_template("personagens/ekko.html")

@app.route("/personagens/caitlyn")
def caitlyn():
    return render_template("personagens/caitlyn.html")

@app.route("/personagens/heimerdinger")
def heimerdinger():
    return render_template("personagens/heimerdinger.html")

@app.route("/personagens/viktor")
def viktor():
    return render_template("personagens/viktor.html")

@app.route("/personagens/jayce")
def jayce():
    return render_template("personagens/jayce.html")

if __name__ == "__main__":
    app.run(debug=True)
