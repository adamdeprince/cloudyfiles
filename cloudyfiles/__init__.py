import cloudyfiles.s3
import cloudyfiles.cloudfiles

_SERVICES = { 's3': cloudyfiles.s3,
              'cloudfiles': cloudyfiles.cloudfiles }

def factory(bucket, *args, **kwargs):
    if ':' not in bucket:
        raise ValueError(('Cloudydict bucket selectors are of the form '
                          '"service:bucket name"  %r needs at least one :') % bucket )
    service, bucket = bucket.split(':', 1)
    return _SERVICES[service].factory(bucket, *args, **kwargs)
    

def cloudyfiles(*args, **kwargs):
    return factory(*args, **kwargs)()
