# Data Wrangling & Visualization: Laptop Selling Analysis

## A. Background
Laptop is one of the important devices for daily activity due to the flexibility of bringing it everywhere if compared to a personal computer. There are many brand and series in the market. For marketplace, knowing the popular products based on the brand and series is important for generating product recommendations, understanding customer demand and trends, and highlighting well-known products to attract more traffic to marketplace.



## B. Objectives
This project is built to implement data wrangling skills by using data library Python and data visualization in Tableau. The highlighted steps in this project are enriching, structuring, cleaning the data, and visualizing the data.



## C. Dataset
The dataset is obtained from Kaggle named [**E-commerce Laptop Price Scraping**](https://www.kaggle.com/datasets/artakusuma/laptopecomercee). This project only uses the data in January 2021 from Tokopedia marketplace due to the different features between the available months. The other reason for using only the data in January is because it provides the selling sales amount of laptops for different laptop brands and types and also in the different shops for available dates.
The dataset consists of laptop brand and series which represented as the folder's name. In each folder of series's brand laptop, it consists of the sales data in `.csv` extension on a specific date in January 2021.

Details of available laptop's brand and series:
- Acer: aspire, nitro, swift
- Asus: rog, tuf, vivobook, zenbook
- Dell: inspiron
- HP: envy, omen, pavilion
- Lenovo: ideapad, legion, yoga
- MSI: alpha, gfthin, modern, prestige



## D. Workflow
This program contains two modules, which are `main.py` and `preprocessing.ipynb`:
1. File `merge_data.py` includes:
   - Function `divide_file_to_folder()` to divide the `.csv` files based on the laptop series for every brand.
   - Function `merge_file()` to merge the data in `.csv` files based on the laptop's brand name
   - Function `main()` as the entry point to start the merging process of the dataset
2. File `preprocessing.ipynb` includes:
   - Exploring and checking the dataset
   - Change the data type of some of the feature variables such as `price`, `sold`, and `date` in order to match the purpose of the feature variable for data manipulation
   - Text normalization
   - Enriching the dataset to obtain more informations
   - Adding important information regarding the laptop specification and deleting unimportant feature variable
   - Structuring the data as cleaned dataset



## E. Data Wrangling Result
- **Before**:
  ![image](https://github.com/novitaaryanti/laptop-selling-analysis-project/assets/138101831/47aea6ea-2908-44a2-9037-36049e14d284)

- **After**:
  ![image](https://github.com/novitaaryanti/laptop-selling-analysis-project/assets/138101831/936c5c2d-cfa4-4014-96a7-7f831d7a512a)



## F. Data Visualization
The data visualization is done in [Tableau](https://public.tableau.com/app/profile/novita.aryanti/viz/LaptopSellinginTokopediaJanuary2021/Dashboard1)
![Dashboard 1](https://github.com/novitaaryanti/laptop-selling-analysis-project/assets/138101831/9f746bff-e3ea-4cd9-9b78-8da1d9ef314b)
The data visualization obtains several information including:
1. The number of laptop sold in each day of January 2021*
2. Daily average selling per laptop from 14 - 29 January 2021
3. Distribution of Laptop Price in January 2021
4. Distribution of Laptop Price in each day of January 2021*
5. Top 5 selling of laptop product based on the shop in January 2021
6. Top 5 selling of laptop product based on the shop in each day of January 2021*
7. Comparison of laptop selling based on brand and series in January 2021
8. Comparison of laptop selling based on brand and series in each day of January 2021*

_*Note:_ open the visualization link to see the filter result
