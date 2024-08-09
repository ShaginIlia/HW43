import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                        format='%(asctime)s | %(levelname)s | %(message)s', encoding='UTF-8', )

import HW43
import unittest

"""
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. 
Далее 10 раз у объектов вызываются методы run и walk соответственно. 
Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов."""


def frozen_test(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print('Тесты в этом кейсе заморожены')
        else:
            func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    #is_frozen = False

    #@frozen_test
    def test_walk(self):
        try:
            sportsmen = HW43.Runner('Коля', -5)
            for i in range(10):
                sportsmen.walk()
            self.assertEqual(sportsmen.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            sportsmen = HW43.Runner(11341, 10)
            for i in range(10):
                sportsmen.run()
            self.assertEqual(sportsmen.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        sportsmen = HW43.Runner('Коля')
        sportsmen2 = HW43.Runner('Саша')
        for i in range(10):
            sportsmen.walk()
            sportsmen2.run()
        self.assertNotEqual(sportsmen.distance, sportsmen2.distance)


if __name__ == "__main__":
    unittest.main()
