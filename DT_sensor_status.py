#!/usr/bin/env python3
from DtAPI import DtAPI
# Dict with API tokens and server address. should look like:
# authparams={'server': 'https://darktrace.example.com', 'private': 'xxxxxxxxxxx', 'public':'yyyyyyyyyyyyy'}
import apitoken
import logging
import json

def dump_to_json(event):
    json_file_path = "status.json"
    logging.info('Generating json to {}.'.format(json_file_path))

    with open(json_file_path, 'a') as json_file:
        events_data = json.dumps(event)
        json_file.write(events_data + '\n')

    logging.info('json generated to {}.'.format(json_file_path))


def main():
    #logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(asctime)s: %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')


    extract_keys_instance = ("id", "time", "type", "version", "label", "hostname", "type", "load", "cpu", "memoryUsed", "networkInterfacesState_eth0", "networkInterfacesState_eth1", "networkInterfacesState_eth2", "networkInterfacesReceived_eth0", "networkInterfacesReceived_eth1", "networkInterfacesReceived_eth2", "networkInterfacesTransmitted_eth0", "networkInterfacesTransmitted_eth1", "networkInterfacesTransmitted_eth2", "bandwidthCurrent", "bandwidthCurrentString", "processedBandwidthCurrent", "processedBandwidthCurrentString", "connectionsPerMinuteCurrent")
    extract_keys = ("id", "time", "type", "version", "label", "hostname", "diskUtilization", "load", "cpu", "memoryUsed", "networkInterfacesState_eth0", "networkInterfacesState_eth1", "networkInterfacesState_eth2", "networkInterfacesReceived_eth0", "networkInterfacesReceived_eth1", "networkInterfacesReceived_eth2", "networkInterfacesTransmitted_eth0", "networkInterfacesTransmitted_eth1", "networkInterfacesTransmitted_eth2", "bandwidthCurrent", "bandwidthCurrentString", "processedBandwidthCurrent", "processedBandwidthCurrentString", "connectionsPerMinuteCurrent")

    try:
        status = api.getStatus(includeProbes=False)
        logging.info(status)
        for instance_name in status['instances']:
            instance = status['instances'][instance_name]
            print("Instance name %s" % instance_name)
            print(instance)
            if 'probes' in instance:
                for probe_name in instance['probes']:
                    probe = instance['probes'][probe_name]
                    try:
                        probe_filtered = {}
                        for extract_key in extract_keys:
                            probe_filtered[extract_key] = probe[extract_key]
                    except Exception as e:
                        continue
                    print("\tProbe name %s" % probe_name)
                    print("\t%s" % probe_filtered)
                    dump_to_json(probe_filtered)

    except Exception as e:
        logging.error(e.__doc__)
        logging.error(e.message)

if __name__ == "__main__":
    main()