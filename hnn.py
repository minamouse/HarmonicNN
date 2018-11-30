# import all the important stuff
# import the other files
# import the models
# import the data processing stuff
import sys

if len(sys.argv) < 4:
    raise ValueError('Not enough arguments.')
else:
    FORMAT = sys.argv[1]
    # MODEL = sys.argv[2]
    # DATASET = sys.argv[3]


format_options = []
model_options = []
dataset_options = []


if FORMAT not in format_options:
    raise ValueError('Format option unavailable.')
# elif MODEL not in model_options:
#     raise ValueError('Model option unavailable.')
# elif DATASET not in dataset_options:
#     raise ValueError('Dataset option unavailable.')

# check if this combination has already been trained and if so say something!
