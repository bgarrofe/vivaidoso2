def upload_path_handler(instance, filename):
    return "images/empresa_{id}/{file}".format(id=instance.empresa.id, file=filename)