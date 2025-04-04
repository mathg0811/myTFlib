import ssl
from enum import Enum

ssl._create_default_https_context = ssl._create_unverified_context

__version__ = "0.1.0dev"


class LearningType(str, Enum):
    ONE_CLASS = "one_class"
    ZERO_SHOT = "zero_shot"
    FEW_SHOT = "few_shot"


class TaskType(str, Enum):
    CLASSIFICATION = "classification"
    DETECTION = "dectection"
    SEGMENTATION = "segmentation"