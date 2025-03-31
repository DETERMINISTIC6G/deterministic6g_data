import math

xml_template = "<histogram>\n{bins}</histogram>"

bin_template = '    <bin low="{lower_bound}">{count}</bin>\n'


def np_hist_to_bins(n, bins, unit):
    final_rows = [{
        'count': 0,
        'lower_bound': str(-math.inf) + " " + unit,
        'upper_bound': math.inf
    }]

    for i in range(0, len(n)):
        final_rows.append({
            'count': n[i],
            'lower_bound': str(bins[i]) + unit,
            'upper_bound': str(bins[i + 1]) + unit
        })

    final_rows[0]['upper_bound'] = final_rows[1]['lower_bound']
    final_rows.append({
        'count': 0,
        'lower_bound': final_rows[-1]['upper_bound'],
        'upper_bound': str(math.inf) + " " + unit
    })
    return final_rows


def write_bins(final_rows, out_name):
    # Check if lower bound is equal to upper bound of previous row
    bin_str = ''
    for i in range(0, len(final_rows)):
        if i == 0 or final_rows[i]['lower_bound'] == final_rows[i - 1]['upper_bound']:
            bin_str += bin_template.format(**final_rows[i])
        else:
            print("NOK!")
    xml = xml_template.format(bins=bin_str)
    # Write to file
    # print(xml)
    with open(out_name, 'w') as xmlfile:
        xmlfile.write(xml)
    print(out_name)

def write_traces(delays, timestamps=None, out_name=None):
    initial_timestamp = 0
    if timestamps is not None:
        initial_timestamp = timestamps[0]

    with open(out_name, 'w') as f:
        if timestamps is not None:
            for i in range(len(delays)):
                timestamp_to_add = timestamps[i] - initial_timestamp
                f.write(f"{delays[i]}ms,{timestamp_to_add}ns\n")
        else:
            for i in range(len(delays)):
                f.write(f"{delays[i]}ms\n")
    print(out_name)
