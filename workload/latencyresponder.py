#
# @file latencyresponder.py
#
# Project Edge
# Copyright (C) 2016-17  Deutsche Telekom Capital Partners Strategic Advisory LLC
#

import enswr

# Event handler function for simple latency test responder.
def event_handler(session_id, event_type, sqn, data):
    if event_type == enswr.REQUEST:
        return data
    elif event_type == enswr.NOTIFY:
        enswr.session_notify(session_id, sqn, data)

    return


