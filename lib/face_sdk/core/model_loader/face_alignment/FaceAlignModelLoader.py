import logging.config

logging.config.fileConfig("config/logging.conf")
logger = logging.getLogger('sdk')

import torch

from ..BaseModelLoader import BaseModelLoader


class FaceAlignModelLoader(BaseModelLoader):
    def __init__(self, model_path, model_category, model_name, meta_file='model_meta.json'):
        logger.info('Start to analyze the face landmark model, model path: %s, model category: %s，model name: %s' %
                    (model_path, model_category, model_name))
        super().__init__(model_path, model_category, model_name, meta_file)
        self.cfg['img_size'] = self.meta_conf['input_width']

    def load_model(self):
        try:
            if not torch.cuda.is_available():
                model = torch.load(self.cfg['model_file_path'], map_location=torch.device('cpu'))
            else:
                model = torch.load(self.cfg['model_file_path'])
        except Exception as e:
            logger.error('The model failed to load, please check the model path: %s!'
                         % self.cfg['model_file_path'])
            raise e
        else:
            logger.info('Successfully loaded the face landmark model!')
            return model, self.cfg
