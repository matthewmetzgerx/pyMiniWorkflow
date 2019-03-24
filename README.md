# pyMiniWorkflow
Mini workflow sequencer made in python. This utility enables the sequential exectution of python methods while allowing data to be raised into active state params and used by subsequent method executions. In layman's terms, it runs functions in order, and allows you to make content from one function available to another.

## Prerequisites
This project was built using Python 3. It uses publicly accessible libraries: 

* import inspect
* import sys
* import logging


## Installation
Presently, installation is only to add the MetzgerWorkflow class, import a workflow, and let her rip!
`
import workflow1, workflow2, workflow3
import MetzgerWorkflow as MWF

mwf = MWF.MetzgerWorkflow()
mwf.runWorkflow(workflow1) # WORKFLOW
mwf.runWorkflow(workflow2) # WORKFLOW
`

## Authors
This project was created by [Mattew Metzger](https://matthewmetzgerx.github.io/) and was built to complete a missing functional process in the Bellevue.edu DSC 550 coursework.
