import os
import shutil
import pandas as pd

# Paths
img_dir = 'C:/Users/hp/Desktop/hairstyle/img_align_celeba/img_align_celeba'
attr_file = 'C:/Users/hp/Desktop/hairstyle/list_attr_celeba.csv'
output_dir = 'C:/Users/hp/Desktop/hairstyle/gender_sorted_faces'

# Output folders
male_dir = os.path.join(output_dir, 'male')
female_dir = os.path.join(output_dir, 'female')
os.makedirs(male_dir, exist_ok=True)
os.makedirs(female_dir, exist_ok=True)

# Load CSV
df = pd.read_csv(attr_file)

# Make sure image names are the index
if 'image_id' in df.columns:
    df.set_index('image_id', inplace=True)

# Sort images
count = {'male': 0, 'female': 0}
for filename in os.listdir(img_dir):
    if filename not in df.index:
        continue

    gender_flag = df.loc[filename]['Male']
    gender = 'male' if gender_flag == 1 else 'female'
    dest_folder = male_dir if gender == 'male' else female_dir

    src_path = os.path.join(img_dir, filename)
    dst_path = os.path.join(dest_folder, filename)
    shutil.copy(src_path, dst_path)
    count[gender] += 1

print("✅ Sorting complete!")
print(f"👨 Males: {count['male']}")
print(f"👩 Females: {count['female']}")
