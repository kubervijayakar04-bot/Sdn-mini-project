# Network Utilization Monitor using SDN (POX + Mininet)

---

## 📌 Problem Statement

To monitor network bandwidth utilization using Software Defined Networking (SDN) by collecting flow statistics from switches and calculating real-time bandwidth usage.

---

## ⚙️ Tools Used

* Mininet
* POX Controller
* OpenFlow Protocol
* Ubuntu (Linux VM)

---

## 🧠 Approach

* Created a virtual network topology using Mininet
* Used POX controller to interact with OpenFlow switches
* Collected flow statistics (byte counters) from switches
* Calculated bandwidth using byte differences over time
* Displayed real-time network utilization

---

## ⚙️ Controller Logic

The controller periodically requests flow statistics from the switch.

Bandwidth is calculated using:

Bandwidth = (Current Byte Count − Previous Byte Count) / Time Interval

* Each flow is identified using source and destination IP
* The controller computes bandwidth for each flow
* Results are printed in real-time

---

## ▶️ Steps to Run

### 1. Start POX Controller

```
cd ~/pox
./pox.py forwarding.l2_learning misc.monitor
```

---

### 2. Start Mininet

(Open a new terminal)

```
sudo mn --controller=remote --topo single,3
```

---

### 3. Test Connectivity

```
pingall
```

Expected:

* 0% packet loss

---

### 4. Generate Traffic

```
h1 ping h2
```

OR

```
iperf
```

---

## 📊 Output

* Displays bandwidth for each flow in Bytes/sec
* Example output:

```
Flow 10.0.0.1 -> 10.0.0.2 | Bandwidth: 114.96 Bytes/s
```

* Bandwidth updates periodically based on traffic

---

## 🔁 Test Scenarios

### ✅ Scenario 1: Normal Traffic

* Traffic is generated between hosts using ping/iperf
* Controller displays continuous bandwidth usage

---

### ❌ Scenario 2: Reduced/No Traffic

* When traffic is stopped, bandwidth values decrease
* Demonstrates real-time monitoring capability

---

## 📸 Screenshots


### 1. Controller Code

<img width="1402" height="746" alt="Screenshot 2026-04-20 at 10 28 13 PM" src="https://github.com/user-attachments/assets/bf0c5801-999d-45a8-a9a7-550d522d92aa" />


### 2. Controller Running

<img width="906" height="401" alt="Screenshot 2026-04-20 at 10 29 45 PM" src="https://github.com/user-attachments/assets/b7e5ce9b-5279-445b-af1a-48288e601f80" />

### 3. Mininet Connected to Controller

<img width="761" height="345" alt="Screenshot 2026-04-20 at 10 30 57 PM" src="https://github.com/user-attachments/assets/1df727c4-f287-4508-bacf-b52046b571be" />


### 4. Traffic Generation

<img width="548" height="110" alt="Screenshot 2026-04-20 at 10 31 40 PM" src="https://github.com/user-attachments/assets/c6dfcc8a-c6b2-4cc4-811a-7d6bfea4b062" />


### 5. Bandwidth Output (Main Result)

<img width="756" height="397" alt="Screenshot 2026-04-20 at 10 34 28 PM" src="https://github.com/user-attachments/assets/59b6c3df-3f7c-42fb-910e-a3067d69108b" />



### 16. Reduced Traffic Scenario

<img width="746" height="159" alt="Screenshot 2026-04-20 at 10 36 37 PM" src="https://github.com/user-attachments/assets/efabd137-c185-43c4-b827-f2e03a98d617" />


---

## 📈 Future Scope

* Visualize bandwidth using graphs
* Implement traffic filtering or firewall rules
* Extend to larger and complex network topologies
* Integrate with real-time dashboards

---

## ✅ Conclusion

This project demonstrates how SDN enables centralized control and monitoring of networks.
The POX controller dynamically collects flow statistics and calculates bandwidth utilization in real-time, allowing efficient observation and analysis of network behavior.

----

## 📎 References

* https://mininet.org/
* https://github.com/noxrepo/pox
* https://mininet.org/walkthrough/
