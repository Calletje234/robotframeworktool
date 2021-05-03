
class CommandConstruct:
    def __init__(self, tst_inc=None, tst_exc=None, tag_inc=None, tag_exc=None,
                 suite_inc=None, suite_exc=None, python_path=None, robot_path=None,
                 planning=None):
        # INIT VARIABLES
        self.planning = planning
        self.tst_inc = tst_inc
        self.tst_exc = tst_exc
        self.tag_inc = tag_inc
        self.tag_exc = tag_exc
        self.suite_inc = suite_inc
        self.suite_exc = suite_exc

        self.python_path = python_path
        self.robot_path = robot_path

        self.constructed_command = str



