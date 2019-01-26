from data_generator import DataGenerator

PATH_TO_TRAIN_IMAGES = '../../data/train/images/full-image-dir'
PATH_TO_TRAIN_QUESTIONS = '../../data/train/questions/v2_OpenEnded_mscoco_train2014_questions.json'
PATH_TO_TRAIN_ANSWERS = '../../data/train/answers/v2_mscoco_train2014_annotations.json'
PATH_TO_TRAINED_GLOVE = '../../models/GloVe/glove.6B.50d.txt'
PATH_TO_WORD_VOCAB = '../../models/GloVe/vocab_only.txt'
PATH_TO_VISUALIZATION_GRAPHS = '../../visualization/'

dat_gen = DataGenerator(image_path=PATH_TO_TRAIN_IMAGES,
q_path=PATH_TO_TRAIN_QUESTIONS,
a_path=PATH_TO_TRAIN_ANSWERS,
image_rescale=False,
image_horizontal_flip=False,
image_target_size=(150, 150),
use_num_answers=5)

print("Loading train pickles.")
dat_gen.load_qa_into_mem()
dat_gen.prepare_generator_iterable(f_name='../../models/train_data_items.txt')
print("Train pickles loaded successfully")