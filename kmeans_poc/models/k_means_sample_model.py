import logging

import pandas as pd

from sklearn.cluster import KMeans

from src.models import BaseModel
from src.data_processing import EmptyProcessor


class KMeansModel(BaseModel):
    """
    Example model implementation to demonstrate the approach
    Model that predicts the movie review text sentiment: is it positive or negative review.
    """

    def __init__(self, model_name='KMeans',
                 preprocessor=EmptyProcessor(),
                 postprocessor=EmptyProcessor()
                 ):
        """
        :param model_name: name of model
        :param preprocessor: TextPreprocessor object for text data in this example
        :param postprocessor: TextPostprocessor object for text data in this example
        :nclusters: predefined number of clusters
        """
        self.k_means = KMeans(n_clusters=2)

        super().__init__(model_name=model_name,
                         preprocessor=preprocessor,
                         postprocessor=postprocessor)


    def fit(self, X, y=None) -> None:
        """
        Fits model
        """
        logging.info("Fitting classifier")
        self.k_means.fit(X)
        logging.info("Finished fitting model")

    def predict(self, X) -> pd.DataFrame:
        """
        find cluster for X
        """
        y_predicted_cluster = self.k_means.predict(X)

        return y_predicted_cluster
