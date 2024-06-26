from toolkit import prestack_analysis as gisis

obj = gisis.Prestack()

source_file = "example/geometry/source_file.txt"
receiver_file = "example/geometry/receiver_file.txt"
relational_file = "example/geometry/relational_file.txt"

time_samples = 1501
time_spacing = 2e-3
trace_number = 282
total_gathers = 251

for gather_index in range(total_gathers):

    input_path = f"example/data_bin/open_data_seg_poland_vibroseis_2ms_1501x282_shot_{gather_index+1}.bin"
    output_path = f"example/data_sgy/open_data_seg_poland_vibroseis_2ms_1501x282_shot_{gather_index+1}.sgy"

    obj.import_geometry(source_file, receiver_file, relational_file)

    obj.import_binary_data(time_samples, trace_number, input_path)

    obj.add_binary_data_trace_header(time_spacing, gather_index, trace_number, output_path)
