import paddle
import torch
import numpy

if __name__ == '__main__':
    paddle.utils.run_check()
    print('hello fleet')
    print(torch.cuda.is_available())
