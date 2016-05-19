from __future__ import absolute_import
from celery import shared_task
from document.models import Document
from document.models import Tag, Neighbour


from celery.signals import worker_process_init
from multiprocessing import current_process

@worker_process_init.connect
def fix_multiprocessing(**kwargs):
    try:
        current_process()._config
    except AttributeError:
        current_process()._config = {'semprefix': '/mp'}


@shared_task
def get_tags(document_id):
    global lda_model

    # if this is the first time it is called load the classifier
    if 'lda_model' not in globals():
        global lda_model
        from sklearn.externals import joblib
        lda_model = joblib.load('worker/pickled_model/lda_model.pkl')

    # Get the objects from the database
    document = Document.objects.filter(id=document_id).first()

    # Get the lda result
    result = lda_model.get_neighbours(document.body)

    # Write the tags
    for tag in result['tags']:
        saving = True
        while saving:
            try:
                Tag(position=tag['position'],
                    score=tag['score'],
                    tag=tag['tag'],
                    document=document).save()
                saving = False
            except:
                pass

    # Write the neighbours
    for neighbour in result['neighbours']:
        saving = True
        while saving:
            try:
                Neighbour(url=neighbour['url'],
                          distance=neighbour['distance'],
                          document=document).save()
                saving = False
            except:
                pass

@shared_task
def build_model():
    from random import randint
    from worker.buildlda import BuildLda
    import os
    lda_model = BuildLda(print_list=False)
    lda_model.build_object()
    from sklearn.externals import joblib

    directory = 'worker/pickled_model/{}'.format(randint(0,1000000))

    if not os.path.exists(directory):
        os.makedirs(directory)

    joblib.dump(lda_model, '{}/lda_model.pkl'.format(directory))