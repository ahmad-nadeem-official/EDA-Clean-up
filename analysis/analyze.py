import pandas as pd


class Analysis:

    def __init__(self, file):
        self.file = file

    def shape(self):
        return self.file.shape

    def head(self):
        return self.file.head()

    def tail(self):
        return self.file.tail()

    def columns(self):
        return self.file.columns

    def info(self):
        self.file.info()

    def describe(self):
        return self.file.describe(include="all")


# data = pd.read_csv(
#     r"/home/ahmad/workshop/EDA-Clean-up/res/Titanic-Dataset.csv"
# )

# pic = Analysis(data)

# print(pic.columns())
# print(pic.describe())
# print(pic.head())
# pic.info()
# print(pic.shape())