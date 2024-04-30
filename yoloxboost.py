def setup():
  import subprocess
  def pip_install(name):
    subprocess.call(['pip', 'install', name])
  pip_install('azure-storage-blob')
  pip_install('ultralytics')  
