
class CommandConstruct:
    def __init__(self, python_path, robot_path, output_path, variable_path, planner_date, tst_inc, tag_inc, tag_exc,
                 suite_inc):
        self.final_command = ""
        self.cmd_command = ""
        self.tst_inc_command = ""
        self.suite_inc_command = ""
        self.python_path = python_path
        self.robot_path = robot_path
        self.output_path = output_path
        self.variable_path = variable_path
        self.planner_date = planner_date
        self.tst_inc = tst_inc
        self.tag_inc = tag_inc
        self.tag_exc = tag_exc
        self.suite_inc = suite_inc

    def construct_command(self):
        if self.tst_inc != 0:
            self.tst_inc_command = f"--task {self.tst_inc}"
        if self.tag_inc != 0:
            self.final_command += self.tag_inc
        if self.tag_exc != 0:
            self.final_command += self.tag_exc
        if self.suite_inc != 0:
            self.suite_inc_command = f"--suite {self.suite_inc}"

        self.cmd_command = f"{self.python_path} -m robot.run {self.tst_inc_command} {self.suite_inc_command}"

        return self.cmd_command


