import os
import re
import shutil
import pandas as pd


def divide_file_to_folder(folder_path):
    """
    Function to divide the csv files based on the laptop's series for every brand
    - Acer: aspire, nitro, swift
    - Asus: rog, tuf, vivobook, zenbook
    - Dell: inspiron
    - HP: envy, omen, pavilion
    - Lenovo: ideapad, legion, yoga
    - MSI: alpha, gfthin, modern, prestige

    :param folder_path: string contains the directory of brand's folder
    """

    # get the list of all the csv files in the brand's folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # the regex to get the laptop's series from csv file's name
    file_regex = r"([^_]+)_tokped_[\d_]+\.csv"
    # get the available laptop's series name from the brand
    brand_series = list(
        set([re.search(file_regex, path).group(1) for path in csv_files if re.search(file_regex, path)]))

    # make subfolder in the brand's folder based on laptop's series
    for series in brand_series:
        subfolder_path = os.path.join(folder_path, series)
        os.makedirs(subfolder_path, exist_ok=True)

    # move the csv files from brand's folder to the series subfolder based on the laptop's series
    for file in csv_files:
        for series in brand_series:
            if series in file:
                src_file_path = os.path.join(folder_path, file)
                dest_folder_path = os.path.join(folder_path, series)
                shutil.move(src_file_path, dest_folder_path)
                break


def merge_file(folder, folder_path, destination):
    """
    Function to merge the data in csv files based on the laptop's brand name

    :param folder: string contains the name of brand's folder
    :param folder_path: string contains the directory of brand's folder
    :param destination: string contains the directory of the folder to place the merging result
    """

    # set a new list variable to place the name of the csv files that want to be merged
    df_brand_list = []

    # loop for the available series in the brand
    for series in os.listdir(folder_path):
        series_path = os.path.join(folder_path, series)

        # get the list of csv files based on the laptop brand's series
        csv_type_files = [file for file in os.listdir(series_path) if file.endswith('.csv')]

        # add column 'series' in each csv files and put the series name as the value of the column for each row
        # place the csv file's name into the list of files that want to be merged
        for file_path in csv_type_files:
            df = pd.read_csv(os.path.join(series_path, file_path))
            df['series'] = series
            df_brand_list.append(df)

    # merged all the csv files as a new dataset based on laptop brand's name
    df_merged = pd.concat(df_brand_list, ignore_index=True)

    # add column 'brand' in the dataset and put the brand name as the value of the column for each row
    df_merged['brand'] = folder

    # add the merged dataset into the folder 'merged'
    output_path = os.path.join(destination, f'merged_{folder}.csv')
    df_merged.to_csv(output_path, index=False)


def main():
    """
    Function that acts as the entry point to start the merging process of dataset

    Data condition:
    - Before merging: all csv files located based on brand only (Acer, Asus, Dell, HP, Lenovo, MSI)
    - After merging: a csv file as merged dataset with the labelling of the laptop's brand and the series
    """

    # get the current working directory as a root directory
    os.getcwd()

    # the location of all the csv files
    data_path = 'data'
    # get each folder's name in the folder 'data' -> 'Acer', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI'
    subfolders = [subf for subf in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, subf))]

    # set a new folder as a temporary place of merged file based on the brand name
    new_folder_merged = 'data/merged'
    if not os.path.exists(new_folder_merged):
        os.mkdir(new_folder_merged)

    # loop for every subfolder in the folder 'data' (except folder 'merged')
    for folder in subfolders:
        if folder != 'merged':
            folder_path = os.path.join(data_path, folder)

            # divide each brand based on the series of laptop's brand
            divide_file_to_folder(folder_path)

            # merge the csv files based on the laptop's brand data
            merge_file(folder, folder_path, new_folder_merged)

    # set a new list variable to place the name of the csv files that want to be merged
    df_merged_list = []

    # get the list of csv files based on the laptop's brand
    csv_merged_subfiles = [merged_type_to_brand for merged_type_to_brand in os.listdir(new_folder_merged) if
                           merged_type_to_brand.endswith('.csv')]

    # loop for the available laptop's brand merged dataset
    # place the csv file's name into the list of files that want to be merged
    for file_path in csv_merged_subfiles:
        df = pd.read_csv(os.path.join(new_folder_merged, file_path))
        df_merged_list.append(df)

    # merged all the csv files as a whole new merged dataset
    merged_df = pd.concat(df_merged_list, ignore_index=True)

    # add the whole new merged dataset to folder 'data'
    output_file_path = os.path.join(data_path, f'merged_all_brand.csv')
    merged_df.to_csv(output_file_path, index=False)


if __name__ == "__main__":
    main()
