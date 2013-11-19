import SimpleITK as sitk
import sys
import os

if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + ' <sequence_file> <output_dir>')
    sys.exit(1)

sequence_file = sys.argv[1]
output_dir = sys.argv[2]

input_image = sitk.ReadImage(sequence_file)

number_of_frames = input_image.GetSize()[2]
frame_size = list(input_image.GetSize())
frame_size[2] = 1
frame_index = [0, 0, 0]
roi_first = sitk.RegionOfInterestImageFilter()
roi_first.SetSize(frame_size)
roi_first.SetIndex(frame_index)
roi_second = sitk.RegionOfInterestImageFilter()
roi_second.SetSize(frame_size)
roi_second.SetIndex(frame_index)
diff_image = sitk.Image(input_image)
for first_frame in range(number_of_frames - 1):
    frame_first = roi_first.Execute(input_image)
    frame_index[2] += 1
    roi_first.SetIndex(frame_index)
    roi_second.SetIndex(frame_index)
    frame_second = roi_second.Execute(input_image)

    frame_first = sitk.Cast(frame_first, sitk.sitkInt16)
    frame_second = sitk.Cast(frame_second, sitk.sitkInt16)
    frame_first.SetOrigin((0.0, 0.0, 0.0))
    frame_second.SetOrigin((0.0, 0.0, 0.0))
    diff = sitk.Subtract(frame_first, frame_second)
    print('Writing frame ' + str(first_frame))
    sitk.WriteImage(diff, os.path.join(output_dir,
        'frame_{0:04d}.tif'.format(first_frame)))
    sitk.WriteImage(diff, os.path.join(output_dir,
        'frame_{0:04d}.mha'.format(first_frame)))
