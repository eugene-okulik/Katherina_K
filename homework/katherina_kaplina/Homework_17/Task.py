import argparse
import os
import re


parser = argparse.ArgumentParser()
parser.add_argument("directory", help="directory name where the text was found")
parser.add_argument("text", help="search_text")

args = parser.parse_args()


def search_text_in_file(directory: str, text: str):
    result = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_result = []
            for line_number in range(len(lines)):
                line = lines[line_number]
                if text in line:
                    words = re.split(r"[, ]", line)
                    if text in words:
                        text_index = words.index(text)
                        if text_index < 5:
                            first = 0
                        else:
                            first = text_index - 5
                        last = text_index + 5
                        data = ' '.join(words[first:last])
                        file_result.append((line_number+1, data))
            result.append((file_path, file_result))
    return result


results = search_text_in_file(args.directory, args.text)

if not results:
    print("No needed text in the files from this directory")
else:
    for file_path_i, file_result_i in results:
        print(f"File: {file_path_i}")
        for line_number_i, data_i in file_result_i:
            print(f"       Line: {line_number_i} - Data: {data_i}")
