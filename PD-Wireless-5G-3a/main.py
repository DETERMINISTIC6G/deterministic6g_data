from scripts.csv_to_hist_xml import convert_pdw5g_csv_to_xml

if __name__ == '__main__':
    convert_pdw5g_csv_to_xml('raw/5G-URLLC-mmW-Uplink_PD-Wireless-5G-3a.csv', 'uplink.xml')
    convert_pdw5g_csv_to_xml('raw/5G-URLLC-mmW-Downlink_PD-Wireless-5G-3a.csv', 'downlink.xml')