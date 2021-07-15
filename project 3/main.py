import cv2
import numpy as np


def calculate_dots_and_compress(u, sigma, v, k):
    product = np.dot(u[:, :k], np.diag(sigma[:k])).dot(v[:k, :])
    product[product < 0] = 0
    product[product > 255] = 255
    return np.rint(product).astype('uint8')


def singular_value_decomposition(image, k):
    array = np.array(image)

    r_u, r_sigma, r_v = np.linalg.svd(array[:, :, 0])
    r = calculate_dots_and_compress(r_u, r_sigma, r_v, k)

    g_u, g_sigma, g_v = np.linalg.svd(array[:, :, 1])
    g = calculate_dots_and_compress(g_u, g_sigma, g_v, k)

    b_u, b_sigma, b_v = np.linalg.svd(array[:, :, 2])
    b = calculate_dots_and_compress(b_u, b_sigma, b_v, k)

    return np.stack((r, g, b), axis=2)


if __name__ == "__main__":
    for i in [10, 50, 100, 150, 250, 1000]:
        for j in [1]:
            name = "original pictures\\" + str(j) + ".bmp"
            dest = "result" + str(j) + "\\" + "k=" + str(i) + ".bmp"
            img = cv2.imread(name)
            result = singular_value_decomposition(img, i)
            cv2.imwrite(dest, result)
