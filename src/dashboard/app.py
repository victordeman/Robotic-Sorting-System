# Streamlit dashboard for Robotic Sorting System
# Überwachungsschnittstelle für das Robotersortiersystem
import streamlit as st
import sqlite3
import paho.mqtt.client as mqtt
import json
import time
from src.vision.object_detection import detect_object  # Import vision function

# MQTT setup
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "sorting/status"

# Database connection
def get_db_connection():
    conn = sqlite3.connect("src/database/sorting_log.db")
    conn.row_factory = sqlite3.Row
    return conn

# Log to database
def log_to_db(object_type):
    conn = get_db_connection()
    conn.execute("INSERT INTO SortingLog (object_type, timestamp) VALUES (?, CURRENT_TIMESTAMP)", (object_type,))
    conn.commit()
    conn.close()

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    st.session_state["mqtt_status"] = "Connected" if rc == 0 else f"Connection failed: {rc}"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    st.session_state["status"] = data["status"]
    st.session_state["object_type"] = data["object_type"]

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)
client.loop_start()

# Streamlit app
st.title("Robotic Sorting System Dashboard")
st.write("Real-time monitoring for industrial automation (PLC, robotics, vision).")

# Initialize session state
if "status" not in st.session_state:
    st.session_state["status"] = "Idle"
    st.session_state["object_type"] = "None"
    st.session_state["mqtt_status"] = "Disconnected"

# MQTT status
st.subheader("MQTT Connection")
st.write(f"**Status**: {st.session_state['mqtt_status']}")

# System status
st.subheader("System Status")
st.write(f"**Status**: {st.session_state['status']}")
st.write(f"**Current Object**: {st.session_state['object_type']}")

# Vision system integration
st.subheader("Vision System")
image_path = st.text_input("Enter image path", "src/vision/sample_images/red_block.jpg")
if st.button("Detect Object"):
    result = detect_object(image_path)
    object_type = {1: "Red", 2: "Blue", 0: "Unknown"}[result]
    st.write(f"Detected: {object_type}")
    client.publish(TOPIC, json.dumps({"status": "Running", "object_type": object_type}))
    log_to_db(object_type)

# Sorting log
st.subheader("Sorting Log")
try:
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM SortingLog ORDER BY timestamp DESC LIMIT 5")
    logs = cursor.fetchall()
    conn.close()
    st.table([{"ID": row["id"], "Object Type": row["object_type"], "Timestamp": row["timestamp"]} for row in logs])
except sqlite3.Error as e:
    st.error(f"Database error: {e}")

# Simulate fault
if st.button("Simulate Fault"):
    st.session_state["status"] = "Fault Detected"
    client.publish(TOPIC, json.dumps({"status": "Fault", "object_type": "None"}))
    log_to_db("Fault")

# Refresh button
if st.button("Refresh"):
    st.experimental_rerun()

# AI placeholder
st.subheader("AI Classification (Optional)")
st.write("Placeholder for AI-based object classification (e.g., TensorFlow model).")
