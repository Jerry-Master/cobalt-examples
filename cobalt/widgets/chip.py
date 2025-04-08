# Copyright (C) 2023-2024 BlueLightAI, Inc. All Rights Reserved.
#
# Any use, distribution, or modification of this software is subject to the
# terms of the BlueLightAI Software License Agreement.

import ipyvuetify as v


def Chip(*args, **kwargs):
    defaults = {"dense": True, "label": True}

    defaults.update(kwargs)

    return v.Chip(*args, **defaults)
