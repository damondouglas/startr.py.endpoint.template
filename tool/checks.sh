export secret_file_path='./secret/client_secret.json'
export lib_directory='./lib'
export setup_script='./tool/setup.sh'

if [ -e "$secret_file_path" ]; then
  echo "Found $secret_file_path."
else
  echo "$secret_file_path not found."
  echo "Download client credentials from Google Cloud console to:"
  echo "$secret_file_path"

  exit

fi

if [ -e "$lib_directory" ]; then
  echo "Found $lib_directory."
else
  echo "$lib_directory not found. Run:"
  echo "  bash $setup_script"

  exit

fi
