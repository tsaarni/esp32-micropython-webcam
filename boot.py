
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(dhcp_hostname='esp32cam')

# SSID and password are stored in flash:
# micropython code ports/esp32/modnetwork.c was changed to
# esp_wifi_set_storage(WIFI_STORAGE_FLASH)
wlan.connect()


import webcam
webcam.run()
