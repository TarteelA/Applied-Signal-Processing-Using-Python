import os
import soundfile as sf
import numpy as np

# Specify the directory containing your .wav files
directory_path = 'train/Normal'  # Replace with your actual directory path

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.wav'):  # Check if the file is a .wav file
        file_path = os.path.join(directory_path, filename)  # Create full file path
        try:
            # Load the .wav file
            signal, fs = sf.read(file_path)

            # Calculate amplitude
            A = np.max(np.abs(signal))
            
            # Calculate duration in whole seconds (as an integer)
            duration = len(signal) // fs

            # Print only files with a duration of 5 seconds
            print(f"File: {filename} | Sampling Frequency (fs): {fs} | Amplitude (A): {A} | Duration: {duration} seconds")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
