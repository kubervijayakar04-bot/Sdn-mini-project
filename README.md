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

```text
Network-Utilization-Monitor/
│── pox/
│── ext/
│   └── monitor.py
│── README.md
