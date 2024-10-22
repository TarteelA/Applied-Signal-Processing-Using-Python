import os
import soundfile as sf
import numpy as np

# Specify the directory containing your .wav files
directory_path = 'train/MelospizaMelodia'  # Replace with your actual directory path

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.wav'):  # Check if the file is a .wav file
        file_path = os.path.join(directory_path, filename)  # Create full file path
        try:
            # Load the .wav file
            signal, fs = sf.read(file_path)

            # Calculate amplitude
            A = np.max(np.abs(signal))

            # Print the sampling frequency and amplitude
            print(f"File: {filename} | Sampling Frequency (fs): {fs} | Amplitude (A): {A}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")