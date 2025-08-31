from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# User Login
@app.route('/login/user', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        return render_template('login.html', message="Oops! You're not in the sweet circle yet!🍬")
    return render_template('login.html', message="")

# Admin Login
@app.route('/login/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        return render_template('login.html', message="Only the master confectioner can enter!🍬")
    return render_template('login.html', message="")

# Custom Header
REQUIRED_HEADER = "X-Sweet-Key"
REQUIRED_VALUE = "Marshmallow"

# Check the header
def check_custom_header():
    if request.headers.get(REQUIRED_HEADER) != REQUIRED_VALUE:
        abort(403)  # 403 Forbidden

# Protected Endpoints
@app.route('/worldpay')
def worldpay():
    check_custom_header()
    return "🌍 Welcome to WorldPay page! -  SV9T"

@app.route('/Provas')
def provas():
    check_custom_header()
    return "🔍 You've unlocked Provas! - YzAw"

@app.route('/_legacy')
def legacy():
    check_custom_header()
    return "🕰️ Legacy systems are hidden here! - cDNk"

@app.route('/accueil')
def accueil():
    check_custom_header()
    return "🏠 Accueil unlocked! - X1Ro"

@app.route('/cheesebot')
def cheesebot():
    check_custom_header()
    return "🧀 CheeseBot activated! - M19G"

@app.route('/tikiwiki')
def tikiwiki():
    check_custom_header()
    return "🌴 Welcome to TikiWiki! - bDRn"

# Robots.txt
@app.route('/robots.txt')
def robots():
    return '''
    User-agent: *
    Disallow: /login/
    # There's more sweetness hidden around! 🍬
    '''

# Custom 403 Error Page
@app.errorhandler(403)
def forbidden(e):
    return "🤔 Nothing to see here...", 403

   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)

