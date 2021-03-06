from __future__ import absolute_import

import os
from got10k.experiments import *

from siamfc import TrackerSiamFC

##############################################################
import sys
current_dir = os.getcwd()  # obtain work dir
sys.path.append(current_dir)  # add work dir to sys path
##############################################################
## IF you want to get the results from the original SiameseFC, go to 'siamfc/__init__.py' (siamfc folder) and comment the
## the code ""


if __name__ == '__main__':
    ## Absolute PATH for net
    # net_path = 'E:\PSUThirdSemester\CSE586ComputerVision\Term-Project1\Pythonversion\siamfc-pytorch-master\defaultpretrained\siamfc_alexnet_e1.pth'
    ## Relative PATH (if cannot not work using Absolute PATH based on your own computer)
    net_path = '.././defaultpretrained\siamfc_alexnet_e1.pth'

    tracker = TrackerSiamFC(net_path=net_path)

    ## Data Path
    root_dir = 'E:\PSUThirdSemester\CSE586ComputerVision\Term-Project1\Pythonversion\data\OTB100'
    e = ExperimentOTB(root_dir, version=2015,result_dir='results_KF_CF', report_dir='reports_KF_CF')
    e.run(tracker, visualize=False)
    e.report([tracker.name])
