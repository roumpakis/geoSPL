# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:34:58 2023

@author: roub
"""

from copernicusNotify import copernicusNotify as CN
cn = CN()

events,feed = cn.get_all_notifications()
null_polygon_count = 0
non_null_polygon_count = 0

for event in events:
    if "polygon" in event:
        if event["polygon"] is None:
            null_polygon_count += 1
        else:
            non_null_polygon_count += 1

print("Count of events with 'polygon' as None:", null_polygon_count)
print("Count of events with non-None 'polygon':", non_null_polygon_count

)



for event in events:
    if "polygon" in event:
        if event["polygon"] is None:
            null_polygon_count += 1
        else:
            non_null_polygon_count += 1

print("Count of events with 'polygon' as None:", null_polygon_count)
print("Count of events with non-None 'polygon':", non_null_polygon_count


cn.generate_feed_map(events)