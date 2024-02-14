#######################################
# Leon Doungala - 13 /02 / 2024
#########################################
#Bird stats

"""
The number of birds banded at a series of sampling sites has been counted by your field crew and
entered into the following list. The first item in each sublist is an alphanumeric code for the site and
the second value is the number of birds banded.

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0], ['A5', 10], ['A6', 22], ['A7', 30], ['A8',
19], ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25], ['B5', 9], ['B6', 38], ['B7', 21], ['B8',
12], ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3], ['D1', 0], ['D2', 5], ['D3', 55], ['D4',
62],['D5', 98], ['D6', 32]]


        Write a script to answer these questions:
        - How many sites are there?
        - How many birds were counted at the 7th site?
        - How many birds were counted at the last site?
        - What is the total number of birds counted across all sites?
        - What is the average number of birds seen on a site?
        - What is the total number of birds counted on sites with codes beginning with C? (don’t just
        identify these sites by eye, in the real world there could be hundreds or thousands of sites)

"""

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0], ['A5', 10], ['A6', 22], ['A7', 30], ['A8',
19], ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25], ['B5', 9], ['B6', 38], ['B7', 21], ['B8',
12], ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3], ['D1', 0], ['D2', 5], ['D3', 55], ['D4',
62],['D5', 98], ['D6', 32]]



###########################################
#  Version 2 : Version using pandas 
###########################################

print("-----Version 2 : Version using pandas---\n")
# How many sites are there?

num_sites = len(data)
print("- Number of sites:", num_sites)

# How many birds were counted at the 7th site?

birds_7th_site = data[6][1]  
print("- Number of birds at the 7th site:", birds_7th_site)

# How many birds were counted at the last site?

birds_last_site = data[-1][1]  # negative indexing for the last element
print("- Number of birds at the last site:", birds_last_site)

# What is the total number of birds counted across all sites?

total_birds = sum(bird_count for site, bird_count in data)
print("- Total number of birds counted across all sites:", total_birds)

# What is the average number of birds seen on a site?

average_birds_per_site = total_birds / num_sites
print("- Average number of birds seen on a site:", average_birds_per_site)

# What is the total number of birds counted on sites with codes beginning with C?

birds_sites_with_C = sum(bird_count for site, bird_count in data if site.startswith('C'))
print("- Total number of birds counted on sites with codes beginning with C:", birds_sites_with_C)



###########################################
#Version 1 : Using python 3 
###########################################
print("----Using python 3 --------\n")

import subprocess
import sys

# Define the command to install pandas using pip
pip_command = [sys.executable, '-m', 'pip', 'install', 'pandas']

# Run the pip command
try:
    subprocess.check_call(pip_command)
except subprocess.CalledProcessError as e:
    print("Error:", e)

# Import pandas after installation
import pandas as pd


# Convert data to DataFrame
data_df = pd.DataFrame(data, columns=['Site', 'Birds'])


# How many sites are there?

number_sites_v1 = len(data)
print("- Number of sites(version using pandas ):", number_sites_v1)

# How many birds were counted at the 7th site?

birds_7th_site_v1 = data_df["Birds"][6]
print("- Number of birds at the 7th site(version using pandas ):", birds_7th_site_v1)


# How many birds were counted at the last site?

birds_last_site_v1 = data_df['Birds'].iloc[-1]  # negative indexing for the last element
print("- Number of birds at the last site (version using pandas ):", birds_last_site_v1)


# What is the total number of birds counted across all sites?

total_birds_v1 = data_df["Birds"].sum()
print("- Total number of birds counted across all sites (version using pandas ):", total_birds_v1)


# What is the average number of birds seen on a site?

average_birds_per_site_v1 = data_df["Birds"].mean()
print("- Average number of birds seen on a site (version using pandas ):", average_birds_per_site_v1)


# What is the total number of birds counted on sites with codes beginning with C?

Site_list = []
for site in data_df['Site']:
    if site.startswith('C'):
        Site_list.append(site)

birds_sites_with_C_v1 = data_df[data_df['Site'].isin(Site_list)]

print("- Total number of birds counted on sites with codes beginning with C (version using pandas ):",(birds_sites_with_C_v1['Birds'].sum()))