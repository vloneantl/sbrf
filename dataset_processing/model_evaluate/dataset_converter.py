import fiftyone as fo
# path to images
data_path = "/Users/antonlukanov/Desktop/Sber/model_evaluate/val/images"

# The path to labels
labels_path = "/Users/antonlukanov/Desktop/Sber/model_evaluate/labels"

# Import the dataset
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.KITTIDetectionDataset,
    data_path=data_path,
    labels_path=labels_path,
)

# The directory to which to write the exported dataset
export_dir = "/Users/antonlukanov/Desktop/Sber/model_evaluate/Coco_results/16_09"

# The name of the sample field containing the label that you wish to export
# Used when exporting labeled datasets (e.g., classification or detection)
label_field = "ground_truth"  # for example
# The type of dataset to export
# Any subclass of `fiftyone.types.Dataset` is supported
dataset_type = fo.types.COCODetectionDataset  # for example

# Export the dataset
dataset.export(
    export_dir=export_dir,
    dataset_type=dataset_type,
    label_field=label_field,
)