from scripts.csv_to_hist_xml import convert_pdw5g_csv_to_xml

if __name__ == '__main__':
    convert_pdw5g_csv_to_xml('raw/5G-mmW-UL-histData.csv', 'uplink.xml')
    convert_pdw5g_csv_to_xml('raw/5G-mmW-DL-histData.csv', 'downlink.xml')