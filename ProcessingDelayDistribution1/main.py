from scripts.ping_to_hist_xml import convert_pingtxt_to_xml

if __name__ == '__main__':
    convert_pingtxt_to_xml("raw/mmWave_delay/ping-cloud-cmWave.txt", "ping-cloud-cmWave.xml")
    convert_pingtxt_to_xml("raw/mmWave_delay/ping-cloud-mmWave.txt", "ping-cloud-mmWave.xml")
    convert_pingtxt_to_xml("raw/mmWave_delay/ping-MEC-cmWave.txt", "ping-MEC-cmWave.xml")

    convert_pingtxt_to_xml("raw/ORAN_MEC/ping_results_MEC_ORAN.txt", "ping_results_MEC_ORAN.xml")
    convert_pingtxt_to_xml("raw/ORAN_MEC/ping-cloud-ORAN-upd.txt", "ping-cloud-ORAN-upd.xml")
    convert_pingtxt_to_xml("raw/ORAN_MEC/ping-cloud-ORAN.txt", "ping-cloud-ORAN.xml")
    convert_pingtxt_to_xml("raw/ORAN_MEC/ping-MEC-ORAN-upd.txt", "ping-MEC-ORAN-upd.xml")
    convert_pingtxt_to_xml("raw/ORAN_MEC/ping-MEC-ORAN.txt", "ping-MEC-ORAN.xml")