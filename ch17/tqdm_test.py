import time
from tqdm import tqdm

for i in tqdm(range(100), desc='test', ascii=True):
    time.sleep(.01)
