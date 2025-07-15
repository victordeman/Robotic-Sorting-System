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
1. Clone the repository: `git clone https://github.com/victordeman/Robotic-Sorting-System.git`
2. Install dependencies: `pip install -r src/dashboard/requirements.txt`
3. Run Streamlit dashboard: `streamlit run src/dashboard/app.py`

## Directory Structure
- `src/plc/`: TIA Portal PLC code.
- `src/vision/`: Python-based vision system.
- `src/dashboard/`: Streamlit dashboard and network code.
- `src/database/`: SQL database files.
- `robodk/`: RoboDK simulation files.
- `docs/`: Documentation (specs, manual, diagrams).
- `demo/`: Demo video and slides.

## License
MIT License
