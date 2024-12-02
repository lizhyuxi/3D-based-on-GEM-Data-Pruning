# python run_random_subset.py <ROOT:str> <EXP:str> <SIZE:int> <RUN:int>

from data_diet.train import train
import sys
from types import SimpleNamespace

# setup
ROOT = sys.argv[1]
EXP = sys.argv[2]
SIZE = int(sys.argv[3])
RUN = int(sys.argv[4])
META_MODEL_SEED, META_TRAIN_SEED, SEED_INCR = 42, 4242, 424242
META_SUBSET_SEED = 4426
EP_STEPS = 390
DATA_DIR = ROOT + '/data'
EXPS_DIR = ROOT + '/exps'

# arguments
args = SimpleNamespace()
# data
args.data_dir = DATA_DIR
args.dataset = 'cifar10'
# subsets
args.subset = 'random'
args.subset_size = SIZE
args.scores_path = None
args.subset_offset = None
args.random_subset_seed = META_SUBSET_SEED + RUN * SEED_INCR
# model
args.model = 'resnet18_lowres'
args.model_seed = META_MODEL_SEED + RUN * SEED_INCR
args.load_dir = None
args.ckpt = 0
# optimizer
args.lr = 0.1
args.beta = 0.9
args.weight_decay = 0.0005
args.nesterov = True
args.lr_vitaly = False
args.decay_factor = 0.2
args.decay_steps = [60*EP_STEPS, 120*EP_STEPS, 160*EP_STEPS]
# training
args.num_steps = 200*EP_STEPS
args.train_seed = META_TRAIN_SEED + RUN * SEED_INCR
args.train_batch_size = 128
args.test_batch_size = 1024
args.augment = True
args.track_forgetting = False
# checkpoints
args.save_dir = EXPS_DIR + f'/{EXP}/size_{SIZE}/run_{RUN}'
args.log_steps = EP_STEPS
args.early_step = 0
args.early_save_steps = None
args.save_steps = 1000 * EP_STEPS

# experiment
train(args)
