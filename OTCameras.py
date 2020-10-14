import glob
import subprocess


class OTCameras:
    def __init__(self):
        self.ot_cameras, self.other_cameras = self._get_video_devices()

    def _list_all_camera_devices(self):
        return glob.glob("/dev/video*")

    def _get_info(self, device):
        return subprocess.check_output(
            ["udevadm", "info", "--query=all", device]).decode()

    def _get_vendor(self, device):
        vendor_prefix = "E: ID_VENDOR="
        for line in self._get_info(device).split("\n"):
            if vendor_prefix in line:
                return line.replace(vendor_prefix, "")
        raise ValueError(f"Unable to detect the vendor for {device}")

    def _get_video_devices(self):
        ot_cameras = []
        other_cameras = []
        OT_CAMERA_VENDOR = "Sonix_Technology_Co.__Ltd."
        for device in self._list_all_camera_devices():
            if self._get_vendor(device) == OT_CAMERA_VENDOR:
                ot_cameras.append(device)
            else:
                other_cameras.append(device)
        return sorted(ot_cameras), sorted(other_cameras)

    def _take_picture(self, device, path):
        subprocess.check_output([
            "ffmpeg", "-y", "-f", "video4linux2", "-s", "640x480", "-i",
            device, "-ss", "0:0:1", "-frames", "1", path
        ]).decode()

    def take_picture_with_builtin_camera(self, path):
        """Take a picture with the robot's built-in camera."""
        if len(self.ot_cameras) == 0:
            raise ValueError("No built-in camera found.")
        self._take_picture(self.ot_cameras[0], path)

    def take_picture_with_external_camera(self, path):
        """Take a picture with an external USB web cam connected to the robot."""
        if len(self.other_cameras) == 0:
            raise ValueError("No external camera found.")
        self._take_picture(self.other_cameras[0], path)
