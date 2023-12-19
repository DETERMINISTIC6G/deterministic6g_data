from scripts.csv_to_hist_xml import convert_pdw5g_csv_to_xml

if __name__ == '__main__':
    convert_pdw5g_csv_to_xml('raw/5G-midband-Uplink_PD-Wireless-5G-2a.csv', 'uplink.xml')
    convert_pdw5g_csv_to_xml('raw/5G-midband-Downlink_PD-Wireless-5G-2a.csv', 'downlink.xml')
