from scripts.ping_to_hist_xml import convert_pingtxt_to_xml

if __name__ == '__main__':
    convert_pingtxt_to_xml("raw/ping-cloud-cmWave.txt", "ping-cloud-cmWave.xml")
    convert_pingtxt_to_xml("raw/ping-cloud-mmWave.txt", "ping-cloud-mmWave.xml")
    convert_pingtxt_to_xml("raw/ping-MEC-cmWave.txt", "ping-MEC-cmWave.xml")
