from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
import time

log = core.getLogger()

class NetworkMonitor(object):
    def __init__(self, connection):
        self.connection = connection
        self.connection.addListeners(self)
        self.last_stats = {}
        self.last_time = time.time()

        # Request stats every 2 seconds
        core.callDelayed(2, self._request_stats)

    def _request_stats(self):
        self.connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))
        core.callDelayed(2, self._request_stats)

    def _handle_FlowStatsReceived(self, event):
        current_time = time.time()
        time_diff = current_time - self.last_time

        for stat in event.stats:
            if stat.byte_count == 0:
                continue

            key = (stat.match.nw_src, stat.match.nw_dst)

            if key in self.last_stats:
                prev_bytes = self.last_stats[key]
                byte_diff = stat.byte_count - prev_bytes

                bandwidth = byte_diff / time_diff  # Bytes per second

                log.info("Flow %s -> %s | Bandwidth: %.2f Bytes/s",
                         stat.match.nw_src,
                         stat.match.nw_dst,
                         bandwidth)

            self.last_stats[key] = stat.byte_count

        self.last_time = current_time


def launch():
    def start_switch(event):
        log.info("Monitoring switch %s", dpidToStr(event.dpid))
        NetworkMonitor(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
