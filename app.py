#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    target = os.environ.get('TARGET', 'World')
    
    request_json = request.json(silent=True)
    request_args = request.args
    filepath = os.path.join("/n01/filestore", "test.txt") # Or your correct path
    
    print("Program stated successfully")
    filepath_filestore = r"/n01/filestore"
    print("The filepath exists:{}".format(os.path.exists(filepath_filestore)))

    result = subprocess.run(
            ['whoami'],  # Command and arguments as a list
            capture_output=True,          # Capture stdout and stderr
            text=True,                     # Decode output as text
            check=True                     # Raise an exception if the command fails (return code != 0)

        )
    print("The Subprocess code whoami:{}".format(result.stdout))
    result = subprocess.run(
            ['df', '-h', "/n01/filestore"],  # Command and arguments as a list
            capture_output=True,          # Capture stdout and stderr
            text=True,                     # Decode output as text
            check=True                     # Raise an exception if the command fails (return code != 0)

        )
    print("The Subprocess code df:{}".format(result.stdout))
    result = subprocess.run(
            ['ls', '-l', "/n01/filestore"],  # Command and arguments as a list
            capture_output=True,          # Capture stdout and stderr
            text=True,                     # Decode output as text
            check=True                     # Raise an exception if the command fails (return code != 0)

        )
    print("The Subprocess code ls:{}".format(result.stdout))

    filepath = os.path.join(filepath_filestore,"test.txt" )
    try:
        with open(filepath, "w") as file:
            file.write("Hello filestore test")
            print(f"File uploaded to Filestore: {filepath_filestore}")
    except PermissionError as e:
        print(f"SalJar Permission Error: {e}")  # Log the full exception
            
    print(f"File uploaded to Filestore: {filepath_filestore}")

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
