#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

import precompile as pcp

if __name__ == "__main__":
    
    segments = pcp.SEGMENTS()
    for segment_name in pcp.SEGMENTS_NAMES:
        segments.addSegment(pcp.SEGMENT(segment_name))
    for x in range(10):
        for segment_name in pcp.SEGMENTS_NAMES:
            for datatype in pcp.DATATYPES:
                segments.getSegment(segment_name).addData(datatype)
                pcp.write(segments.getSegment(segment_name))
    