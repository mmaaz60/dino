import os
import cv2

# image_names = ['000009.jpg', '000005.jpg', '000000500716.jpg', '000000565469.jpg', '000016.jpg', '000007.jpg',
#                '000000031749.jpg', '000000429530.jpg', '000000331569.jpg', '000000334977.jpg', '000012.jpg',
#                '000000097585.jpg']

images_dir = "/home/maaz/PycharmProjects/dino/visualizations/test_images"
dino_attn_bbox_dir = "/home/maaz/PycharmProjects/dino/images/dino_boxes/dino_boxes/attention"
save_path = "/home/maaz/PycharmProjects/dino/images/dino_boxes/dino_boxes/combined"

image_names = os.listdir(images_dir)

if not os.path.exists(save_path):
    os.makedirs(save_path)

for image_name in image_names:
    image_path = f"{images_dir}/{image_name}"
    dino_path = f"{dino_attn_bbox_dir}/{image_name}"
    image = cv2.imread(image_path)
    dino_image = cv2.imread(dino_path)
    h, w, _ = image.shape
    d_h, d_w, _ = dino_image.shape
    resize_h = d_h
    resize_w = int(w * (d_h / h))
    resized_image = cv2.resize(image, (resize_w, resize_h))
    final_image = cv2.hconcat((resized_image, dino_image))
    cv2.imwrite(f"{save_path}/{image_name}", final_image)
