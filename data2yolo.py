from PIL import Image

anno_box_path = "E:\dataset\CelebA\Anno\list_bbox_celeba.txt"
label_dir = "E:\dataset\CelebA\Img\labels"
img_dir = "E:\dataset\CelebA\Img\img_celeba"
count = 0
epoch = 1

with open(anno_box_path, "r") as box_file:
    i = 0
    for line in box_file:
        if i < 2:
            i += 1
            continue
        i += 1

        imgname = line[0:6]
        img_strs = line.split()
        x1, y1, w, h = int(img_strs[1]), int(img_strs[2]), int(img_strs[3]), int(img_strs[4])
        x2, y2 = x1 + w, y1 + h

        img = Image.open(f"{img_dir}/{img_strs[0]}")
        img_w, img_h = img.size

        # ****************************
        dw = 1. / (int(img_w))
        dh = 1. / (int(img_h))
        x = ((x1 + x2) / 2.0 - 1) * dw
        y = ((y1 + y2) / 2.0 - 1) * dh
        w = (x2 - x1) * dw
        h = (y2 - y1) * dh
        # ****************************

        with open(f"{label_dir}\{imgname}.txt", "w") as label_txt:
            label_txt.write(f"0 {x} {y} {w} {h}\n")

        if i == 2000:
            exit()
