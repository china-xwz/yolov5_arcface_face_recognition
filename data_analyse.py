imgdir = r"E:\dataset\CelebA\Img/img_celeba"
attributepath = r"E:\dataset\CelebA\Anno\list_attr_celeba.txt"


def stats():
    with open(attributepath)as f:
        numofimgs = int(f.readline())
        line = f.readline()
        items = line.split()
        attrs = []
        for i in range(len(items)):
            attrs.append(items[i])
        # print(attrs)
        stats = []
        print(f"numofimgs:{numofimgs}\n\nline:{line}\nitems:{items}\n\nattrs{attrs}\n")
        for i in range(len(attrs)):
            stat = []
            stat.append(0)
            stat.append(0)
            stats.append(stat)
        print(f"stats:{stats}\n")

        for i in range(numofimgs):
            line = f.readline()
            items = line.split()[1:]
            for j in range(len(attrs)):
                if items[j] == "1":
                    stats[j][0] += 1
                else:
                    stats[j][1] += 1
        for i in range(len(attrs)):
            print(attrs[i], stats[i][0], stats[i][1])




if __name__ == "__main__":
    stats()
