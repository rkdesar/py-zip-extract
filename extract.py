import zipfile
import sys 

filename = sys.argv[1]



zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall("/tmp/")
zip_ref.close()
