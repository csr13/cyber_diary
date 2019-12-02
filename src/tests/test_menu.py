import sys
import unittest

sys.path.append("..")

from menu.menu import Menu


class TestMenu(unittest.TestCase):

    def setUp(self):
        # create choices to use.
        self.menu_choices = ["1","2","3","4","5"]
        # create a test menu.
        self.test_menu = Menu(main_choices=self.menu_choices)


    def test_instance_creation(self):
        # for every choice in the range of the lenght of the menu choices
        for choice in range(len(self.test_menu.main_choices)):
            # assert that the choices to use match the set choices of the
            # test menu.
            self.assertEquals(
                self.menu_choices[choice],
                self.test_menu.main_choices[choice]
            )


    def test_set_choice_wrong_choice(self):
        """This function tests for the exception that is raised when
        passing a wrong choice to the menu"""
        # make a wrong choice
        wrong_choice = "wrong choice"
        # try to set it
        self.test_menu.set_current_choice = wrong_choice
        # asert the conditional statement of the set current choice works, 
        # its supposed to reset choice to None of given a value, then uses picks 
        # to check if the value is None, for recutsion.
        self.assertEquals(self.test_menu.current_choice, None)


    def test_set_correct_choice(self):
        """This function tests for picking the right menu choice"""
        # make a correct choice
        correct_choice = "1"
        # set the correct choice
        self.test_menu.set_current_choice = correct_choice
        # assert that the correct choice is in the main choices
        self.assertTrue(
            correct_choice in self.test_menu.main_choices,
            msg="correct choice in main choices"
        )
        # assert that the current choice 
        self.assertEquals(
            self.test_menu.get_current_choice,
            correct_choice,
            msg="correct choice equals current_choice"
        )


    def test_get_choice_works(self):
        """This just tests that we can get a choice, to use in our application"""
        # this is a spam choice
        spam_choice = "2"
        # this statement gives the spam choice,
        # which is a correct choice, to the menu. 
        self.test_menu.set_current_choice = spam_choice
        # get the choice we just set.
        menu_spam_choice = self.test_menu.get_current_choice
        # and assert that it equals the intial spam_choice
        self.assertEquals(spam_choice, menu_spam_choice)


    def tearDown(self):
        # for every test function the setUp method runs first,
        # then the test function, then this method.
        del self.test_menu


if __name__ == "__main__":
    unittest.main()

        