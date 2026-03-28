import os
import sys
from dotenv import load_dotenv
from flask import jsonify
from app import create_app
from app.config import Config

load_dotenv()

# --- 1. Global Setup (Must be outside functions) ---
os.environ['ZEP_API_KEY'] = 'z_1dWlkIjoiMmM5ODQ0MzktYzM4OS00ZDhkLTk2MzItMDFkN2RiNzZkMTY0In0...'

if sys.platform == 'win32':
    # Your UTF-8 fixes...
    pass

# --- 2. Create the app instance GLOBALLY ---
# This is what Vercel looks for!
app = create_app()

# --- 3. Add your routes ---
@app.route('/test', methods=['GET'])
def test_route():
    return jsonify({
        "status": "success",
        "message": "MiroFish Backend is running on Vercel!",
        "port": os.environ.get('FLASK_PORT', 5001)
    })

# --- 4. Local Development Only ---
if __name__ == '__main__':
    errors = Config.validate()
    if errors:
        print("Configuration Error:", errors)
        sys.exit(1)
    
    port = int(os.environ.get('FLASK_PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)