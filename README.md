# TurtleBot 4 SLAM & Nav2 Project

Dự án mô phỏng robot TurtleBot 4: Quét bản đồ (SLAM Toolbox), định vị (AMCL) và dẫn đường tự động tránh vật cản (Nav2).

---

## 1. Cài đặt (Installation)

### Cài đặt các gói phụ thuộc:
```bash
sudo apt update
sudo apt install -y ros-humble-turtlebot4-simulator \
                    ros-humble-turtlebot4-desktop \
                    ros-humble-turtlebot4-navigation \
                    ros-humble-teleop-twist-keyboard
```

### Biên dịch Package:
```bash
cd ~/ros2_ws
colcon build --packages-select tb4_nav2_assignment
source install/setup.bash
```

---

## 2. Hướng dẫn chạy (Usage)

### Bước 1: Quét và lưu bản đồ (SLAM)

1. **Khởi chạy mô phỏng và SLAM Toolbox:**
```bash
ros2 launch tb4_nav2_assignment tb4_slam.launch.py
```

2. **Mở terminal mới để lái robot khảo sát (Lưu ý: Undock trước khi chạy):**
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

3. **Lưu bản đồ sau khi quét xong:**
```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/src/tb4_nav2_assignment/maps/map
```

---

### Bước 2: Định vị và Dẫn đường tự động (Nav2)

1. **Khởi chạy hệ thống điều hướng với bản đồ đã lưu:**
```bash
ros2 launch tb4_nav2_assignment tb4_nav2.launch.py
```

2. **Khởi tạo vị trí ban đầu (2D Pose Estimate):**
   - **Thêm công cụ nếu thanh toolbar chưa có:** Nhìn lên thanh công cụ trên cùng của RViz2, bấm vào dấu **`+`** (Add a new tool) $\rightarrow$ Chọn **`2D Pose Estimate`** (hoặc `SetInitialPose`) $\rightarrow$ Bấm **OK**.
   - **Đặt vị trí:** 
     1. Click chọn công cụ **`2D Pose Estimate`**.
     2. Click chuột trái vào vị trí của robot trên bản đồ, kéo mũi tên theo hướng mặt robot đang nhìn rồi thả tay ra.
     3. AMCL sẽ nhận tọa độ và các viền Costmap sẽ hiện ra quanh tường.

3. **Ra lệnh tự hành (Navigation):**
   - Undock
   - Chọn công cụ **`2D Goal Pose`** 
   - Click và kéo mũi tên ở điểm đích bất kỳ. Robot sẽ tự lập đường dẫn và di chuyển né vật cản để đến đích.
