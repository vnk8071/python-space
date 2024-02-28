import itertools

import bentoml
import mlflow
import pandas as pd


@bentoml.service(resources={"cpu": "2"}, traffic={"timeout": 10})
class GenreClassifier:
    def __init__(self):
        self.model = mlflow.sklearn.load_model("results/model_export")
        print("Loaded Model:", self.model)

    @bentoml.api(route="/api/predict")
    def predict(self, inputs):
        df_predict = pd.DataFrame.from_dict([inputs])
        used_columns = list(
            itertools.chain.from_iterable(
                [x[2] for x in self.model["preprocessor"].transformers]
            )
        )
        pred_class = self.model.predict(df_predict[used_columns])[0]
        return {"class": pred_class}


if __name__ == "__main__":
    inputs = {
        "danceability": 0.711,
        "energy": 0.884,
        "key": 9,
        "loudness": -5.396,
        "mode": 1,
        "speechiness": 0.1989999999999999,
        "acousticness": 0.004,
        "instrumentalness": 0.442,
        "liveness": 0.0798,
        "valence": 0.206,
        "tempo": 145.02200000000005,
        "duration_ms": 398897,
        "time_signature": 4,
        "song_name": "",
        "title": "Psytrance New Releases 2020",
        "text_feature": "Psytrance New Releases 2020",
    }
    bento_service = GenreClassifier()
    pred_class = bento_service.predict(inputs)["class"]
    print("Predicted class:", pred_class)
