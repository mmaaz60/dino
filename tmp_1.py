import os
import shutil

image_names = [
    "000000320232.jpg",
    "000000319935.jpg",
    "000000319369.jpg",
    "000000318080.jpg",
    "000000316666.jpg",
    "000000316015.jpg",
    "000000315450.jpg",
    "000000312237.jpg",
    "000000311295.jpg",
    "000000309391.jpg",
    "000000308587.jpg",
    "000000305317.jpg",
    "000000304404.jpg",
    "000000303818.jpg",
    "000000303566.jpg",
    "000000302030.jpg",
    "000000299553.jpg",
    "000000296231.jpg",
    "000000293324.jpg",
    "000000292997.jpg",
    "000000292446.jpg",
    "000000289741.jpg",
    "000000288685.jpg",
    "000000287527.jpg",
    "000000286908.jpg",
    "000000077460.jpg",
    "000000042276.jpg",
]
image_dir = "/home/maaz/PycharmProjects/dino/images/dino_boxes/dino_boxes/dino_boxes_combined"
save_dir = "/home/maaz/PycharmProjects/dino/images/dino_boxes/dino_boxes/difficult"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for image_name in image_names:
    image_path = f"{image_dir}/{image_name}"
    shutil.copy(image_path, f"{save_dir}/{image_name}")
