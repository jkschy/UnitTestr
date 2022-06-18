import os
import sys
from inspect import getmembers, isfunction
from helpers.JsonHelp import verifySettings, getSetting
from helpers import Logger
sys.path.append(os.getcwd())

class GenericRunner:
    results: list[tuple] = []

    def __init__(self):
        """
        A Generic Runner to fun all files below "Tests" directory
        """
        verifySettings()

    def run_all_files(self):
        for file in os.listdir(getSetting("dir")):
            # Verify all files are python files
            if file.endswith(".py") and not file.startswith("__init__"):

                # Import the file
                file = __import__(f'Tests.{file.split(".")[0]}', fromlist=["tests"])

                # Gets all functions from the files
                tests = getmembers(file, isfunction)

                # Sep the Before, After and Test Files
                before_method = [test for test in tests if test[0] == "Before" or test[0] == "before"]
                after_method = [test for test in tests if test[0] == "After" or test[0] == "after"]
                test_methods = [test for test in tests if not before_method.__contains__(test)
                                and not after_method.__contains__(test)]
                self.__verify_before_and_after(before_method, after_method)

                before_res: any = None

                # Runs the Tests
                for test in test_methods:
                    print(f"\nRunning Test {test[0]}")

                    # Before
                    try:
                        if before_method:
                            before_res = before_method[0][1]()

                        # Runs the test and passes the before result into the test
                        test[1](before_res if before_res is not None else None)

                        # Passes
                        self.__pass(test[0])
                    except Exception as e:
                        # Fails
                        self.__fail(test[0])
                        Logger.Error(e.__str__())

                    finally:
                        # After
                        if after_method:
                            # In Case the After Fails
                            try:
                                after_method[0][1](before_res if before_res is not None else None)
                            except Exception as e:
                                Logger.Error(e.__str__(), "After")
                                self.results.pop()
                                self.__fail(test[0])

        self.__print_results()

    def __pass(self, name):
        self.results.append((name, u'\u2713'))

    def __fail(self, name):
        self.results.append((name, u'\u2A09'))

    def __print_results(self):
        print("\n\n\n")
        for res in self.results:
            print(f"{res[0]}: {res[1]}")

    def __verify_before_and_after(self, before, after):
        if len(before) > 1:
            raise Exception("We only support 1 before method in each suite")

        if len(after) > 1:
            raise Exception("We only support 1 after method in each suite")
