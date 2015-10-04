from lxml import html
import argparse, requests, time

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="write output to IP_log.txt",
                    action="store_true")
args = parser.parse_args()

def get_ip():
    server = 'https://wtfismyip.com'
    print("Fetching IP from: {0}".format(server))
    page = requests.get(server)
    tree = html.fromstring(page.text)
    public_ip = tree.xpath('//div[@id="main"]/center[2]/p[1]/text()')
    public_host = tree.xpath('//div[@id="main"]/center[4]/p[1]/text()')
    public_geo = tree.xpath('//div[@id="main"]/center[6]/p[1]/text()')
    public_isp = tree.xpath('//div[@id="main"]/center[8]/p[1]/text()')

    print("Public IP:             {0}".format(public_ip[0]))
    print("Public Host:           {0}".format(public_host[0]))
    print("Public Location:       {0}".format(public_geo[0]))
    print("Public ISP:            {0}".format(public_isp[0]))

    if args.log:
        log_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        with open('IP_log.txt', 'a') as log_file:
            log_file.write("---\n{0}\nPublic IP: {1}\nPublic Host: {2}\nPublic Location: {3}\nPublic ISP: {4}\n"
            .format(log_time, public_ip, public_host, public_geo, public_isp))

if __name__ == '__main__':
    get_ip()
