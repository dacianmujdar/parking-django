import boto

from parking_project import settings


class MediaStorage:
    _s3 = None

    @classmethod
    def upload_image(cls, img, path):
        if not cls._s3:
            cls._s3 = boto.connect_s3()
            cls.bucket = cls._s3.lookup(settings.AWS_STORAGE_BUCKET_NAME)

        aws_key = cls.bucket.get_key('media/' + path)
        if not aws_key:
            aws_key = boto.s3.key.Key(cls.bucket)
            aws_key.key = 'media/' + path

        aws_key.set_contents_from_string(img.getvalue())

        file_link = settings.MEDIA_URL + path

        return file_link
