from scripts.csv_to_hist_xml import convert_csv_to_xml

if __name__ == '__main__':
    convert_csv_to_xml('/home/haugls/Downloads/cloud_application_latency_histogram_fifo.csv', "fifo.xml")
    convert_csv_to_xml('/home/haugls/Downloads/cloud_application_latency_histogram_deadline.csv', "deadline.xml")
