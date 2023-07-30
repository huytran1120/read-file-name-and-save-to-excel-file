import os
import pandas as pd
def get_file_names(directory):
    file_names = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_names.append(filename)
    return file_names
def save_to_excel(file_names, output_file):
    data = {"File Name": file_names}
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
if __name__ == "__main__":
    # Directory path containing the files you want to read
    input_directory = r"C:\Users\huytc\Pictures\Screenshots"
    # Excel file name to save file names
    output_excel = "output.xlsx"
    # Get a list of filenames
    file_names = get_file_names(input_directory)
    # save name file to file Excel
    save_to_excel(file_names, output_excel)
    print("File names have been saved to 'output.xlsx'.")
