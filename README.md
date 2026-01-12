# 🚁 Tello Face-Following Drone


An autonomous DJI Tello drone application that detects and tracks a human face in real time and dynamically adjusts its motion to keep the face centered and at a safe distance.

The system integrates **computer vision**, **face geometry**, and a **PD control loop** to achieve smooth, responsive face-following behavior.

---

## 📌 Project Overview

This project demonstrates a **vision-guided UAV control pipeline** where a DJI Tello drone autonomously follows a human face using live video feedback.

### Key Capabilities

* Real-time face detection using **Face Mesh**
* Distance estimation using **facial geometry**
* Closed-loop control using a **PD controller**
* Autonomous **yaw** and **forward/backward** motion
* Manual override for **takeoff and landing**

This project is designed for **learning, experimentation, and prototyping** in UAV autonomy and human–robot interaction.

---

## 🧠 Core Concept

The drone continuously:

1. Detects a human face from its onboard camera
2. Estimates the face position and distance
3. Computes control commands using a feedback controller
4. Adjusts its motion to keep the face centered and within range

This forms a classic **perception → control → actuation** loop, a foundational pattern in robotics.

---

## 🧩 System Architecture

```
Camera Feed
     ↓
Face Mesh Detection (MediaPipe / cvzone)
     ↓
Face Center & Width Extraction
     ↓
Distance Estimation (Pinhole Camera Model)
     ↓
PD Control Algorithm
     ↓
DJI Tello Motion Commands
```

---

## 🧮 Face-Following Algorithm

### 1️⃣ Face Detection & Landmark Extraction

* Uses **Face Mesh detection** to identify facial landmarks
* Selects key points on the **left and right sides of the face**
* Computes **face width in pixels**

---

### 2️⃣ Distance Estimation

Uses a simplified **pinhole camera model**:

```
Distance = (Real_Face_Width × Focal_Length) / Pixel_Face_Width
```

Where:

* **Real face width** ≈ constant
* **Focal length** is empirically calibrated
* **Pixel width** is measured between facial landmarks

This provides a **relative distance estimate**, sufficient for control.

---

### 3️⃣ PD Control for Yaw (Horizontal Tracking)

**Error calculation:**

```
error = face_center_x − image_center_x
```

**Control output:**

```
speed = Kp × error + Kd × (error − previous_error)
```

* **Proportional (P):** reacts to face displacement
* **Derivative (D):** smooths motion and reduces oscillations

Yaw speed is **clipped to safe limits** to prevent aggressive motion.

---

### 4️⃣ Forward / Backward Control

Based on estimated distance:

* Too close → move **backward**
* Too far → move **forward**
* Within range → **hover**

---

### 5️⃣ Safety & Fail-Safe Logic

* If **no face is detected** → stop motion
* Manual override for **takeoff and landing**
* Speed limits enforced at all times

---

## 🛠️ Requirements

### Hardware

* DJI Tello Drone
* PC / Laptop (for development & visualization)

### Software

* Python **3.8+**
* DJI Tello SDK

### Python Libraries

```bash
pip install opencv-python numpy djitellopy cvzone mediapipe
```

---

## ▶️ How to Run

1. Power on the **DJI Tello** drone
2. Connect your system to the **Tello Wi‑Fi network**
3. Clone the repository
4. Run the script:

```bash
python main.py
```

---

## 🎮 Controls

| Key | Action       |
| --- | ------------ |
| t   | Takeoff      |
| q   | Land         |
| ESC | Exit program |

---

## 📚 Applications

* Autonomous UAV tracking systems
* Human–Drone Interaction (HDI)
* Vision-based robotic control
* Robotics and AI education
* Surveillance and monitoring prototypes
* Research in perception-driven autonomy

---

## 🎯 Learning Outcomes

Through this project, you gain hands-on experience with:

* UAV control using real-time vision feedback
* Face geometry–based distance estimation
* PD control systems in robotics
* Closed-loop autonomy design
* Integrating perception with actuation
* Safe command throttling for drones

---

## ⚠️ Limitations

* Performs best in **good lighting conditions**
* **Single-face tracking** only
* No obstacle avoidance
* Indoor / controlled environment recommended

---

## 🚀 Future Improvements

* Upgrade from **PD to full PID control**
* Add **face re-identification**
* Integrate **obstacle avoidance**
* ROS 2–based simulation before flight
* Multi-target tracking
* State estimation using **sensor fusion**

---

## ⚠️ Safety Disclaimer

This project is intended for **educational and experimental purposes only**.

Always operate UAVs in controlled environments and comply with **local drone regulations**.

The author is **not responsible** for misuse or unsafe operation.
