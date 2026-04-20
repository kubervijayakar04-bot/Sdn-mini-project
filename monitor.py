from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time

log = core.getLogger()
prev = {}

def handle_flowstats(event):
    global prev
    now = time.time()

    for stat in event.stats:
        try:
            src = stat.match.nw_src
            dst = stat.match.nw_dst

            if not src or not dst:
                continue

            key = str(src) + " -> " + str(dst)
            current = stat.byte_count

            if key in prev:
                old_bytes, old_time = prev[key]
                diff = current - old_bytes
                dt = now - old_time

                if dt > 0:
                    bw = diff / dt
                    log.info("Flow %s | Bandwidth: %.2f Bytes/s", key, bw)

            prev[key] = (current, now)

        except:
            pass

def request_stats():
    for c in core.openflow._connections.values():
        c.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))

def launch():
    core.openflow.addListenerByName("FlowStatsReceived", handle_flowstats)
    Timer(2, request_stats, recurring=True)
    log.info("Bandwidth Monitor Started")
