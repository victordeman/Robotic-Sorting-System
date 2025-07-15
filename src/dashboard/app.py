# Streamlit dashboard for Robotic Sorting System
# Überwachungsschnittstelle für das Robotersortiersystem
import os
import sys
import streamlit as st
import sqlite3
import paho.mqtt.client as mqtt
import json
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.vision.object_detection import detect_object

# Database connection
def get_db_connection():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../database/sorting_log.db'))
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Log to database
def log_to_db(object_type):
    color_map = {1: "Red", 2: "Blue", 0: "Unknown"}
    object_type_str = color_map.get(object_type, "Unknown") if isinstance(object_type, int) else object_type
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO SortingLog (timestamp, object_type, status) VALUES (datetime('now'), ?, ?)", 
                      (object_type_str, "Detected" if object_type_str != "Fault" else "Fault"))
        conn.commit()
        conn.close()
    except Exception as e:
        st.error(f"Database error: {e}")

# MQTT setup
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        st.session_state.mqtt_status = "Connected"
    else:
        st.session_state.mqtt_status = "Disconnected"

def on_message(client, userdata, msg):
    st.session_state.mqtt_message = msg.payload.decode()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("sorting/status")
client.loop_start()

# Streamlit UI
st.title("Robotic Sorting System Dashboard")
st.write("Real-time monitoring for industrial automation (PLC, robotics, vision).")

# MQTT Connection
st.header("MQTT Connection")
if "mqtt_status" not in st.session_state:
    st.session_state.mqtt_status = "Disconnected"
st.write(f"Status: {st.session_state.mqtt_status}")

# System Status
st.header("System Status")
if "system_status" not in st.session_state:
    st.session_state.system_status = "Idle"
st.write(f"Status: {st.session_state.system_status}")

# Current Object
if "current_object" not in st.session_state:
    st.session_state.current_object = "None"
st.write(f"Current Object: {st.session_state.current_object}")

# Vision System
st.header("Vision System")
image_path = st.text_input("Enter image path", "src/vision/sample_images/red_block.jpg")
if st.button("Detect Object"):
    if image_path:
        result = detect_object(image_path)
        color_map = {1: "Red", 2: "Blue", 0: "Unknown"}
        object_type = color_map.get(result, "Unknown")
        st.write(f"Detected: {object_type}")
        st.session_state.current_object = object_type
        st.session_state.system_status = "Running"
        log_to_db(result)
    else:
        st.write("Please enter an image path.")

# Simulate Fault
if st.button("Simulate Fault"):
    st.session_state.system_status = "Fault"
    st.session_state.current_object = "None"
    client.publish("sorting/status", json.dumps({"status": "Fault", "object_type": "None"}))
    log_to_db("Fault")

# Sorting Log
st.header("Sorting Log")
try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SortingLog ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    conn.close()
    if logs:
        st.table(logs)
    else:
        st.write("No logs available.")
except Exception as e:
    st.error(f"Database error: {e}")

st.write("Made with Streamlit")
