import argparse, time, json, urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="write output to IP_log.json",
                    action="store_true")
args = parser.parse_args()

def get_ip():
    server = 'https://wtfismyip.com/json'
    print("Fetching IP from: {0}".format(server))
    with urllib.request.urlopen(server) as response:
        str_response = response.readall().decode('utf-8')
        data = json.loads(str_response)

    print("Public IP:             {0}".format(data["YourFuckingIPAddress"]))
    print("Public Host:           {0}".format(data["YourFuckingLocation"]))
    print("Public Location:       {0}".format(data["YourFuckingHostname"]))
    print("Public ISP:            {0}".format(data["YourFuckingISP"]))

    if args.log:
        log_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        with open('IP_log.json', 'a') as log_file:
            log_data = {log_time: [data]}
            json.dump(log_data, log_file)

if __name__ == '__main__':
    get_ip()
