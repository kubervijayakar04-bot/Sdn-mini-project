# ~/pox/ext/monitor.py
# Network Utilization Monitor for POX
# Collect byte counters, estimate bandwidth, display utilization, update periodically

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time

log = core.getLogger()

# Store previous stats
prev_stats = {}

# Assume link speed = 100 Mbps for utilization calculation
LINK_SPEED = 100000000  # bits per second


def request_stats():
    for connection in core.openflow.connections:
        connection.send(of.ofp_port_stats_request())
    log.info("Requested port statistics...")


def handle_portstats(event):
    global prev_stats

    dpid = event.connection.dpid
    now = time.time()

    for stat in event.stats:
        port_no = stat.port_no

        # Skip local port
        if port_no > 65534:
            continue

        key = (dpid, port_no)

        rx_bytes = stat.rx_bytes
        tx_bytes = stat.tx_bytes
        total_bytes = rx_bytes + tx_bytes

        if key in prev_stats:
            old_bytes, old_time = prev_stats[key]

            delta_bytes = total_bytes - old_bytes
            delta_time = now - old_time

            if delta_time > 0:
                bandwidth_bps = (delta_bytes * 8) / delta_time
                utilization = (bandwidth_bps / LINK_SPEED) * 100

                print("--------------------------------------------------")
                print("Switch:", dpid, " Port:", port_no)
                print("RX Bytes:", rx_bytes, " TX Bytes:", tx_bytes)
                print("Bandwidth: %.2f Mbps" % (bandwidth_bps / 1000000))
                print("Utilization: %.2f%%" % utilization)

        prev_stats[key] = (total_bytes, now)


def start_monitor():
    Timer(5, request_stats, recurring=True)
    log.info("Network Utilization Monitor Started (every 5 sec)")


def launch():
    core.openflow.addListenerByName("PortStatsReceived", handle_portstats)
    core.openflow.addListenerByName("ConnectionUp",
                                    lambda event: log.info("Switch Connected: %s",
                                                           event.connection.dpid))
    start_monitor()
