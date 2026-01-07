import os
import shutil
import random

# Paths to your dataset
base_dir = r"C:\Users\adity\Soil classification IPYNB format\Soil classification Demo\Soil classification\Dataset"
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")
test_dir = os.path.join(base_dir, "test")

# Create val/test directories if not exist
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Loop through each soil type in the training folder
for class_name in os.listdir(train_dir):
    class_train_path = os.path.join(train_dir, class_name)
    if not os.path.isdir(class_train_path):
        continue

    # Create the same folders in val and test if missing
    class_val_path = os.path.join(val_dir, class_name)
    class_test_path = os.path.join(test_dir, class_name)
    os.makedirs(class_val_path, exist_ok=True)
    os.makedirs(class_test_path, exist_ok=True)

    # Collect all images for that class
    all_images = [f for f in os.listdir(class_train_path) if os.path.isfile(os.path.join(class_train_path, f))]

    # Shuffle and split for val/test
    random.shuffle(all_images)
    val_count = max(1, len(all_images) // 10)  # 10% for validation
    test_count = max(1, len(all_images) // 10) # 10% for testing

    val_images = all_images[:val_count]
    test_images = all_images[val_count:val_count + test_count]

    # Copy them
    for img in val_images:
        shutil.copy(os.path.join(class_train_path, img), os.path.join(class_val_path, img))
    for img in test_images:
        shutil.copy(os.path.join(class_train_path, img), os.path.join(class_test_path, img))

    print(f"✅ Synced {class_name}: {val_count} val, {test_count} test")

print("🎉 All soil types are now available in train, val, and test folders!")