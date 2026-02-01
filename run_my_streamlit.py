# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 18:38:34 2026

@author: Owner
"""
#Python file for deploying streamlit app on Spyder

import subprocess

file = "app_profiler_Tiffany.py"

subprocess.Popen(
    ["streamlit", "run", file], shell=True
)
