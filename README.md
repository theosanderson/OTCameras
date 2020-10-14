# OTCameras
Helper class for OT2 cameras

## Introduction

It can be useful to plug an external webcam into your OT2, but this makes it hard to know which camera is which. This is a helper class that helps with these sorts of issues.

Usage:

```{py}
import OTCameras

cameras = OTCameras.Cameras()
cameras.take_picture_with_builtin_camera("/data/builtin.jpg")
cameras.take_picture_with_external_camera("/data/external.jpg")

```
