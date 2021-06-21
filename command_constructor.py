
class CommandConstruct:
    def __init__(self, python_path, robot_path, output_path, planner_date, tst_inc, tst_exc, tag_inc, tag_exc,
                 suite_inc, suite_exc):
        self.final_command = ""
        self.python_path = python_path
        self.robot_path = robot_path
        self.output_path = output_path
        self.planner_date = planner_date
        self.tst_inc = tst_inc
        self.tst_exc = tst_exc
        self.tag_inc = tag_inc
        self.tag_exc = tag_exc
        self.suite_inc = suite_inc
        self.suite_exc = suite_exc

    def construct_command(self):
        if self.tst_inc != 0:
            self.final_command += self.tst_inc
        if self.tst_exc != 0:
            self.final_command += self.tst_exc
        if self.tag_inc != 0:
            self.final_command += self.tag_inc
        if self.tag_exc != 0:
            self.final_command += self.tag_exc
        if self.suite_inc != 0:
            self.final_command += self.suite_inc
        if self.suite_exc != 0:
            self.final_command += self.suite_exc

        self.final_command += self.python_path
        self.final_command += self.robot_path
        self.final_command += self.output_path
        self.final_command += self.planner_date

        return self.final_command


