#!/bin/bash

# Script to set up the Robotic-Sorting-System repository structure
REPO_DIR="Robotic-Sorting-System"

echo "Creating repository structure in $REPO_DIR..."

# Create main directory if it doesn't exist
if [ -d "$REPO_DIR" ]; then
    echo "Directory $REPO_DIR already exists. Overwriting files..."
else
    mkdir -p "$REPO_DIR"
fi
cd "$REPO_DIR" || { echo "Failed to change to $REPO_DIR"; exit 1; }

# Create directory structure
mkdir -p src/plc src/vision/sample_images src/dashboard src/database robodk docs demo scripts

# Create placeholder files in src/plc
touch src/plc/sorting_system.scl
echo "FUNCTION_BLOCK \"SortingLogic\"\nEND_FUNCTION_BLOCK" > src/plc/sorting_system.scl
touch src/plc/safety_logic.scl
echo "FUNCTION_BLOCK \"SafetyLogic\"\nEND_FUNCTION_BLOCK" > src/plc/safety_logic.scl
touch src/plc/diagnostics.scl
echo "FUNCTION_BLOCK \"Diagnostics\"\nEND_FUNCTION_BLOCK" > src/plc/diagnostics.scl

# Create placeholder files in src/vision
touch src/vision/object_detection.py
echo "# Python script for object detection using OpenCV\nprint('Object detection placeholder')" > src/vision/object_detection.py
touch src/vision/sample_images/red_block.jpg
touch src/vision/sample_images/blue_block.jpg

# Create placeholder files in src/dashboard
touch src/dashboard/app.py
echo "# Streamlit dashboard for Robotic Sorting System\nimport streamlit as st\nst.write('Dashboard placeholder')" > src/dashboard/app.py
touch src/dashboard/network.py
echo "# Network communication (MQTT/OPC UA)\nprint('Network placeholder')" > src/dashboard/network.py
touch src/dashboard/requirements.txt
echo "streamlit==1.28.0\nopencv-python==4.8.1\npaho-mqtt==1.6.1" > src/dashboard/requirements.txt

# Create placeholder files in src/database
touch src/database/sorting_log.sql
echo "CREATE TABLE SortingLog (id INTEGER PRIMARY KEY AUTOINCREMENT, object_type TEXT, timestamp DATETIME);" > src/database/sorting_log.sql
touch src/database/sample_data.sql
echo "INSERT INTO SortingLog (object_type, timestamp) VALUES ('Red', CURRENT_TIMESTAMP);" > src/database/sample_data.sql

# Create placeholder files in robodk
touch robodk/sorting_station.rdk
touch robodk/robot_config.py
echo "# Python API for RoboDK control\nprint('RoboDK configuration placeholder')" > robodk/robot_config.py

# Create placeholder files in docs
touch docs/functional_spec.md
echo "# Functional Specification\nPlaceholder for system specs" > docs/functional_spec.md
touch docs/requirements.md
echo "# Requirements\nPlaceholder for system requirements" > docs/requirements.md
touch docs/architecture_diagram.png
touch docs/user_manual.md
echo "# User Manual\nPlaceholder for user guide" > docs/user_manual.md

# Create placeholder files in demo
touch demo/demo_video.mp4
touch demo/demo_slides.pdf

# Move setup script to scripts/ (if running from outside REPO_DIR)
if [ ! -f scripts/setup_repo.sh ]; then
    mv ../setup_repo.sh scripts/ || echo "Warning: Could not move setup_repo.sh to scripts/"
fi

# Create README.md
touch README.md
cat <<EOL > README.md
# Robotic Sorting System

A simulated robotic sorting system using Siemens TIA Portal, RoboDK, Python, SQL, and Streamlit for industrial automation. Demonstrates skills in PLC programming, robotics, vision systems, networking, and optionally AI.

## Overview
Simulates a robotic sorting system for a manufacturing environment, sorting objects by type (e.g., color) using:
- **Siemens TIA Portal** for PLC control and safety logic.
- **RoboDK** for Kuka/Fanuc robotic arm simulation.
- **OpenCV** (Python) for virtual vision-based object detection.
- **Streamlit** dashboard with MQTT for networked monitoring.
- **SQLite** for logging sorting operations.

## Setup Instructions
1. Clone the repository: \`git clone https://github.com/victordeman/Robotic-Sorting-System.git\`
2. Install dependencies: \`pip install -r src/dashboard/requirements.txt\`
3. Run Streamlit dashboard: \`streamlit run src/dashboard/app.py\`

## Directory Structure
- \`src/plc/\`: TIA Portal PLC code.
- \`src/vision/\`: Python-based vision system.
- \`src/dashboard/\`: Streamlit dashboard and network code.
- \`src/database/\`: SQL database files.
- \`robodk/\`: RoboDK simulation files.
- \`docs/\`: Documentation (specs, manual, diagrams).
- \`demo/\`: Demo video and slides.

## License
MIT License
EOL

# Create .gitignore
touch .gitignore
cat <<EOL > .gitignore
*.pyc
__pycache__/
*.exe
*.bin
venv/
*.db
*.log
EOL

# Create LICENSE
touch LICENSE
echo "MIT License\n\nCopyright (c) 2025 Victor Deman\n\nPermission is hereby granted, free of charge, to any person obtaining a copy..." > LICENSE

echo "Repository structure created successfully!"

# Initialize Git repository if not already initialized
if [ ! -d ".git" ]; then
    git init
    git remote add origin https://github.com/victordeman/Robotic-Sorting-System.git
    echo "Git repository initialized. Run 'git add .', 'git commit', and 'git push' to upload."
else
    echo "Git repository already initialized."
fi
