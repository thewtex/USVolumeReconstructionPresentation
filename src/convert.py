import SimpleITK as sitk
import sys

if len(sys.argv) < 3:
    print('Usage: convert.py <input_image> <output_image>')
    sys.exit(1)

input_image_file = sys.argv[1]
output_image_file = sys.argv[2]

input_image = sitk.ReadImage(input_image_file)
sitk.WriteImage(input_image, output_image_file)
