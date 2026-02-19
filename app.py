from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "womensafety2024secretkey"

# In-memory storage (no database needed for demo)
incidents = []
users = {}
emergency_contacts_db = {}

# ─── ROUTES ───────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username', 'Guest')
    contacts = emergency_contacts_db.get(username, [])
    return render_template('dashboard.html', username=username, contacts=contacts)

@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/education')
def education():
    return render_template('education.html')

# ─── API ENDPOINTS ────────────────────────────────────────────────────────────

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name', '').strip()
    if name:
        session['username'] = name
        users[name] = {'name': name, 'joined': datetime.now().strftime('%Y-%m-%d')}
        return jsonify({'success': True, 'username': name})
    return jsonify({'success': False, 'error': 'Name required'})

@app.route('/api/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/api/sos', methods=['POST'])
def sos_alert():
    data = request.get_json()
    alert = {
        'id': len(incidents) + 1,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'lat': data.get('lat'),
        'lng': data.get('lng'),
        'user': session.get('username', 'Anonymous'),
        'type': 'SOS',
        'address': data.get('address', 'Unknown location'),
        'message': data.get('message', 'Emergency SOS triggered')
    }
    incidents.append(alert)
    print(f"🚨 SOS ALERT: {alert}")
    return jsonify({'success': True, 'alert_id': alert['id'], 'message': 'Alert sent to all emergency contacts!'})

@app.route('/api/report-incident', methods=['POST'])
def report_incident():
    data = request.get_json()
    incident = {
        'id': len(incidents) + 1,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'category': data.get('category', 'Other'),
        'description': data.get('description', ''),
        'lat': data.get('lat'),
        'lng': data.get('lng'),
        'address': data.get('address', 'Unknown'),
        'user': session.get('username', 'Anonymous'),
        'type': 'incident'
    }
    incidents.append(incident)
    return jsonify({'success': True, 'id': incident['id']})

@app.route('/api/incidents')
def get_incidents():
    return jsonify(incidents)

@app.route('/api/add-contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    username = session.get('username', 'Guest')
    if username not in emergency_contacts_db:
        emergency_contacts_db[username] = []
    contact = {
        'name': data.get('name'),
        'phone': data.get('phone'),
        'relation': data.get('relation', 'Family')
    }
    emergency_contacts_db[username].append(contact)
    return jsonify({'success': True, 'contact': contact})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()
    
    # Rule-based safety chatbot (no API key needed)
    responses = {
        'follow': "🚨 If someone is following you:\n1. Walk to a crowded public place\n2. Enter a shop or restaurant\n3. Call 100 (Police) or 112\n4. Alert someone nearby\n5. Avoid going home directly",
        'police': "📍 Nearest Police Station: Call 100\nMumbai Police Control Room: 022-100\nWomen Helpline: 1091\nNational Emergency: 112",
        'helpline': "📞 Emergency Helplines:\n• Police: 100\n• Women Helpline: 1091\n• Ambulance: 108\n• National Emergency: 112\n• Childline: 1098\n• Cyber Crime: 1930",
        'safe': "✅ Safety Tips:\n1. Share your location with trusted contacts\n2. Keep your phone charged\n3. Use well-lit routes\n4. Trust your instincts\n5. Know emergency numbers by heart",
        'dark': "💡 Avoid Dark Areas:\n1. Use Google Maps to find busy routes\n2. Call someone while walking\n3. Use the SOS button if uncomfortable\n4. Prefer public transport at night",
        'stalk': "🚨 If you are being stalked:\n1. Don't confront the stalker\n2. Document all incidents\n3. File a complaint at nearest police station\n4. Call Women Helpline: 1091\n5. Inform trusted family/friends",
        'rights': "⚖️ Your Legal Rights:\n1. Right to lodge FIR anytime, anywhere\n2. Right to be examined by female doctor\n3. Protection under IPC 354 (molestation)\n4. Zero FIR can be filed at any police station\n5. Complaint can be filed online at cybercrime.gov.in",
        'number': "📞 Important Numbers:\n• Police: 100\n• Women Helpline: 1091\n• Ambulance: 108\n• Emergency: 112\n• Cyber Crime: 1930",
    }
    
    reply = "🤖 I'm your safety assistant. Ask me about:\n• What to do if someone follows you\n• Helpline numbers\n• Legal rights\n• Safety tips\n• How to stay safe at night"
    
    for keyword, response in responses.items():
        if keyword in user_message:
            reply = response
            break
    
    return jsonify({'reply': reply})

# ─── RUN ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("🚨 Women Safety Platform Starting...")
    print("🌐 Open: http://localhost:5000")
    app.run(debug=True, port=5000)
