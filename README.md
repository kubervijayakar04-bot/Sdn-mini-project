# Network Utilization Monitor

## Project Overview
The Network Utilization Monitor is a Software Defined Networking (SDN) based project developed using **POX Controller** and **Mininet**. The main objective of this project is to monitor bandwidth utilization across the network by collecting byte counters from switches and displaying network usage periodically.

This project demonstrates how SDN controllers can be used for real-time traffic monitoring and network management.

---

## Objectives
- Measure and display bandwidth utilization across the network.
- Collect RX and TX byte counters from switch ports.
- Estimate bandwidth usage.
- Display utilization statistics.
- Update network statistics periodically.

---

## Tools & Technologies Used
- **Operating System:** Ubuntu Linux
- **Programming Language:** Python
- **SDN Controller:** POX
- **Network Emulator:** Mininet

---

## Project Structure

```bash
Network-Utilization-Monitor/
│── pox/
│── ext/
│   └── monitor.py
│── README.md
```

 ## RESULTS /OUTPUT

 1. POX Controller Start
    <img width="1016" height="514" alt="Screenshot 2026-04-20 at 12 06 32 AM" src="https://github.com/user-attachments/assets/db7e4b5e-fc63-4893-8389-bf6ce7aadc2d" />

 2. Mininet Topology
<img width="1168" height="287" alt="Screenshot 2026-04-20 at 12 08 05 AM" src="https://github.com/user-attachments/assets/ce652ed6-b079-44b0-baa5-5cbf426b6300" />

 3. pingall Connectivity Test
<img width="570" height="115" alt="Screenshot 2026-04-20 at 12 08 41 AM" src="https://github.com/user-attachments/assets/940cfce9-a498-404d-83fd-49d2d17d9d66" />

 4. Traffic Generation (h1 ping h2)
<img width="1092" height="591" alt="Screenshot 2026-04-20 at 12 08 49 AM" src="https://github.com/user-attachments/assets/8204c071-ecf2-43fc-b9e0-11b2b1d42485" />

 5. Network Utilization Monitor Started Successfully
    <img width="776" height="183" alt="Screenshot 2026-04-20 at 12 18 19 AM" src="https://github.com/user-attachments/assets/b29b2215-2f73-4e64-b981-bd18d7266473" />
