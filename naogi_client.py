from naogi import NaogiModel

class Model(NaogiModel):
    # the very first step, where you can download checkpoints or some big files
    # executes once before server starting
    def load_model(self):
        pass

    # model initialisation, result of this function can be accessed in other methods below as self.model
    def init_model(self):
        pass

    # request parameters (also binary data)
    def prepare(self, params):
        raise NotImplemented

    # main function for model prediction, result will be passed to Renrerer
    def predict(self):
        raise NotImplemented

    # returns class of render (by default it's JsonRenderer, but you can write your own)
    def renderer(self):
        raise NotImplemented
