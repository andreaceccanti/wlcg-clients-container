import os
import sys
import gfal2
import logging

streamHandler = logging.StreamHandler(sys.stdout)
streamHandler.setFormatter(logging.Formatter(
    "%(asctime)s.%(msecs)03d [%(levelname)s](%(module)s:%(lineno)d) %(message)s", "%d %b %H:%M:%S"))

gfal2_logger = logging.getLogger("gfal2")
gfal2_logger.addHandler(streamHandler)
gfal2_logger.setLevel(logging.DEBUG)
gfal2.set_verbose(gfal2.verbose_level.debug)
gfal2.set_verbose(gfal2.verbose_level.trace)

dst = 'davs://storm.example:8443/wlcg/test-not-found'
ctx = gfal2.creat_context()

ctx.set_opt_boolean("HTTP PLUGIN", "KEEP_ALIVE", True)

cred = gfal2.cred_new("BEARER", os.getenv('BEARER_TOKEN'))
gfal2.cred_set(ctx, dst, cred)

try:
    ctx.stat(dst)
except:
    pass
try:
    ctx.stat(dst)
except:
    pass
