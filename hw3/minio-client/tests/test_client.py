import os
import sys

# Ensure that the project root is on sys.path so that "src" is recognized as a package.
# This inserts the absolute path of the parent folder of "tests" (i.e. the project root).
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.client import MinioClient
import tempfile

# Define some constants for testing.
MINIO_HOST = "localhost:9000"
ACCESS_KEY = "admin"
SECRET_KEY = "admin123"
BUCKET = "test-bucket"
OBJECT = "hello.txt"
CONTENT = "hello minio"

def test_crud_operations():
    # Create the MinioClient instance
    mc = MinioClient(MINIO_HOST, ACCESS_KEY, SECRET_KEY)

    # Create bucket
    mc.create_bucket(BUCKET)

    # Upload file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(CONTENT.encode())
        tmp_path = tmp.name

    mc.upload_file(BUCKET, OBJECT, tmp_path)

    # List files to verify the uploaded file is present
    objects = mc.list_files(BUCKET)
    assert any(obj.object_name == OBJECT for obj in objects)

    # Download the file and verify its contents
    download_path = tmp_path + ".dl"
    mc.download_file(BUCKET, OBJECT, download_path)
    with open(download_path, "r") as f:
        assert f.read() == CONTENT

    # Delete the file, then clean up the temporary files
    mc.delete_file(BUCKET, OBJECT)
    os.remove(tmp_path)
    os.remove(download_path)
