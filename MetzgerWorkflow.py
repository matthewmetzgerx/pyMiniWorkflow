import inspect
import sys
import logging

class MetzgerWorkflow:

    def __init__(self):
        logging.basicConfig(filename="reports/workflow.log", level=logging.INFO, filemode="w")

    def canRun(self, task, dependencies):
        """ Check if dependent on anything else
            to run.
        """
        return not (task in dependencies)

    def getParams(self,func, params):
        """ Get the required params for a function.
        """
        ps = inspect.signature(func).parameters.keys()
        return (params[p] for p in ps)

    def setNewParams(self, params, payload):
        """ Make return params available in the workflow
        """
        for key, val in payload.items():
            params[key] = val
        return params

    def processList(self, alltasks, rules, params):
        """ Sequence and process all workflow tasks until
            the workflow has been completely finished or
            failed.
        """
        wftasks, dependencies = rules.copy(), [d[1] for d in rules]
        for task in alltasks:
            if self.canRun(task, dependencies):
                addParams = self.getParams(task, params)
                logging.info("Start: " + str(task))
                response = task(*addParams)
                if response[0] == False:
                    logging.info("FAIL: " + response[1])
                    sys.exit(response[1])
                params = self.setNewParams(params, response[2])
                logging.info("Complete: " + str(task))
                wftasks = [t for t in wftasks if t[0] != task]
                alltasks = [t for t in alltasks if t != task]
                self.processList(alltasks, wftasks, params)
                break

    def runWorkflow(self, wf):
        """ Prepare and deliver all workflow tasks to processing
        """
        logging.info("WORKFLOW START" )
        alltasks = [d[0] for d in wf.workflow["tasks"]] + [d[1] for d in wf.workflow["tasks"]]
        self.processList(set(alltasks), wf.workflow["tasks"], wf.workflow["params"])
        logging.info("WORKFLOW COMPLETE")


