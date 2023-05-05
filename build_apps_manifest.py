import os
import json

apps_dir = "apps"

manifest = []

for app_name in os.listdir(apps_dir):
    app_path = os.path.join(apps_dir, app_name)
    if os.path.isdir(app_path):
        app_name = app_path.split("/")[-1].replace("_", " ").capitalize()
        app_files = os.listdir(app_path)
        python_files = [file for file in app_files if file.endswith("py")]

        if python_files:
            app_file = os.path.join(app_path, python_files[0])
            requirements_file = os.path.join(app_path, "requirements.txt")
            if os.path.exists(requirements_file):
                with open(requirements_file, "r") as f:
                    requirements = [line.strip() for line in f.readlines() if line.strip()]
            else:
                requirements = []
            manifest.append(
                {"app": app_file, "requirements": requirements, "name": app_name}
            )

with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
