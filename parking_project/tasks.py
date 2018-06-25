from celery import app


@app.task
def test():
    import pdb; pdb.set_trace()
    print('done')
