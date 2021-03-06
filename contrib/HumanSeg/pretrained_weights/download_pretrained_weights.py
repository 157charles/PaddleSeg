# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_PATH = os.path.join(LOCAL_PATH, "../../../", "test")
sys.path.append(TEST_PATH)

from test_utils import download_file_and_uncompress

model_urls = {
    "humanseg_server":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_server.zip",
    "humanseg_server_export":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_server_export.zip",
    "humanseg_mobile":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_mobile.zip",
    "humanseg_mobile_export":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_mobile_export.zip",
    "humanseg_mobile_quant":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_mobile_quant.zip",
    "humanseg_lite":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_lite.zip",
    "humanseg_lite_export":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_lite_export.zip",
    "humanseg_lite_quant":
    "https://paddleseg.bj.bcebos.com/humanseg/models/humanseg_lite_quant.zip",
}

if __name__ == "__main__":
    for model_name, url in model_urls.items():
        download_file_and_uncompress(
            url=url,
            savepath=LOCAL_PATH,
            extrapath=LOCAL_PATH,
            extraname=model_name)

    print("Pretrained Model download success!")
