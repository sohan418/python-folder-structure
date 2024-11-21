import os
import zipfile

# Define the folder structure
project_folder = 'project_name'
src_folder = os.path.join(project_folder, 'src')
app_folder = os.path.join(src_folder, 'app')
routes_folder = os.path.join(app_folder, 'routes')
services_folder = os.path.join(app_folder, 'services')
utils_folder = os.path.join(app_folder, 'utils')
models_folder = os.path.join(app_folder, 'models')

# Creating directories
os.makedirs(routes_folder, exist_ok=True)
os.makedirs(services_folder, exist_ok=True)
os.makedirs(utils_folder, exist_ok=True)
os.makedirs(models_folder, exist_ok=True)

# Sample content for files
file_structure = {
    'README.md': "# Project Documentation\nThis project is a sample Flask API structure.",
    'requirements.txt': "flask\npymongo\n",
    'Dockerfile': "# Dockerfile for Flask app\nFROM python:3.8-slim\nRUN pip install -r requirements.txt\n",
    '.env': "FLASK_APP=src/app/main.py\nFLASK_ENV=development\n",
    'src/app/__init__.py': "# Initialize app and DB\nfrom flask import Flask\napp = Flask(__name__)\n",
    'src/app/config.py': "# Configuration settings\nDEBUG = True\n",
    'src/app/main.py': "from flask import Flask\nfrom src.app.routes.vendor_routes import vendor_routes\n\n"
                        "def create_app():\n    app = Flask(__name__)\n    vendor_routes(app)\n    return app\n\n"
                        "if __name__ == '__main__':\n    app = create_app()\n    app.run(debug=True)\n",
    'src/app/routes/vendor_routes.py': "from flask import request\nfrom src.app.services.vendor_service import insert_vendor_service\n\n"
                                       "def vendor_routes(app):\n    @app.route('/api/vendor/insert-single-vendor', methods=['POST'])\n"
                                       "    def insert_vendor():\n        try:\n            response = insert_vendor_service(request.form)\n"
                                       "            return response\n        except Exception as e:\n            return str(e)\n",
    'src/app/services/vendor_service.py': "def insert_vendor_service(form_data):\n    # Logic to insert vendor data\n    return {'status': 'success'}\n",
    'src/app/utils/id_generator.py': "import uuid\n\ndef generate_unique_id():\n    return str(uuid.uuid4())\n",
    'src/app/models/vendor_model.py': "# Vendor model (MongoDB)\nclass VendorModel:\n    pass\n"
}

# Create the files in the specified directories
for relative_path, content in file_structure.items():
    file_path = os.path.join(project_folder, relative_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(content)

# Create the zip file
zip_filename = 'wms-backend.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_folder):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, project_folder))

print(f"Project structure created and zipped as '{zip_filename}'")
