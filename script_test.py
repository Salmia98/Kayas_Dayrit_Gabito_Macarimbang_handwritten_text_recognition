# from PIL import Image
# import pandas as pd
# import os

# df = pd.read_csv("metadata/test_metadata.csv")

# for fn in df["file_name"]:
#     path = os.path.join("data/test_crops", fn)

#     try:
#         img = Image.open(path)
#         img.verify()
#     except Exception as e:
#         print("BAD IMAGE:", fn)
#         print(e)

# print("Done checking images.")

import torch

print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())

if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))