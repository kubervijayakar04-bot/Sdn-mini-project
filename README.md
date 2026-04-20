# File: monitor.py
# Place this file inside: pox/pox/misc/monitor.py

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time

log = core.getLogger()

# Store previous flow stats
previous_stats = {}


class NetworkMonitor(object):
    def __init__(self, connection):
        self.connection = connection
        self.connection.addListeners(self)

        # Request stats every 2 seconds
        Timer(2, self.request_stats, recurring=True)

    def request_stats(self):
        self.connection.send(
            of.ofp_stats_request(
                body=of.ofp_flow_stats_request()
            )
        )

    def _handle_FlowStatsReceived(self, event):
        global previous_stats

        current_time = time.time()

        for stat in event.stats:
            try:
                if stat.byte_count == 0:
                    continue

                src = stat.match.nw_src
                dst = stat.match.nw_dst

                if src is None or dst is None:
                    continue

                flow_key = str(src) + " -> " + str(dst)

                if flow_key in previous_stats:
                    old_bytes, old_time = previous_stats[flow_key]

                    byte_diff = stat.byte_count - old_bytes
                    time_diff = current_time - old_time

                    if time_diff > 0:
                        bandwidth = byte_diff / time_diff

                        log.info(
                            "Flow %s | Bandwidth: %.2f Bytes/s",
                            flow_key,
                            bandwidth
                        )

                previous_stats[flow_key] = (
                    stat.byte_count,
                    current_time
                )

            except:
                pass


def launch():
    def start_switch(event):
        log.info("Switch Connected - Monitoring Started")
        NetworkMonitor(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)

    log.info("Bandwidth Monitor Started")        global previous_stats

        current_time = time.time()

        for stat in event.stats:
            try:
                # Ignore empty flows
                if stat.byte_count == 0:
                    continue

                src = stat.match.nw_src
                dst = stat.match.nw_dst

                # Ignore flows without IP match
                if src is None or dst is None:
                    continue

                flow_key = str(src) + " -> " + str(dst)

                if flow_key in previous_stats:
                    old_bytes, old_time = previous_stats[flow_key]

                    byte_diff = stat.byte_count - old_bytes
                    time_diff = current_time - old_time

                    if time_diff > 0:
                        bandwidth = byte_diff / time_diff

                        log.info(
                            "Flow %s | Bandwidth: %.2f Bytes/s",
                            flow_key,
                            bandwidth
                        )

                previous_stats[flow_key] = (
                    stat.byte_count,
                    current_time
                )

            except:
                pass


def launch():
    def start_switch(event):
        log.info("Monitoring Switch Connected")
        NetworkMonitor(event.connection)

    core.openflow.addListenerByName(
        "ConnectionUp",
        start_switch
    )

    log.info("Bandwidth Monitor Started")
