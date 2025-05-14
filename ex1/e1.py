import os
import shutil
from sklearn.model_selection import train_test_split

# 定义数据集路径
dataset_path = "flower_dataset"
categories = ["daisy", "dandelion", "rose", "sunflower", "tulip"]

# 创建train/val文件夹
os.makedirs("flower_dataset/train", exist_ok=True)
os.makedirs("flower_dataset/val", exist_ok=True)

# 按类别划分数据
for category in categories:
    src_path = os.path.join(dataset_path, category)
    images = [f for f in os.listdir(src_path) if f.endswith(".jpg")]
    train_files, val_files = train_test_split(images, test_size=0.2, random_state=42)
    
    # 创建类别子文件夹
    os.makedirs(os.path.join(dataset_path, "train", category), exist_ok=True)
    os.makedirs(os.path.join(dataset_path, "val", category), exist_ok=True)
    
    # 移动文件
    for f in train_files:
        shutil.copy(os.path.join(src_path, f), os.path.join(dataset_path, "train", category, f))
    for f in val_files:
        shutil.copy(os.path.join(src_path, f), os.path.join(dataset_path, "val", category, f))
        
        
# 生成classes.txt
with open("flower_dataset/classes.txt", "w") as f:
    for category in categories:
        f.write(f"{category}\n")

# 生成train.txt和val.txt
def generate_annotation_file(root_path, output_file):
    with open(output_file, "w") as f:
        for idx, category in enumerate(categories):
            img_dir = os.path.join(root_path, "val", category)
            for img in os.listdir(img_dir):
                f.write(f"{category}/{img} {idx}\n")

# generate_annotation_file("flower_dataset", "flower_dataset/train.txt")
generate_annotation_file("flower_dataset", "flower_dataset/val.txt")