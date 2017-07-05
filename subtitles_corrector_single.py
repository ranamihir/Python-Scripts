from datetime import datetime, timedelta

with open('<input_file_name>.srt', 'r') as f1:
    with open('<input_file_name>_corrected.srt', 'wb') as f2:
        data = f1.readlines()
        for i in range(len(data)):
            line = data[i].strip('\n')
            if ' --> ' in line:
                line_time = datetime.strptime(line.split(' --> ')[0].split(',')[0], '%H:%M:%S').time()
                if line_time > line_time.replace(minute=40, second=31, microsecond=888000):
                    start, end = line.split(' --> ')[0].split(','), line.split(' --> ')[1].split(',')
                    start_seconds, start_milliseconds = start[0], start[1]
                    end_seconds, end_milliseconds = end[0], end[1]

                    start_datetime = datetime.strptime(start_seconds, '%H:%M:%S')
                    end_datetime = datetime.strptime(end_seconds, '%H:%M:%S')

                    time_difference = timedelta(seconds=27, milliseconds=20 - int(start_milliseconds))
                    updated_start_datetime = start_datetime - time_difference
                    updated_end_datetime = end_datetime - time_difference

                    f2.write(str(updated_start_datetime.time())[:-3].replace('.', ',') + ' --> ' + str(updated_end_datetime.time())[:-3].replace('.', ',') + '\n')

                    i += 1
                else:
                    f2.write(line + '\n')
            else:
                f2.write(line + '\n')