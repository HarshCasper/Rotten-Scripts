#!/usr/bin/env python3

# Imports

import librosa
import numpy as np

import os
import csv

# The Features to be Extracted as headers

header = "filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate"
for i in range(1, 21):
    header += f" mfcc{i}"
header += " label"
header = header.split()

# Creating a CSV File
csv_path = input("Enter the path for CSV file containing the features: ")
file = open(csv_path, "w", newline="")
with file:
    writer = csv.writer(file)
    writer.writerow(header)

# The Genres in Dataset
genres = "blues classical country disco hiphop jazz metal pop reggae rock".split()
print(
    "Enter the path of where you downloaded the Database"
    "Example - C:/Users/<user-name>/Downloads/GTZAN/"
)

database_path = input("Path: ")
for g in genres:
    # Traversing through various genres in the Dataset
    # Feed the complete path of the GTZAN folder
    for filename in os.listdir(database_path + "/" + g):

        # Traversing through various songs in a particular genre.

        songname = database_path + "/" + g + "/" + filename
        # Using LibRosa to determine the features
        y, sr = librosa.load(songname, mono=True, duration=30)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        to_append = f"{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}"
        for e in mfcc:
            to_append += f" {np.mean(e)}"
        to_append += f" {g}"

        # Writing all the information in the CSV
        file = open(csv_path, "a", newline="")
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())
