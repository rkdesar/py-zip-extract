import zipfile
zip_ref = zipfile.ZipFile("phone.zip", 'r')
zip_ref.extractall("/tmp/")
zip_ref.close()
