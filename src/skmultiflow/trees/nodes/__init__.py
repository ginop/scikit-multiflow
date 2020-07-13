"""
The :mod:`skmultiflow.trees.nodes` module includes learning and split node
implementations for the hoeffding trees.
"""

from .core import FoundNode, Node, SplitNode, LearningNode, ActiveLeaf, InactiveLeaf, AdaNode
from .htc_nodes import ActiveLeafClass, LearningNodeMC, LearningNodeNB, LearningNodeNBA, \
    ActiveLearningNodeMC, InactiveLearningNodeMC, ActiveLearningNodeNB, ActiveLearningNodeNBA
from .hatc_nodes import AdaSplitNode, AdaLearningNode  # TODO: verify name
from .arf_htc_nodes import RandomActiveLeafClass, RandomActiveLearningNodeMC, \
    RandomActiveLearningNodeNB, RandomActiveLearningNodeNBA
from .efdtc_nodes import EFDTSplitNode, EFDTActiveLearningNodeMC, EFDTInactiveLearningNodeMC, \
    EFDTActiveLearningNodeNB, EFDTActiveLearningNodeNBA
from .lc_htc_nodes import LCActiveLearningNodeMC, LCInactiveLearningNodeMC, \
    LCActiveLearningNodeNB, LCActiveLearningNodeNBA
from .htr_nodes import LearningNodeMean, LearningNodePerceptron, ActiveLearningNodeMean, \
    ActiveLearningNodePerceptron, InactiveLearningNodeMean, InactiveLearningNodePerceptron
from .arf_htr_nodes import RandomActiveLeafRegressor, RandomActiveLearningNodeMean, \
    RandomActiveLearningNodePerceptron
from .hatr_nodes import AdaSplitNodeRegressor, AdaActiveLearningNodeRegressor


# TODO continue from here
from .isouptr_nodes import ActiveLearningNodePerceptronMultiTarget, \
    ActiveLearningNodeAdaptiveMultiTarget, InactiveLearningNodePerceptronMultiTarget, \
    InactiveLearningNodeAdaptiveMultiTarget
from .sst_htr_nodes import SSTActiveLearningNode, SSTActiveLearningNodeAdaptive, \
    SSTInactiveLearningNode, SSTInactiveLearningNodeAdaptive


__all__ = ["FoundNode", "Node", "SplitNode", "LearningNode", "ActiveLeaf", "InactiveLeaf",
           "AdaNode", "ActiveLeafClass", "LearningNodeMC", "LearningNodeNB", "LearningNodeNBA",
           "ActiveLearningNodeMC", "InactiveLearningNodeMC", "ActiveLearningNodeNB",
           "ActiveLearningNodeNBA", "RandomActiveLeafClass", "RandomActiveLearningNodeMC",
           "RandomActiveLearningNodeNB", "RandomActiveLearningNodeNBA", "AdaSplitNode",
           "AdaLearningNode", "EFDTActiveLeaf", "EFDTSplitNode", "EFDTActiveLearningNodeMC",
           "EFDTInactiveLearningNodeMC", "EFDTActiveLearningNodeNB", "EFDTActiveLearningNodeNBA",
           "LCActiveLearningNodeMC", "LCInactiveLearningNodeMC", "LCActiveLearningNodeNB",
           "LCActiveLearningNodeNBA", "LearningNodeMean", "LearningNodePerceptron",
           "ActiveLearningNodeMean", "ActiveLearningNodePerceptron", "InactiveLearningNodeMean",
           "InactiveLearningNodePerceptron", "RandomActiveLeafRegressor",
           "RandomActiveLearningNodeMean", "RandomActiveLearningNodePerceptron",
           "AdaSplitNodeRegressor", "AdaActiveLearningNodeRegressor",
           "ActiveLearningNodeForRegressionMultiTarget", "ActiveLearningNodePerceptronMultiTarget",
           "ActiveLearningNodeAdaptiveMultiTarget", "InactiveLearningNodePerceptronMultiTarget",
           "InactiveLearningNodeAdaptiveMultiTarget", "SSTActiveLearningNode",
           "SSTActiveLearningNodeAdaptive", "SSTInactiveLearningNode",
           "SSTInactiveLearningNodeAdaptive"]
