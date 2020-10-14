# OTCameras
Helper class for using webcams with the OT2.

## Introduction

It can be useful to plug an external webcam into your OT2, but this makes it hard to know which camera is the built-in OT camera and which is the external camera. This is a helper class that helps with these sorts of issues.

Usage:

```py
import OTCameras

cameras = OTCameras.Cameras()
cameras.take_picture_with_builtin_camera("/data/builtin.jpg")
cameras.take_picture_with_external_camera("/data/external.jpg")

```
