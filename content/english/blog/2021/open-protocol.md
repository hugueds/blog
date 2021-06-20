---
title: "Open Protocol"
date: 2021-06-20T01:00:25-03:00
draft: true
image: "images/portfolio/item1.jpg"
tags: []
description: "This is meta description."
---

# Open Protocol

 -> Talk about its history
 -> Talk about what manufacturers have in common with this protocol
 -> Point the URL of the latest version available
 -> Explain about the most important MIDs
 -> Create a block of code implementing some basic MIDs
 -> Putting Everything together
 -> Check if signature is present on the post
 
``` python

import socket
from events import Event

class OpenProtocol:

	client = None
	__events__ = ('on_this', 'on_that')
	
	def __init__(self, ip, port=4545):
		self.ip = ip
		self.port = port
		self.on_tool_update += self.tool_updated

	def connect(self):
		...

	def disconnect(self):
		...

	def keep_alive(self):
		...

	def job_subscribe(self):
		...

	def on_tool_update(self):
		...


if __name__ == '__main__':
	tool = OpenProtocol('192.168.0.100', 4545)
	tool.connect()
	tool.job_subscribe()
		


```




