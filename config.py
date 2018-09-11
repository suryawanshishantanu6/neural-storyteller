"""
Configuration for the generate module
"""

#-----------------------------------------------------------------------------#
# Flags for running on CPU
#-----------------------------------------------------------------------------#
FLAG_CPU_MODE = True

#-----------------------------------------------------------------------------#
# Paths to models and biases
#-----------------------------------------------------------------------------#
paths = dict()

# Skip-thoughts
paths['skmodels'] = ''
paths['sktables'] = ''

# Decoder
paths['decmodel'] = 'romance.npz'
paths['dictionary'] = 'romance_dictionary.pkl'

# Image-sentence embedding
paths['vsemodel'] = 'coco_embedding.npz'

# VGG-19 convnet
paths['vgg'] = 'vgg19.pkl'
paths['pycaffe'] = ''
paths['vgg_proto_caffe'] = 'VGG_ILSVRC_19_layers_deploy.prototxt'
paths['vgg_model_caffe'] = 'VGG_ILSVRC_19_layers.caffemodel'


# COCO training captions
paths['captions'] = 'coco_train_caps.txt'

# Biases
paths['negbias'] = 'caption_style.npy'
paths['posbias'] = 'romance_style.npy'
