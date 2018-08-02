import random
import time, datetime
import sys

import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult, IoTHubError, DeviceMethodReturnValue

CONNECTION_STRING = '<IotEdgeConectionString>'
PROTOCOL = IoTHubTransportProvider.MQTT

CLIENT = IoTHubClient(CONNECTION_STRING, PROTOCOL)

WAIT_COUNT = 5

SEND_REPORTED_STATE_CONTEXT = 0
METHOD_CONTEXT = 0

SEND_REPORTED_STATE_CALLBACKS = 0
METHOD_CALLBACKS = 0

def send_reported_state_callback(status_code, user_context):
    global SEND_REPORTED_STATE_CALLBACKS

    print ( "Device twins updated." )

def device_method_callback(method_name, payload, user_context):
    global METHOD_CALLBACKS

    if method_name == "custommethod":
        print("Custom Method Running...")
        # some thing here

        print("Custom Method End...")

        # sample code to update reboot edge device time
        current_time = str(datetime.datetime.now())
        reported_state = "{\"rebootTime\":\"" + current_time + "\"}"
        CLIENT.send_reported_state(reported_state, len(reported_state), send_reported_state_callback, SEND_REPORTED_STATE_CONTEXT)

        print ( "Updating device twins: rebootTime" )

    device_method_return_value = DeviceMethodReturnValue()
    device_method_return_value.response = "{ \"Response\": \"Custom Method is running\" }"
    device_method_return_value.status = 200

    return device_method_return_value
def iothub_client_init():
    if CLIENT.protocol == IoTHubTransportProvider.MQTT or client.protocol == IoTHubTransportProvider.MQTT_WS:
        CLIENT.set_device_method_callback(device_method_callback, METHOD_CONTEXT)

def iothub_client_sample_run():
    try:
        iothub_client_init()

        while True:
            print ( "IoTHubClient waiting for commands, press Ctrl-C to exit" )

            status_counter = 0
            while status_counter <= WAIT_COUNT:
                time.sleep(10)
                status_counter += 1

    except IoTHubError as iothub_error:
        print ( "Unexpected error %s from IoTHub" % iothub_error )
        return
    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "Starting the IoT Hub Python sample..." )
    print ( "    Protocol %s" % PROTOCOL )
    print ( "    Connection string=%s" % CONNECTION_STRING )

    iothub_client_sample_run()
