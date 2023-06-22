import numpy as np
import pandas as pd






def img_proc (name):
    """Loads image csv data from file name and returns the mean and SD"""
    img = np.genfromtxt(name, delimiter=",", dtype=float)
    array_mean = np.mean(img)
    array_SD = np.std(img)
    return array_mean, array_SD

print(img_proc ("test_image0.csv"))

#Random image
def random_image():
    a_image = 255 * np.random.rand(50, 50)
    a_image = np.round(a_image, 2)
    #  a_image_frame = pd.DataFrame(a_image)
    #  a_image_frame.to_csv("image_randompd.csv")
    np.savetxt("image_random.csv", a_image, delimiter=",")

# #test image
def test_image(const):
    a_image = np.zeros((50, 50), dtype=float)+const
    a_image = np.round(a_image, 2)
    np.savetxt(f"test_image{const}.csv", a_image, delimiter=",")

# random_image()
# test_image(50)
