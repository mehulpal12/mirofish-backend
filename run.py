"""
MiroFish Backend Startup Entry Point
"""
import os
import sys
from dotenv import load_dotenv
from flask import jsonify # Import jsonify to send JSON responses

load_dotenv()

# Pre-setting the key to pass validation
os.environ['ZEP_API_KEY'] = 'z_1dWlkIjoiMmM5ODQ0MzktYzM4OS00ZDhkLTk2MzItMDFkN2RiNzZkMTY0In0.jLddHhiLuIQ6w7UtLnepJvz0ECqx1G-uRFd2gn-igV7YuwlycNMYCS796U_zQYhdMHLB-P106gSbf6VQ6CNITA'

# UTF-8 Fixes for Windows
if sys.platform == 'win32':
    os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.config import Config

def main():
    """Main Function"""
    errors = Config.validate()
    if errors:
        print("Configuration Error:")
        for err in errors:
            print(f"   - {err}")
        sys.exit(1)
    
    # 1. Initialize the app
    app = create_app()

    # 2. ADD SAMPLE ROUTE HERE
    # Equivalent to app.get('/test', (req, res) => res.json({...}))
    @app.route('/test', methods=['GET'])
    def test_route():
        return jsonify({
            "status": "success",
            "message": "MiroFish Backend is running!",
            "port": os.environ.get('FLASK_PORT', 5001)
        })

    # 3. Retrieve configurations and run
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5001))
    debug = Config.DEBUG
    
    print(f"\n🚀 Server starting at http://localhost:{port}/test")
    app.run(host=host, port=port, debug=debug, threaded=True)

if __name__ == '__main__':
    main()