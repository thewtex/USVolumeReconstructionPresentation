#!/bin/sh

# Run this script to do the volume reconstruction.
#
# Must:
#
# Symlink the
#
#   partial_p14_f05
#
# data directory in the top of the repository.
#
# Put
#
# - ConvertInnerOpticToPlus (from TubeTK)
# - VolumeReconstructor (from Plus)
#
# in the PATH.

inneroptic_metadata=$PWD/partial_p14_f05/log2013_09_25_07_54_59/ultrasound_frames_2013_09_25_08_03_06/reexported_tracking_data_f_Kitware_v2.txt

ConvertInnerOpticToPlus $inneroptic_metadata data/Sequence.mha
ConvertInnerOpticToPlus $inneroptic_metadata -s 55 -e 60 data/SubSequence.mha

VolumeReconstructor --config-file=data/VolumeReconstruction.xml \
  --source-seq-file=data/Sequence.mha \
  --output-volume-file=data/Reconstructed.mha
