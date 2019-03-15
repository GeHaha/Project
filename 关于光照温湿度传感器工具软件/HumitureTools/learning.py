# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:23:49 2019

@author: Gehaha
"""

from __future__ import print_function
from keras.preprocessing.image import load_img ,img_to_array
from scipy.misc import imsave
import numpy as np
from scipy.optimize import fmin_l_bfgs_b
import time
import argparse
from keras.applications import vgg16
from kears import backend as k

parser = argparse.ArgumentParser(description = 'Neural style transfer with keras')
parser.add_argument('base_image_path',metavar = 'base',type = str,
                    help = 'Path to the image to transform')
parser.add_argument('style_reference_image_path',metavar = 'ref',type=str,
                    help = 'Path to the style reference image.')
parser.add_argument('result_prefix', metavar='res_prefix', type=str,
                    help='Prefix for the saved results.')
parser.add_argument('--iter', type=int, default=10, required=False,
                    help='Number of iterations to run.')
parser.add_argument('--content_weight', type=float, default=0.025, required=False,
                    help='Content weight.')
parser.add_argument('--style_weight', type=float, default=1.0, required=False,
                    help='Style weight.')
parser.add_argument('--tv_weight', type=float, default=1.0, required=False,
                    help='Total Variation weight.')


args = parser.parse_args()
base_image_path = args.base_image_path
style_reference_image_path = args.style_reference_image_path
result_prefix = args.result_prefix
iterations = args.iter


# these are the weights of the different loss components
total_variation_weight = args.tv_weight
style_weight = args.style_weight
content_weight = args.content_weight


# dimensions of the generated picture
width,height = load_img(base_image_path).size
img_nrows = 400
img_ncols = int(width * img_nrows / height)


# util function to open ,resize and format pictures into appropriate tensors
def preprocess_image(image_path):
    img = load_img(image_path,atrget_size = (img_nrows,img_ncols))
    img = img_to_array(img)
    img = np.expand_dims(img,axis = 0)
    img = vgg16.preprocess_input(img)
    return img

# util function to convert a tensor into a valid image

def deprocess_image(x):
    if K.image_data_format() == 'channels_first':
        x = x.reshape((3,img_nrows,img_ncols))
        x = x.transpose((1,2,0))
    else:
        x = x.reshape((img_nrows,img_ncols,3))
    
    # remove zero-center by mean pixel
    x[:,:,0] += 103.939
    x[:,:,1] += 116.779
    x[:,:,2] += 123.68
    
    # 'BGR'->'RGB'
    x = x[:,:,::-1]
    x = np.clip(x,0,255).astype('uint8')
    return x

#get tensor representation of our images

base_image = K.variable(preprocess_image(base_image_path))
style_reference_image = K.variable(preprocess_image(style_reference_image_path))
        
    
# this will contain our generated image

if K.image_data_fprmate() == 'channels_first':
    combination_image = K.placeholder((1,3,img_nrows,img_ncols))
else:
    combination_image = K.placeholder((1,img_nrows,img_ncols))

# combine the 3 images into a single keras tensor

input_tensor = K.concatenate([base_image,style_reference_image,combination_image],axis = 0)
model = vgg16.VGG16(input_tensor = input_tensor,
                    weights = 'imagenet',include_top = False)
print('Model loaded')
outputs_dict = dict([(layer.name,layer.output) for layer in model.layers ])

#  compute the neural style loss
# first we need to define 4 util functions
# the gram  matrix of an image tensor(feature-wise outer product)


def gram_matrix(x):
    assert K.ndim(x) == 3
    if K.image_data_format() == 'channels_first':
        features = K.batch_flatten(x)
        