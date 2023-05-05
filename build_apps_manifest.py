import os
import json

apps_dir = "apps"

manifest = []

for app_name in os.listdir(apps_dir):
    app_path = os.path.join(apps_dir, app_name)
    if os.path.isdir(app_path):
        app_file = os.path.join(app_path, "app.py")
        if os.path.exists(app_file):
            requirements_file = os.path.join(app_path, "requirements.txt")
            if os.path.exists(requirements_file):
                with open(requirements_file, "r") as f:
                    requirements = [line.strip() for line in f.readlines()]
            else:
                requirements = []
            manifest.append({"app": f"github.com/SocialFinanceDigitalLabs/path/blob/main/apps/{app_name}/app.py", "requirements": requirements})

with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)